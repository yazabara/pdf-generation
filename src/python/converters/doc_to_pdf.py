import os

import comtypes.client

from converters.file_converter import FileConverter


class DocToPdf(FileConverter):
    WD_FORMAT_PDF = 17

    def convert(self, input_file, output_file):
        in_file = os.path.abspath(input_file)
        out_file = os.path.abspath(output_file)
        word = comtypes.client.CreateObject('Word.Application')
        doc = word.Documents.Open(in_file)
        doc.SaveAs(out_file, FileFormat=DocToPdf.WD_FORMAT_PDF)
        doc.Close()
        word.Quit()


doc_to_pdf = DocToPdf()
