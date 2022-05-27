#!/usr/bin/env python3
# This is a sample Python script.
from dsa.utils import DSADataGen
from pprint import pprint
import pandas as pd

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    dgen = DSADataGen()

    athletes = dgen.getAthletes(500)
    df = pd.DataFrame(athletes)
    print(df)

    writer = pd.ExcelWriter('./entries.xlsx', engine='xlsxwriter')
    df.to_excel(writer)
    writer.save()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
