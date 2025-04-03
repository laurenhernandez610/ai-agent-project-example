# ------------------------------------------------------------------------------
# fine_tune.py
# ------------------------------------------------------------------------------
# This module is optional. It is a placeholder for training or fine-tuning
# classical ML models or small transformer models.
#
# You might use this to:
# - Fine-tune a classification model
# - Fit a clustering algorithm
# - Train embeddings for retrieval
# ------------------------------------------------------------------------------

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def train_dummy_model(X, y):
    """
    Trains a simple logistic regression model.

    Args:
        X (np.ndarray): Feature matrix.
        y (np.ndarray): Labels.

    Returns:
        model: Trained scikit-learn model.
    """
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    model = LogisticRegression()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    print(f"Accuracy: {acc:.2f}")

    return model
