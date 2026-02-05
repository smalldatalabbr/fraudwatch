# FraudWatch

**Sistema de Priorização de Alertas de Fraude**

![FraudWatch](imagens/thumbnail.png)

## Visão Geral

A **FraudWatch** é uma Proof of Concept (POC) que demonstra a construção de um sistema antifraude baseado em Machine Learning, com foco em **decisão de negócio**, **governança mínima** e **avaliação honesta de desempenho**.

O projeto trata o modelo como um **motor de decisão**, e não como um fim em si mesmo, separando explicitamente:

- previsão (score),
- decisão (policy),
- e evolução do modelo ao longo do tempo.

A POC é estruturada em versões bem delimitadas. A **V1** entrega um MVP defensável e publicável, enquanto a **V2** é planejada como evolução do ciclo de vida do modelo.

---

## Problema de Negócio

Empresas que operam com grande volume de transações financeiras enfrentam desafios como:

* fraudes que passam despercebidas (*falsos negativos*);
* clientes legítimos bloqueados indevidamente (*falsos positivos*);
* limitação de capacidade humana para análise manual;
* forte desbalanceamento entre eventos legítimos e fraudulentos.

O **FraudWatch** busca endereçar esse cenário priorizando eventos com maior risco, permitindo que equipes concentrem esforços onde há maior impacto operacional.

---

## Escopo Atual da POC

No estágio atual, o projeto contempla:

* tratamento do dataset como **histórico de transações**;
* auditoria e análise exploratória dos dados;
* divisão **temporal** em conjuntos de treino, validação e teste;
* treinamento de modelo baseline (Logistic Regression);
* treinamento de modelo principal (LightGBM ou equivalente);
* avaliação orientada a métricas relevantes para fraude:

  * Recall,
  * Precision,
  * PR-AUC,
  * matriz de confusão;
* análise de importância de features;
* persistência de artefatos (datasets processados e modelos).

---

## Fonte dos Dados

O projeto utiliza o dataset público [**Credit Card Fraud Detection**](https://www.kaggle.com/c/ieee-fraud-detection/data), disponibilizado originalmente no **Kaggle**.

A base contém transações anonimizadas e componentes transformados por PCA, sendo amplamente utilizada como benchmark técnico para experimentos e estudos em sistemas antifraude.

---

## Estrutura do Projeto

```
fraudwatch/
│
├── data/
│   ├── raw/
│   └── processed/
├── imagens/
│   ├── thumbnail.png
├── src/
│       ├── paths.py
│       └── utils.py
├── notebooks/
│   ├── 01-data_audit_eda.ipynb
│   ├── 02-train_baseline.ipynb
│   └── 03-train_main_model.ipynb
│
├── models/
│   └── fraudwatch_model.joblib
│
├── references/
│   └── 01_dicionario_de_dados.md
│
├── reports/
│   ├── baseline_metrics.json
│   ├── main_model_metrics.json
│   └── feature_importance.csv
│
├── requirements.txt
└── README.md
```

---

## Como Rodar o Projeto

Criação do ambiente virtual e instalação das dependências:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

```

---

## Status

* **V1 — Modelo e decisão:** em execução
* **V2 — Simulação, drift e retreino** planejada

---

## Pipeline Atual

O pipeline implementado até o momento segue os seguintes passos:

1. Leitura e auditoria do histórico de transações
2. Análise exploratória com foco em sinais preditivos
3. Divisão temporal dos dados
4. Treinamento e validação de modelos
5. Avaliação orientada a métricas operacionais
6. Persistência de modelos e artefatos

---

## Próximos Passos Planejados

As próximas etapas previstas para a evolução da POC incluem:

* definição de políticas de decisão baseadas em score de risco;
* implementação de faixas de risco (baixo / médio / alto);
* geração de alertas priorizados a partir do conjunto de teste;
* consolidação de um pipeline de execução local para simular um ambiente operacional.

---

## Licença

Este projeto está licenciado sob os termos da **MIT License**. Consulte o arquivo `LICENSE` para mais detalhes.

---

## Disclaimer

O **FraudWatch** é uma Proof of Concept desenvolvida com fins demonstrativos, voltada à documentação e avaliação de abordagens de detecção e priorização de fraudes em transações financeiras.

Os dados utilizados são públicos e amplamente difundidos para fins de pesquisa, não contendo informações pessoais, sensíveis ou sigilosas.
Este projeto **não deve ser utilizado em ambientes produtivos**.


---

## Contato

**Jhonathan Domingues**

🌐 [Portifólio](https://jhonathan.me) | 💼 [LinkedIn](https://www.linkedin.com/in/jhonathandomingues)