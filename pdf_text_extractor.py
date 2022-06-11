import os
import sys
from pathlib import Path
import numpy as np
import pandas as pd
import PyPDF2 as pypdf


def main():
    df = pd.DataFrame()
    arrayofDF = []

    directory = r'C:\Users\mhursto1\Desktop\FY23Indicators'
    files = [f for f in os.listdir(directory) if os.path.isfile(
        os.path.join(directory, f)) and f.endswith('.pdf')]
    print(files)

    for file in files:
        filepath = directory + "\\" + file
        pdfobject = open(filepath, 'rb')
        pdf = pypdf.PdfFileReader(pdfobject)
        dictionary = pdf.getFormTextFields()
        series = pd.Series(dictionary).to_frame()
        df = pd.DataFrame(pd.Series(dictionary)).T
        # set display max so text doesn't truncate
        pd.set_option('display.max_colwidth', None)
        # print(df)
        arrayofDF.append(df)

    arrayofDF = pd.concat(arrayofDF)
    # print(arrayofDF)
    arrayofDF.to_csv(
        r"C:\Users\mhursto1\Desktop\FY23Indicators\output3.csv", index=None)


if __name__ == '__main__':
    sys.exit(main())
