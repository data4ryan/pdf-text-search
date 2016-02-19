PDF Text search
===============

This searches a PDF for a any string(s).

## How to Use
Get all text from PDF
> from pdf2txtfunc import pdf2str
>
> pdftext = pdf2str('sample.pdf')


Searched PDF for certain words/string
> from pdf2txtfunc import searchpdf
>
> foundterms = searchpdf('sample.pdf',['foo','bar'])
>
> print foundterms
>
> {'foo': True, 'bar': False}
