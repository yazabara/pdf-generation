import logging


class Configuration(object):

    def __init__(self) -> None:
        super().__init__()
        logging.basicConfig(
            filename='../../application.log',
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            datefmt='%m/%d/%Y %I:%M:%S %p',
            level=logging.DEBUG
        )
        self.data_path = "../resources/data/"
        self.templates_path = "../resources/templates/"
        self.reports_path = "../resources/reports/"


configuration = Configuration()
