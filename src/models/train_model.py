import mlflow
import pandas as pd
import mlflow.lightgbm
from lightgbm import LGBMClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, recall_score, f1_score

def train_model(df: pd.DataFrame, target_col: str):
    """
    Trains a LightGBM model and logs with MLflow.

    Args:
        df (pd.DataFrame): Feature dataset.
        target_col (str): Name of the target column.
    """
    X = df.drop(columns=[target_col])
    y = df[target_col]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=12345
    )
    n_est = 300
    model = LGBMClassifier(
        n_estimators=n_est,
        learning_rate=0.1,
        max_depth=-1,
        random_state=42,
        n_jobs=-1, # use all threads
        objective='binary',
#        class_weight = 'balanced' # to be used only in multi-class classification
        is_unbalance = True
    )

    with mlflow.start_run():
        # Train model
        model.fit(X_train, y_train)
        preds = model.predict(X_test)
        acc = accuracy_score(y_test, preds)
        rec = recall_score(y_test, preds)
        f1 = f1_score(y_test, preds)

        # Log params, metrics, and model
        mlflow.log_param("n_estimators", n_est)
        mlflow.log_metric("accuracy", acc)
        mlflow.log_metric("recall", rec)
        mlflow.log_metric("f1-score", f1)
        mlflow.lightgbm.log_model(model, "model")

        # Log dataset so it shows in MLflow UI
        train_ds = mlflow.data.from_pandas(df, source="training_data")
        mlflow.log_input(train_ds, context="training")

        print(f"Model trained. Accuracy: {acc:.4f}, Recall: {rec:.4f}, F1: {f1:.4f}")