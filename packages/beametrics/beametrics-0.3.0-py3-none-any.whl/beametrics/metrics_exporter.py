import json
import logging
import time
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Dict, Optional, Protocol, Union

import apache_beam as beam
from apache_beam.options.value_provider import ValueProvider
from google.api_core import exceptions as google_exceptions
from google.cloud import monitoring_v3


class ConnectionConfig(Protocol):
    """Protocol for connection configuration"""

    pass


@dataclass
class GoogleCloudConnectionConfig(ConnectionConfig):
    """Configuration for Google Cloud connection"""

    project_id: str

    @property
    def project_name(self) -> str:
        return f"projects/{self.project_id}"


@dataclass
class ExporterConfig(Protocol):
    """Configuration for metrics exporting"""

    metric_name: str
    metric_labels: Union[ValueProvider, dict[str, str]]
    connection_config: ConnectionConfig
    export_type: str


@dataclass
class GoogleCloudExporterConfig(ExporterConfig):
    """Configuration for Google Cloud metrics exporting"""

    metric_name: str
    metric_labels: Union[ValueProvider, dict[str, str]]
    connection_config: GoogleCloudConnectionConfig
    export_type: str = "google-cloud-monitoring"


class MetricsExporter(ABC):
    """Base class for exporting metrics"""

    def __init__(self, config: ExporterConfig):
        self.config = config

    @abstractmethod
    def export(
        self, value: float, dynamic_labels: Optional[Dict[str, str]] = None
    ) -> None:
        """Exports a metric value with optional dynamic labels"""
        pass


class GoogleCloudMetricsExporter(MetricsExporter):
    """Export metrics to Google Cloud Monitoring"""

    def __init__(self, config: GoogleCloudExporterConfig):
        self.config: GoogleCloudExporterConfig = config
        self.client = monitoring_v3.MetricServiceClient()

    def export(
        self, value: float, dynamic_labels: Optional[Dict[str, str]] = None
    ) -> None:
        """Exports a metric value with optional dynamic labels"""
        now = time.time()
        seconds = int(now)
        aligned_seconds = seconds - (seconds % 60)

        series = monitoring_v3.TimeSeries()
        series.metric.type = self.config.metric_name

        if isinstance(self.config.metric_labels, ValueProvider):
            if isinstance(
                self.config.metric_labels,
                beam.options.value_provider.StaticValueProvider,
            ):
                final_labels = json.loads(self.config.metric_labels.get())
            else:
                final_labels = {}
        else:
            final_labels = self.config.metric_labels

        if dynamic_labels:
            final_labels.update(dynamic_labels)

        series.metric.labels.update(final_labels)
        series.resource.type = "global"

        point = monitoring_v3.Point()
        point.value.double_value = value
        interval = monitoring_v3.TimeInterval(
            {
                "end_time": {"seconds": aligned_seconds, "nanos": 0},
                "start_time": {"seconds": aligned_seconds, "nanos": 0},
            }
        )
        point.interval = interval
        series.points = [point]

        request = monitoring_v3.CreateTimeSeriesRequest(
            name=self.config.connection_config.project_name,
            time_series=[series],
        )

        try:
            self.client.create_time_series(request=request)
        except google_exceptions.InvalidArgument:
            pass
        except Exception:
            raise


class MetricsExporterFactory:
    """Factory class for creating MetricsExporter instances"""

    @staticmethod
    def create_exporter(config: ExporterConfig) -> MetricsExporter:
        """Create a MetricsExporter instance based on export type.

        Args:
            export_type: Type of exporter ("google-cloud-monitoring", etc)
            config: Configuration for the exporter

        Returns:
            MetricsExporter: An instance of the appropriate exporter

        Raises:
            ValueError: If export_type is not supported or config type is invalid
        """
        if not isinstance(config, GoogleCloudExporterConfig) and not isinstance(
            config, LocalExporterConfig
        ):
            raise ValueError("Invalid config type for metrics exporter")

        export_type = config.export_type
        if export_type == "google-cloud-monitoring":
            if not isinstance(config, GoogleCloudExporterConfig):
                raise ValueError("Invalid config type for monitoring exporter")
            return GoogleCloudMetricsExporter(config)
        elif export_type == "local":
            if not isinstance(config, LocalExporterConfig):
                raise ValueError("Invalid config type for local exporter")
            return LocalMetricsExporter(config)

        raise ValueError(f"Unsupported export type: {export_type}")


class ExportMetrics(beam.DoFn):
    def __init__(self, exporter_config: GoogleCloudExporterConfig):
        self.exporter_config = exporter_config
        self.exporter = None

    def setup(self):
        self.exporter = MetricsExporterFactory.create_exporter(self.exporter_config)

    def process(self, element):
        try:
            self.exporter.export(float(element["value"]), element["labels"])
            yield element
        except Exception as e:
            logging.error(f"Error exporting metrics: {e}")
            yield element


@dataclass
class LocalExporterConfig(ExporterConfig):
    """Configuration for local metrics exporting"""

    metric_name: str
    metric_labels: Union[ValueProvider, dict[str, str]]
    connection_config: ConnectionConfig
    export_type: str = "local"


class LocalMetricsExporter(MetricsExporter):
    """Export metrics to local(stdout for now)"""

    def export(
        self, value: float, dynamic_labels: Optional[Dict[str, str]] = None
    ) -> None:
        now = time.time()
        final_labels = {}

        if isinstance(self.config.metric_labels, ValueProvider):
            if isinstance(
                self.config.metric_labels,
                beam.options.value_provider.StaticValueProvider,
            ):
                final_labels = json.loads(self.config.metric_labels.get())
        else:
            final_labels = self.config.metric_labels

        if dynamic_labels:
            final_labels.update(dynamic_labels)

        metric_name = (
            self.config.metric_name.get()
            if isinstance(self.config.metric_name, ValueProvider)
            else self.config.metric_name
        )

        output = {
            "timestamp": now,
            "metric_name": metric_name,
            "value": value,
            "labels": final_labels,
        }

        print(json.dumps(output))
