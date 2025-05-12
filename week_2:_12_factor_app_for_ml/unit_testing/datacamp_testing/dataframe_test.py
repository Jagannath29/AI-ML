import pytest
import pandas as pd

DF_PATH = "/usr/local/share/salaries.csv" # Not correct path
@pytest.fixture
def read_df():
    return pd.read_csv(DF_PATH)

def get_grouped(df):
    return df.groupby('work_year').agg({'salary': 'describe'})['salary']

def test_read_df(read_df):
    # Check the type of the dataframe
    assert isinstance(read_df, pd.DataFrame)
    # Check that df contains rows
    assert read_df.shape[0] > 0

def test_grouped(read_df):
    df = read_df
    salary_by_year = get_grouped(df)
    # Check the nulls here
    assert salary_by_year.isna().sum().sum() == 0




# Another test

''' import pytest
import pandas as pd

DF_PATH = "/usr/local/share/salaries.csv"
@pytest.fixture
def read_df():
    return pd.read_csv(DF_PATH)

def get_grouped(df):
    return df.groupby('work_year').agg({'salary': 'describe'})['salary']

def test_feature_2022(read_df):
    salary_by_year = get_grouped(read_df)
    salary_2022 = salary_by_year.loc[2022, '50%']
    # Check the median type here
    assert isinstance(salary_2022, float)
    # Check the median is greater than zero
    assert 0 < salary_2022

# Use benchmark here
def test_reading_speed(benchmark):
    benchmark(pd.read_csv, DF_PATH) '''

