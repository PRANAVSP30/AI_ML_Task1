def dataset_summary(df):
    """
    This returns a dictionary containing summary of dataset:
    - shape
    - list of columns
    - data types
    - missing value counts
    - unique value counts

    This gives a complete overview of the dataset in one place.
    """
    summary = {
        "shape": df.shape,
        "columns": df.columns.tolist(),
        "dtypes": df.dtypes.astype(str).to_dict(),
        "null_counts": df.isnull().sum().to_dict(),
        "unique_counts": df.nunique().to_dict()
    }
    return summary


def classify_features(df):
    """
    Classifies features into:
    - numerical
    - categorical
    - binary
    - ordinal (added manually later)

    """
    numerical = []
    categorical = []
    binary = []
    ordinal = []  # manual later

    for col in df.columns:
        if df[col].dtype in ["int64", "float64"]:
            if df[col].nunique() == 2:
                binary.append(col)
            else:
                numerical.append(col)
        else:
            categorical.append(col)

    return numerical, categorical, binary, ordinal
