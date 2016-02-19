PDF Text search
===============

This searches a PDF for a any string(s).

## How to Use
> from pdf2txtfunc import pdf2str,searchpdf
>
> pdftext = pdf2str('sample.pdf') #all text of PDF
>
> foundterms = searchpdf('sample.pdf',['foo','bar']) #searches PDF
>
> print foundterms
>
> {'foo': True, 'bar': False}
