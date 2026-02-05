"""
Definição centralizada dos caminhos de diretórios e arquivos do projeto FraudWatch.

Este módulo descreve a topologia do repositório e fornece caminhos absolutos
para leitura e escrita de dados, modelos, relatórios e artefatos intermediários,
garantindo reprodutibilidade e evitando hardcodes espalhados pelos notebooks.
"""

from pathlib import Path

# Raiz do projeto
BASE_PATH = Path(__file__).resolve().parents[1]

# Pastas principais
DATA_FOLDER = BASE_PATH / "data"
RAW_FOLDER = DATA_FOLDER / "raw"
PROCESSED_FOLDER = DATA_FOLDER / "processed"

MODELS_FOLDER = BASE_PATH / "models"
REPORTS_FOLDER = BASE_PATH / "reports"
PLOTS_FOLDER = REPORTS_FOLDER  / "plots"

# data/raw
RAW_DATA = RAW_FOLDER / "creditcard.zip"

# data/processed
PROCESSED_TRAIN = PROCESSED_FOLDER / "train.parquet"
PROCESSED_VALID = PROCESSED_FOLDER / "valid.parquet"
PROCESSED_TEST  = PROCESSED_FOLDER / "test.parquet"
PROCESSED_SPLIT_METADATA = PROCESSED_FOLDER / "split_metadata.json"

# reports
CHAMPION_METRICS_VALID = REPORTS_FOLDER / "champion_metrics_valid.json"
CHAMPION_METRICS_TEST  = REPORTS_FOLDER / "champion_metrics_test.json"