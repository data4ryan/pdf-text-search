from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice, TagExtractor
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import XMLConverter, HTMLConverter, TextConverter
from pdfminer.cmapdb import CMapDB
from pdfminer.layout import LAParams
from pdfminer.image import ImageWriter
from unicodedata import normalize
import re

#TextConverterToString has custom write_text function to allow writing to string
class TextConverterToString(TextConverter):
    def write_text(self, text):
        if isinstance(self.outfp,str):
            if isinstance(text,str):
                self.outfp += text
            elif isinstance(text,unicode):
                #self.outfp += text.encode(self.codec,'ignore')
                self.outfp += normalize('NFKD',text).encode('ascii','ignore')
            else:
                print 'Funny character found...'
        else:
            self.outfp.write(text.encode(self.codec, 'ignore'))
        return

# pdf2str function was converted from PDFMiner's pdf2txt.py function to return
# string (instead of sending output to a file or stdout)
def pdf2str(pdffilename):
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
                                  check_extractable=False):
        page.rotate = (page.rotate+rotation) % 360
        interpreter.process_page(page)
    fp.close()
    device.close()

    return device.outfp

#searches a pdf for a term (or list of terms) and returns a dictionary with the
#appropriate boolean value if it contains the term
def searchpdf(pdffilename,searchterms):
    has_terms = {}

    if !isinstance(type(searchterms),list):
        terms = [searchterms]
    else:
        terms = searchterms

    [has_terms[term]=False for term in terms]

    pdftext = pdf2str(pdffilename) #converting pdf to text
    for term in terms:
        myregex = re.escape(term)
        m = re.search(r'('+myregex+r')',pdftext)
        if m is not None: has_terms[term] = True

    return has_terms
