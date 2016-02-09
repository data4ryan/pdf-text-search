from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice, TagExtractor
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import XMLConverter, HTMLConverter, TextConverter
from pdfminer.cmapdb import CMapDB
from pdfminer.layout import LAParams
from pdfminer.image import ImageWriter

class TextConverterToString(TextConverter):
    def write_text(self, text):
        if isinstance(self.outfp,basestring):
            self.outfp += text
        else:
            self.outfp.write(text.encode(self.codec, 'ignore'))
        return

# pdf2txt function was converted from PDFMiner's pdf2txt.py function to return
# string (instead of sending output to a file or stdout)
def pdf2txt(pdffilename):
    pagenos = set()
    outfp = ''
    caching = False
    rotation = 0
    rsrcmgr = PDFResourceManager(caching=caching)

    device = TextConverterToString(rsrcmgr, outfp, codec='utf-8',
                               laparams=LAParams(), imagewriter=None)

    fp = file(pdffilename, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    for page in PDFPage.get_pages(fp, pagenos,
                                  maxpages=0, password='', caching=caching,
                                  check_extractable=True):
        page.rotate = (page.rotate+rotation) % 360
        interpreter.process_page(page)
    fp.close()
    device.close()

    return outfp
