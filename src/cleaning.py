## This file is for training purposes only  
#  Not being used in the notebooks 


import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import DateTime as dtm

def colname_and_na (df):
    """Description
    :arguments:
    return
    """
    df = pd.read_csv(df)
    df.columns = [i.capitalize().replace(" ", "-") for i in df.columns]
    df.columns=df.columns.str.capitalize().str.replace(' ','-')
    df.columns= df.columns.str.rstrip(' ')
    df.dropna(axis=0, how='all')
    return df

def capitalize_values(value, df):
    for value in df.column:
        df.column = df.column.str.capitalize(value)
        return value


# new = fix_date(df, 'Year')
def fix_date(df, col_year):
    pd.to_datetime(df[col_year] format='%Y', errors='coerce')
    return df


def fix_date_format(date):
    year = int(date)
    if len(str(year)) != 4:
        return np.nan
    return date

