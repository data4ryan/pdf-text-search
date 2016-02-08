'''this file searches the journal publications PDF files for the acknowledgement
to the CSA'''

import glob
import re

def searchyear(year):
    pubfolder = '/tankhome/rchughes/acebox2/publications/'
    pubfiles = glob.glob(pubfolder+str(year)+'/*.pdf') #get all the publication files


    for file in pubfiles:
        print '*** Searching file: '+file
        all_canSpcAgn = []
        for searchterm in ['Canadian Space Agency','CSA','anadian']:
            myregex = re.escape(searchterm)
            for linenum,line in enumerate(open(file,'r')):
                m = re.search(r'('+myregex+r')',line)
                if m is not None:
                    #print 'Line #: ', linenum
                    all_canSpcAgn.append(linenum)
            print 'Found '+str(len(all_canSpcAgn))+' references of \''+searchterm+'\'.'

if __name__ == "__main__":
    searchyear(2015)
