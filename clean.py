import pandas as pd
from numpy import nan


data = pd.read_csv('artwork_sample.csv')
# data = pd.read_csv('artwork_sample.csv', usecols=['artist', 'title'])

# print(data.head())
# print(data.columns.str.lower())
# data.columns = [x.lower() for x in data.columns]
# import re# data.colums = [re.sub(r'([A-Z])', r'_\1', x).lower() for x in data.columns]
# data.rename(columns={'thumbnailUrl': 'thumbnail'}, inplace=True)
# data.rename(columns=lambda x: x.lower(), inplace=True)
# print(data.columns)

def process_file(path):
    """ Read file containing the artwork information"""

    data = pd.read_csv(path, low_memory=False)
    return data

def understand_data(df):
    """Interpret data by grouping tasks and performning basic agregate"""

    print('\n*** Understanding Data Section ***')
    print('\nData head:\n', df.head())
    print('\nData types of columns:\n', df.types)
    df.year = pd.to_numeric(df.year, errors='coerce')
    df.height = pd.to_numeric(df.height, errors='coerce')
    print('\nData types following conversion:\n', df.types)
    print('\nMin year: ', df['year'].min())
    print('\nMax year: ', df['year'].max())
    print('\nAvg year: ', df['year'].mean)