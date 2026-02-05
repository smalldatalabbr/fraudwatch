"""
Funções utilitárias do FraudWatch.

Este módulo concentra rotinas auxiliares que dão suporte ao pipeline principal,
como persistência de metadados, rastreabilidade de execuções e organização
de artefatos gerados ao longo da POC.
"""
import numpy as np
import pandas as pd
import json
from datetime import datetime


def save_split_metadata(df_train, df_valid, df_test, path):
    """
    Salva metadados dos conjuntos de treino, validação e teste.

    Registra informações essenciais sobre cada split gerado a partir da divisão
    temporal do dataset, permitindo rastrear alterações no perfil dos dados
    entre diferentes execuções.

    Metadados registrados:
        - timestamp de criação
        - número de registros por conjunto
        - taxa de fraude (proporção de Class = 1)
        - intervalo temporal coberto por cada janela (min(Time), max(Time))

    Parâmetros
    ----------
    df_train : pandas.DataFrame
        Conjunto de treino.

    df_valid : pandas.DataFrame
        Conjunto de validação.

    df_test : pandas.DataFrame
        Conjunto de teste.

    path : str ou Path
        Caminho do arquivo JSON onde os metadados serão salvos.
    """

    metadata = {
        "created_at": datetime.now().isoformat(timespec="seconds"),
        "splits": {
            "train": {
                "rows": int(len(df_train)),
                "fraud_rate": float(df_train["Class"].mean()),
                "time_min": float(df_train["Time"].min()),
                "time_max": float(df_train["Time"].max()),
            },
            "valid": {
                "rows": int(len(df_valid)),
                "fraud_rate": float(df_valid["Class"].mean()),
                "time_min": float(df_valid["Time"].min()),
                "time_max": float(df_valid["Time"].max()),
            },
            "test": {
                "rows": int(len(df_test)),
                "fraud_rate": float(df_test["Class"].mean()),
                "time_min": float(df_test["Time"].min()),
                "time_max": float(df_test["Time"].max()),
            },
        },
    }

    with open(path, "w", encoding="utf-8") as f:
        json.dump(metadata, f, ensure_ascii=False, indent=2)


def to_jsonable(x):
    """
    Converte tipos numpy/pandas para tipos serializáveis em JSON.
    Útil para persistência de métricas, logs e artefatos.
    """
    if isinstance(x, (np.integer, np.int64, np.int32)):
        return int(x)

    if isinstance(x, (np.floating, np.float64, np.float32)):
        return float(x)

    if isinstance(x, np.ndarray):
        return x.tolist()

    if isinstance(x, (pd.Series, pd.Index)):
        return x.to_list()

    if isinstance(x, pd.DataFrame):
        return x.to_dict(orient="records")

    return x
