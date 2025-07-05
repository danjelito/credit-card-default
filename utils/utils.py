from tabulate import tabulate
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score,
    f1_score,
    recall_score,
    precision_score,
    confusion_matrix,
)
from collections import namedtuple


def print_df_in_chunks(df, n):
    """
    Prints the DataFrame in chunks of n columns using tabulate.

    Parameters:
    df (pd.DataFrame): The DataFrame to print.
    n (int): The number of columns per chunk.
    """
    start = 0
    end = n
    total_columns = df.shape[1]

    while start < total_columns:
        print(tabulate(df.iloc[:, start:end].head(), headers="keys", tablefmt="orgtbl"))
        start = end
        end += n
        print()  # Add an empty line between chunks for better readability


def split_dataset(x, y, test_size=0.2, val_size=0.1, random_state=None):
    """Split the dataset into train, validation, and test sets."""
    x_train_val, x_test, y_train_val, y_test = train_test_split(
        x, y, test_size=test_size, random_state=random_state
    )
    # Adjust validation size to the remaining training set
    val_fraction_of_train = val_size / (1 - test_size)
    x_train, x_val, y_train, y_val = train_test_split(
        x_train_val,
        y_train_val,
        test_size=val_fraction_of_train,
        random_state=random_state,
    )
    return x_train, x_val, x_test, y_train, y_val, y_test


def return_clf_score(y_true, y_pred):
    acc = accuracy_score(y_true, y_pred)
    f1 = f1_score(y_true, y_pred, average="weighted")
    precision = precision_score(y_true, y_pred, average="weighted", zero_division=0.0)
    recall = recall_score(y_true, y_pred, average="weighted")
    matrix = confusion_matrix(y_true, y_pred, normalize="true")
    Scores = namedtuple("Scores", ["acc", "f1", "precision", "recall", "matrix"])
    return Scores(acc, f1, precision, recall, matrix)


def print_clf_score(scores, title="Classification Report"):
    print(f"\n=== {title} ===")
    print(f"Accuracy : {scores.acc:.4f}")
    print(f"F1 Score : {scores.f1:.4f}")
    print(f"Precision: {scores.precision:.4f}")
    print(f"Recall   : {scores.recall:.4f}")
    print("Confusion Matrix (normalized):")
    print(scores.matrix)
