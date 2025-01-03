import time
from abc import ABC, abstractmethod
from datetime import datetime

from unitsnet_py.units.bit_rate import BitRate, BitRateUnits
from unitsnet_py.units.duration import Duration, DurationUnits


class ConnResult(ABC):
    """ Abstract base class representing a connectivity check result. """

    protocol = None
    success = False
    alert = False
    deviation: Duration = None
    error_message = None
    timestamp = None

    asset = None
    """ The asset to perform the test on (e.g., URL, domain name). """

    def __init__(self):
        self.timestamp = datetime.now().isoformat()

    # Optional properties, relevant to a specific protocol/s implementation
    latency: Duration = None
    upload_bandwidth: BitRate = None
    download_bandwidth: BitRate = None

    def to_dics(self) -> dict:
        obj = {
            'protocol': self.protocol.value,
            'success': self.success,
            'alert': self.alert,
            'timestamp': self.timestamp,
            'asset': self.asset,
        }

        if self.deviation:
            obj['deviation'] = self.deviation.to_dto_json(DurationUnits.Second)

        if self.error_message:
            obj['error_message'] = self.error_message

        if self.latency:
            obj['latency'] = self.latency.to_dto_json(DurationUnits.Second)

        if self.upload_bandwidth:
            obj['upload_bandwidth'] = self.upload_bandwidth.to_dto_json(BitRateUnits.MegabitPerSecond)

        if self.download_bandwidth:
            obj['download_bandwidth'] = self.download_bandwidth.to_dto_json(BitRateUnits.MegabitPerSecond)
        return obj

    @staticmethod
    def from_dict(data: dict):
        result = ConnResult()
        result.protocol = data['protocol']
        result.asset = data['asset']
        result.success = data['success']
        result.timestamp = data['timestamp']
        result.alert = data.get('alert')
        result.error_message = data.get('error_message')
        result.deviation = None if data.get('deviation') is None else Duration.from_dto_json(data.get('deviation'))
        result.latency = None if data.get('latency') is None else Duration.from_dto_json(data.get('latency'))
        result.upload_bandwidth = None if data.get('upload_bandwidth') is None else BitRate.from_dto_json(
            data.get('upload_bandwidth'))
        result.download_bandwidth = None if data.get('download_bandwidth') is None else BitRate.from_dto_json(
            data.get('download_bandwidth'))
        return result
