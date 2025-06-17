from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import precision_score, recall_score, f1_score, roc_auc_score, roc_curve, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
import os

def calcular_metricas():
    data = load_breast_cancer()
    X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.3, random_state=42)

    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    y_pred_proba = model.predict_proba(X_test)[:, 1]

    # Criar pasta de imagens
    os.makedirs('static/images', exist_ok=True)

    # Confusion Matrix
    cm = confusion_matrix(y_test, y_pred)
    tn, fp, fn, tp = cm.ravel()

    # Plot 1: Curva ROC
    fpr, tpr, thresholds = roc_curve(y_test, y_pred_proba)
    plt.figure()
    plt.plot(fpr, tpr, label=f'AUC = {roc_auc_score(y_test, y_pred_proba):.2f}')
    plt.plot([0,1], [0,1], 'k--')
    plt.xlabel('Taxa de Falsos Positivos')
    plt.ylabel('Taxa de Verdadeiros Positivos')
    plt.title('Curva ROC')
    plt.legend(loc='lower right')
    plt.savefig('static/images/auc_roc.png')
    plt.close()

    # Plot 2: Precision - TP vs FP
    plt.figure()
    plt.bar(['TP', 'FP'], [tp, fp], color=['green', 'red'])
    plt.title('Precisão: TP vs FP')
    plt.ylabel('Quantidade')
    plt.savefig('static/images/precision.png')
    plt.close()

    # Plot 3: Recall - TP vs FN
    plt.figure()
    plt.bar(['TP', 'FN'], [tp, fn], color=['green', 'orange'])
    plt.title('Sensibilidade: TP vs FN')
    plt.ylabel('Quantidade')
    plt.savefig('static/images/recall.png')
    plt.close()

    # Plot 4: F1-Score - Precision vs Recall
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)

    plt.figure()
    plt.bar(['Precisão', 'Sensibilidade'], [precision, recall], color=['blue', 'purple'])
    plt.title('F1-Score: Comparando Precisão e Sensibilidade')
    plt.ylabel('Valor')
    plt.savefig('static/images/f1_score.png')
    plt.close()

    metrics = {
        "precision": round(precision, 2),
        "recall": round(recall, 2),
        "f1_score": round(f1_score(y_test, y_pred), 2),
        "auc_roc": round(roc_auc_score(y_test, y_pred_proba), 2)
    }

    return metrics
