import logging

from ch.sachi.weatherstation.logging import configure_logging
from ch.sachi.weatherstation.measureRepository import MeasureRepository
from ch.sachi.weatherstation.sensorService import SensorService
from .config import *


class Main:
    def __init__(self, sensor_service: SensorService, repo: MeasureRepository):
        self.sensor_service = sensor_service
        self.repo = repo

    def run(self) -> None:
        logging.debug('Start getting measures')
        measures = self.sensor_service.get_measures()
        for measure in measures:
            self.repo.save(measure)
        logging.debug('Handled ' + str(len(measures)) + ' measures')


def main():
    config = read_configuration()
    configure_logging(config.loglevel)
    sensor_service = SensorService(config.broker.outdoor_weather_uid)
    repo = MeasureRepository(config.database)
    repo.init()
    Main(sensor_service, repo).run()


if __name__ == '__main__':
    main()
