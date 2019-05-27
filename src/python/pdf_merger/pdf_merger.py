from typing import List

from PyPDF2 import PdfFileMerger


class PdfMerger(object):

    def __init__(self) -> None:
        super().__init__()
        self.merger = PdfFileMerger()

    def merge(self, files: List[str], result_name: str):
        for pdf in files:
            self.merger.append(pdf, bookmark="File {} ".format(pdf))
        self.merger.write(result_name)


pdf_merger = PdfMerger()
