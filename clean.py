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
    print('\nAvg year: ', df['year'].mean())
    print('\nMean of height column per artist:\n', df.groupby('artist')['height'].transform('mean'))
    print('\nExamine columns with word artist:\n', df.filter(like='artist'))
    print('\nExamine columns with word year (case insensitive):\n', df.filter(regex="(?i)year"))

def adjust_columns(df):
    """ For practice of naming and dropping columns"""

    print('\n\n**** Removing and Fixing Columns Section ****')
    print('\nDrop first row (Not in place):\n', df.drop(0))
    print('\nDrop id column:\n', df.drop('id', axis=1))
    print('\nDrop multiple columns:\n', df.drop(columns=['id', 'year', 'height', 'artistRole', 'creditLine']))
    print('\nDrop multiple rows:\n', df.drop(labels=[0, 1, 2]))
    print('\nData columns:\n', df.columns)
    print('\nData columns to lower (Not in place):\n', df.columns.str.lower())
    data1 = pd.read_csv('artwork_sample.csv')
    data1.columns = map(lambda x: x.lower(), data1.columns)
    print('\nColumns to lowercase using function:\n', data1.columns)
    data1.rename({"thumbnailUrl":"thumbnail"}, axis=1, inplace=True)
    data1.columns = ['id', 'accessionNumber', 'artist', 'artistRole', 'artistId', 'title', 'dateText', 'medium', 'creditLine', 'year', 'acquisitionYear', 'dimensions', 'width', 'height', 'depth', 'units', 'inscription', 'thumbnailCopyright', 'thumbnail', 'url']
    print('\nRenamed columns:\n', data1.columns)

def index_filter(df):
    """ Practice accessing and filtering elements using loc/ilocx"""

    print('\n\n***** Indexing and Filtering Section ****')
    print('\nId column:\n', df['id'])
    print('\nSelect multiple columns:\n', df[['artist', 'title']])
    print('\nSelect range of rows with one column:\n', df[1:5]['artist'])
    print('\nGet rows where year > 1800:\n', df[df['year'] > 1800])
    print('\nOnly show year column for above condition:\n', df[df['year'] > 1800]['year'])
    print('\nGet first row, all cols using loc:\n', df.loc[0, :])
    print('\nGet first three rows, all cols with loc:\n', df.loc[0:2, :])
    print('\nRange of rows/cols using loc:\n', df.loc[[1, 5], ['artist', 'title']])
    print('\nFiltering using loc:\n', df.loc[df['artist'] == 'Blake, Robert', :])
    print('\nGet range of rows, cols using iloc:\n', df.iloc[0:3, 0:3])
    print('\nUse contains method to check condition on medium column:\n', df.medium.str.contains('Graphite'))
    print('\nUse contains and loc to filter on medium column:\n', df.loc[df.medium.str.contains('graphite|line', case=False, regex=True), ['artist', 'medium']])
    print('\nUse contains and loc to filter on year column:\n', df.loc[df['year'].astype(str).str.contains('1826'), :])

def handling_bad_data(df):
    """ Practicing finding and dropping null or duplicate values"""

    print('\n\n**** Handling Bad Data Section ****')
    df['title'] = df['title'].str.strip()
    print('\nStrip white space from title column:\n', df['title'])
    print('\nCheck dateText column:\n', df['dateText'])
    print('\nCheck if dateText column contains NaN values:\n', pd.isna(df.loc[:, 'dateText']))
    df.replace({'dateText': {'date not known': nan}}, inplace=True)
    print('\nAfter replacing date not known values with NaN, check dateText column:\n', df['dateText'])
    print('\nEntries where year contains something other than a number:\n', df.loc[df.year.notnull() & df.year.astype(str).str.contains('[^0-9]')])
    df.loc[df.year.notnull() & df.year.astype(str).str.contains('[^0-9]'), ['year']] = nan
    print('\nCheck year column after replacement:\n', df['year'])
    df.fillna(value={'depth': 0}, inplace=True)
    print('\nReplace nan depth values with 0:\n', df['depth'])
    print('\nDrop all rows with nan values (Not in place):\n', df.dropna())
    print('\nDrop all rows with nan values in certain columns (Not in place):\n', df.dropna(subset=['year', 'acquisitionYear']))
    print('\nDrop rows that are duplicates (Not in place):\n', df.drop_duplicates())
    print('\nDrop rows that have duplicates of certain columns (Not in place):\n', df.drop_duplicates(subset=['artist'], keep='first'))
