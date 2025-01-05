"""
Este módulo define o pipeline de machine learning e realiza o treinamento do modelo
usando os dados de treino. O modelo treinado é salvo no formato `.pkl` para uso futuro.
"""

import os
import sys
import pandas as pd
import joblib
from sklearn.pipeline import Pipeline
from lightgbm import LGBMClassifier
from src.config import TRAIN_DATA_PATH, MODEL_PATH
from src.features import (
    ColumnRenamer,
    ColumnDropper,
    DataProcessor,
    MedianImputer,
    TargetFeatureEncoder,
)

# Adicionar o diretório raiz do projeto ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))


def get_pipeline():
    """
    Define e retorna o pipeline de machine learning com as etapas de pré-processamento
    e o modelo LightGBM configurado com os melhores parâmetros.

    Returns:
        sklearn.pipeline.Pipeline: O pipeline completo com todas as etapas e o modelo.
    """
    params = {
        "subsample": 0.8,
        "reg_lambda": 0,
        "reg_alpha": 0,
        "num_leaves": 50,
        "n_estimators": 100,
        "min_child_weight": 0.1,
        "min_child_samples": 20,
        "max_depth": 10,
        "learning_rate": 0.01,
        "colsample_bytree": 0.6,
        "boosting_type": "dart",
    }

    model = LGBMClassifier(class_weight="balanced", random_state=1234, **params)

    return Pipeline(
        [
            ("renamer", ColumnRenamer()),
            ("dropper", ColumnDropper()),
            ("processor", DataProcessor()),
            ("imputer", MedianImputer()),
            (
                "target_encoder",
                TargetFeatureEncoder(
                    cols=[
                        "Possui mais de um sócio",
                        "Funcionários",
                        "PossuiContador",
                        "Faz conciliação bancária",
                        "Módulo Financeiro",
                        "Emissão NF",
                        "Integração Bancária",
                        "Módulo de Vendas",
                        "Relatórios",
                        "APIs de Integração",
                        "Contrato",
                        "Emite boletos.1",
                        "Tipo de pagamento",
                    ]
                ),
            ),
            ("classifier", model),
        ]
    )


def train_model(train_data=TRAIN_DATA_PATH, target_column="Churn"):
    """
    Realiza o treinamento do modelo com os dados fornecidos.

    Args:
        train_data (str): Caminho para o arquivo CSV contendo os dados de treino.
        target_column (str): Nome da coluna de destino (target).

    Returns:
        None: Salva o modelo treinado em um arquivo `.pkl`.
    """
    df_train = pd.read_csv(train_data)

    x_train = df_train.drop(columns=[target_column])
    y_train = df_train[target_column]

    pipeline = get_pipeline()

    pipeline.fit(x_train, y_train)
    print("Modelo treinado com sucesso")

    joblib.dump(pipeline, MODEL_PATH)
    print(f"Modelo salvo em {MODEL_PATH}")


if __name__ == "__main__":
    train_model()
