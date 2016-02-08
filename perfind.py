#!/tankhome/rchughes/Python-2.7.3/python
from sqlalchemy import create_engine, distinct, Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime as dt
#from docx import Document

#pubengine = create_engine('sqlite:////tankhome/rchughes/acebox2/db/ace_publications.db',echo=False)
pubengine = create_engine('postgresql://acelib:readonly@localhost:5432/web_data',echo=False)
pubBase = declarative_base(pubengine)

class publication(pubBase):
    __tablename__='publications'
    __table_args__ = {'autoload':True}

    def __str__(self):
        return "Publication Title: {!s}".format(self.title)

class bookpublication(pubBase):
    __tablename__='acebookpublications'
    __table_Args__ = {'autoload':True}
    pub_id = Column(Integer,primary_key=True)

class group(object):
    def __init__(self,title):
        self.title = str(title)
        self.list = [] #list of simplepub objects
    
    def add(self,publication):
        #extract all desired information and create docpub object
        authors = publication.lead_author_surname+', '+publication.lead_author_given_names
        if publication.coauthors is not None: 
            authors = authors+', '+publication.coauthors
        title = publication.title
        journal = publication.journal_name
        volume = publication.volume
        page = publication.pages
        pubdate = publication.pub_date
        
        self.list.append(simplepub(authors,title,journal,volume,page,pubdate)) #add to list

    def __len__(self):
        return len(self.list)

class simplepub(object):
    def __init__(self,authors,title,journal,volume,page,pubdate):
        self.authors = authors
        self.title = title
        self.journal = journal
        self.volume = volume
        self.page = page
        self.pub_date = pubdate

def createpublist(year):
    solaratlasgr = group('Solar Atlas')
    conferencegr = group('Conference')
    bookgr = group('ACE Book')
    pubsgr = group('')

    metadata = pubBase.metadata
    pubSession = sessionmaker(bind=pubengine)
    mysession = pubSession()
    categs = mysession.query(distinct(publication.category)).\
        filter(publication.pub_date>dt(year,1,1,0,0,0)).\
        filter(publication.pub_date<dt(year,12,31,23,59,59)).all() #distinct categories
    #print categs
    categories = [str(x[0]) for x in categs]
    '''categories = []
    for x in categs:
        #print x
        #print type(x[0])
        #print str(x[0])
        #categories.append(x)  #but this one carries on it's merry way
        categories.append(str(x[0]))   #this line breaks it'''
    for category in categories:
        print 'category: ',category
        mypubs = mysession.query(publication).\
            filter(publication.pub_date>dt(year,1,1,0,0,0)).\
            filter(publication.pub_date<dt(year,12,31,0,0,0)).\
            filter(publication.category==category)
        for pub in mypubs:
            if category=='solaratlas': solaratlasgr.add(pub)
            elif category=='conference': conferencegr.add(pub)
            else: pubsgr.add(pub)
    
    print 'Solar Atlas Papers: ', len(solaratlasgr)
    print 'Conference Papers: ', len(conferencegr)
    print 'All Other Papers: ', len(pubsgr)

    #get ace book publications
    #bookgr = ...
    
    #creating the document
    #doc = Document()
    #doc.add_heading('ACE Publications for '+str(year),0)
    
if __name__ == "__main__":
    createpublist(2015)
    
