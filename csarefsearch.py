'''this file searches the journal publications PDF files for the acknowledgement
to the CSA'''

import glob
import re
from pdf2txtfunc import searchpdf

def searchyear(year):
    #pubfolder = '/tankhome/rchughes/acebox2/publications/'
    pubfolder = './'
    pubfiles = glob.glob(pubfolder+str(year)+'/*.pdf') #find all publications
    termsfound = {}

    for file in pubfiles:
        #folderfile = file.split('/')[-2]+'/'+file.split('/')[-1]
        #print '*** Converting PDF to text: '+folderfile+'...'
        #pdftext = pdf2txt(file)
        #print '*** Searching file: '+folderfile+'...'
        #files_with_reference = []
        #for searchterm in ['Space', 'Agency','CSA','anadian']:
        #    myregex = re.escape(searchterm)
        #    m = re.search(r'('+myregex+r')',pdftext)
        #    if m is not None:
        #        files_with_reference.append(file)
        #        print 'File '+folderfile+' contains term \''+searchterm+'\'.'

        searchterms = ['Space','Agency','CSA','anadian']
        termsfound[file.split('/')[-1]] = searchpdf(file,searchterms)

    return termsfound

if __name__ == "__main__":
    searchyear(2015)
