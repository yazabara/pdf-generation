import comtypes.client

from converters.file_converter import FileConverter


class DocToPdf(FileConverter):
    WD_FORMAT_PDF = 17

    def convert(self, input_file, output_file):
        word = comtypes.client.CreateObject('Word.Application')
        doc = word.Documents.Open(input_file)
        doc.SaveAs(output_file, FileFormat=DocToPdf.WD_FORMAT_PDF)
        doc.ExportAsFixedFormat(
            OutputFileName=output_file,
            ExportFormat=DocToPdf.WD_FORMAT_PDF,
            OpenAfterExport=False,
            OptimizeFor=0,
            CreateBookmarks=1,
            DocStructureTags=True
        )
        doc.Close()
        word.Quit()


doc_to_pdf = DocToPdf()
