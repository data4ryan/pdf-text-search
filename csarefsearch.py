'''this file searches the journal publications PDF files for the acknowledgement
to the CSA'''

import glob
import re
from pdf2txtfunc import pdf2txt

def searchyear(year):
    pubfolder = '/tankhome/rchughes/acebox2/publications/'
    pubfiles = glob.glob(pubfolder+str(year)+'/*.pdf') #get all the publications

    for i,file in enumerate(pubfiles):
        if i>1: continue #for testing
        print '*** Converting PDF to text: '+ file +'...'
        pdftext = pdf2txt(file)
        print pdftext
        print '*** Searching file: '+file
        files_with_reference = []
        for searchterm in ['Canadian Space Agency','CSA','anadian']:
            myregex = re.escape(searchterm)
            m = re.search(r'('+myregex+r')',pdftext)
            if m is not None:
                files_with_reference.append(file)
                print 'File '+file+' contains term \''+searchterm+'\'.'

if __name__ == "__main__":
    searchyear(2015)
