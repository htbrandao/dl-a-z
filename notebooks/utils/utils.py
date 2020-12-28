import pandas as pd


def _value_counts(df):
    """
    Generalizes pd.value_counts() to all columns
    """
    print('>> Value counts:\n')
    for c in df.columns:
        print(f'# {c}:\n{df[c].value_counts()}\n\n')


def _describe(df):
    """
    Generalizes pd.describe() to all columns
    """
    print('>> Describe columns:\n')
    for c in df.columns:
        print(f'# {c}:\n{df[c].describe()}\n\n')


def _isnull(df):
    """
    Generalizes pd.isnull() to all columns
    """
    print('>> Null registers:\n')
    for c in df.columns:
        cnt = df[pd.isnull(df[c])].shape[0]
        if cnt == 0:
            print(f'# {c}: 0 null rows')
        else:
            print(f'# {c}: {cnt} rows')
