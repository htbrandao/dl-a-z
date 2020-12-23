import pandas

def _value_counts(df):
    """
    Generalizes pd.value_counts() to all columns
    """
    for c in df.columns:
        print(f'# {c}:\n{df[c].value_counts()}\n\n')


def _describe(df):
    """
    Generalizes pd.describe() to all columns
    """
    for c in df.columns:
        print(f'# {c}:\n{df[c].describe()}\n\n')


def _isnull(df):
    """
    Generalizes pd.isnull() to all columns
    """
    for c in df.columns:
        cnt = df[pandas.isnull(df[c])].shape[0]
        if cnt != 0:
            print(f'# {c}: {cnt} rows')
