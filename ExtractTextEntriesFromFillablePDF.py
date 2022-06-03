#!/usr/bin/env python
# coding: utf-8

pip install PyPDF2

import pandas as pd
import PyPDF2 as pypdf

pdfobject=open(r'C:\Users\mhursto1\Desktop\FY23Indicators\TM_FY23 Quality Indicator Worksheet.pdf','rb') #replace file path and name as appropriate.
pdf=pypdf.PdfFileReader(pdfobject)
dictionary = pdf.getFormTextFields()
dictionary
# Create DataFrame from simple dictionary i.e dictionary with key and simple value like integer or string value.
df = pd.DataFrame(list(dictionary.items()))
#set display max so text doesn't truncate
pd.set_option('display.max_colwidth', None)
df
