from sklearn.metrics import accuracy_score, f1_score, roc_auc_score

def evaluate(model, X, y):
    preds = model.predict(X)
    probs = model.predict_proba(X)[:, 1]
    return {
        "accuracy": accuracy_score(y, preds),
        "f1": f1_score(y, preds),
        "roc_auc": roc_auc_score(y, probs)
    }
