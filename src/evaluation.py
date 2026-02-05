"""
Módulo de avaliação de modelos para a POC FraudWatch.

Este módulo contém funções utilitárias para:
- geração de métricas
- análise de thresholds
- visualização de resultados
- avaliação padronizada no conjunto de validação

O módulo é determinístico e não controla estado global (ex: seeds).
"""

# Imports bibliotecas

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.metrics import (
    average_precision_score,
    precision_recall_curve,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
)

# Curva Precision–Recall

def plot_pr_curve(y_true, proba, title=None, savepath=None):
    precisions, recalls, _ = precision_recall_curve(y_true, proba)
    pr_auc = average_precision_score(y_true, proba)

    plt.figure(figsize=(6, 4))
    plt.plot(recalls, precisions, label=f"PR-AUC = {pr_auc:.3f}")
    plt.xlabel("Recall")
    plt.ylabel("Precision")
    plt.title(title or "Precision-Recall Curve")
    plt.legend()
    plt.grid(True)

    if savepath:
        plt.savefig(savepath, bbox_inches="tight")

    plt.show()

    return pr_auc

# Matriz de confusão (plot)

def plot_confusion(cm, title=None, savepath=None, cmap="Blues", labels=("Legit", "Fraud")):
    cm = np.asarray(cm)

    fig, ax = plt.subplots(figsize=(6, 4))
    im = ax.imshow(cm, cmap=cmap)
    ax.set_title(title or "Confusion Matrix")
    fig.colorbar(im, ax=ax)

    # Anotações
    for i in range(cm.shape[0]):
        for j in range(cm.shape[1]):
            ax.text(j, i, int(cm[i, j]), ha="center", va="center")

    ax.set_xlabel("Predicted")
    ax.set_ylabel("Actual")

    # ✅ ticks limpos (remove -0.5, 0.0…)
    ax.set_xticks([0, 1])
    ax.set_yticks([0, 1])
    ax.set_xticklabels(labels, rotation=0)
    ax.set_yticklabels(labels, rotation=0)

    # ✅ mata a grade que o tema pode ter ligado
    ax.grid(False)

    # ✅ evita “sombra”/bordas estranhas
    ax.set_axisbelow(False)

    if savepath:
        fig.savefig(savepath, bbox_inches="tight")

    plt.tight_layout()
    plt.show()

# Tabela de thresholds

def make_threshold_table(y_true, proba):
    precisions, recalls, thresholds = precision_recall_curve(y_true, proba)

    df = pd.DataFrame({
        "threshold": thresholds,
        "precision": precisions[:-1],
        "recall": recalls[:-1],
    })

    df["f1"] = 2 * (df["precision"] * df["recall"]) / (
        df["precision"] + df["recall"]
    ).replace(0, np.nan)

    df["alerts"] = (proba.reshape(-1, 1) >= thresholds).sum(axis=0)
    df["alert_rate"] = df["alerts"] / len(y_true)

    return df

# Seleção de threshold por política

def select_threshold(threshold_df, min_precision):
    candidates = threshold_df[threshold_df["precision"] >= min_precision]

    if candidates.empty:
        raise ValueError(
            f"Nenhum threshold atende à precisão mínima ({min_precision})."
        )

    best = candidates.sort_values(
        by=["recall", "precision"],
        ascending=[False, False]
    ).iloc[0]

    return float(best["threshold"]), best

# Avaliação padronizada no VALID

def evaluate_on_valid(
    model_name,
    y_valid,
    proba_valid,
    min_precision,
):
    pr_auc = average_precision_score(y_valid, proba_valid)

    threshold_df = make_threshold_table(y_valid, proba_valid)
    threshold, best_row = select_threshold(threshold_df, min_precision)

    y_pred = (proba_valid >= threshold).astype(int)

    cm = confusion_matrix(y_valid, y_pred)

    return {
        "model": model_name,
        "pr_auc_valid": pr_auc,
        "chosen_threshold": threshold,
        "precision_valid": precision_score(y_valid, y_pred, zero_division=0),
        "recall_valid": recall_score(y_valid, y_pred, zero_division=0),
        "f1_valid": f1_score(y_valid, y_pred, zero_division=0),
        "alerts_valid": int(best_row["alerts"]),
        "alert_rate_valid": float(best_row["alert_rate"]),
        "confusion_matrix_valid": cm,
        "threshold_table": threshold_df,
    }
