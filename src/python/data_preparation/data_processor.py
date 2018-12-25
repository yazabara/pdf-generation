import logging

import numpy as np
import pandas as pd


class DataProcessor(object):
    """
    Data Processor prepares data for PDF (makes a data structure)
    """

    def __init__(self) -> None:
        super().__init__()
        self.logger = logging.getLogger("Data Processor")
        self.logger.debug('Data Processor initialized')

    def prepare_sample(self, data_frame):
        self.logger.info("Application prepares data for {}".format(data_frame.head()))
        return pd.pivot_table(data=data_frame,
                              index=["Manager", "Rep", "Product"],
                              values=["Price", "Quantity"],
                              aggfunc=[np.sum, np.mean],
                              fill_value=0)


data_processor = DataProcessor()
