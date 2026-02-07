# FraudWatch

**Sistema de Priorização de Alertas de Fraude**

![Author](https://img.shields.io/badge/author-Jhonathan%20Domingues-lightgrey)
![License](https://img.shields.io/badge/license-MIT-blue)
![Status](https://img.shields.io/badge/status-V1.1%20completed-green)

![Python](https://img.shields.io/badge/python-3.12.5-blue?logo=python&logoColor=white)
![ML](https://img.shields.io/badge/ml-scikit--learn-orange?logo=scikitlearn&logoColor=white)
![Model](https://img.shields.io/badge/model-LightGBM-black)
![Model](https://img.shields.io/badge/model-XGBoost-black)
![Explainability](https://img.shields.io/badge/explainability-SHAP-teal)
![Data](https://img.shields.io/badge/data-Pandas%20%7C%20NumPy-blue)
![Viz](https://img.shields.io/badge/viz-Matplotlib%20%7C%20Seaborn-purple)

![FraudWatch](imagens/thumbnail.png)

---

## Visão Geral

A **FraudWatch** é uma Proof of Concept (POC) que demonstra a construção de um sistema antifraude baseado em Machine Learning, com foco em **decisão de negócio**, **governança mínima** e **avaliação honesta de desempenho**.

O projeto trata o modelo como um **motor de decisão**, e não como um fim em si mesmo, separando explicitamente:

- previsão (score),
- decisão (policy),
- e evolução do modelo ao longo do tempo.

A POC é estruturada em versões bem delimitadas. A **V1.1** entrega um MVP defensável e publicável, enquanto a **V2** é planejada como evolução do ciclo de vida do modelo.

Embora o dataset utilizado seja de fraude em cartão, a arquitetura e a lógica da FraudWatch são aplicáveis a outros domínios de **risco transacional**, como **Prevenção à Lavagem de Dinheiro (PLD/AML)** e **análise de risco de crédito**.  
O foco da POC está na geração de **scores de risco**, definição de **políticas de decisão** e avaliação de trade-offs operacionais — elementos centrais em sistemas regulatórios e de compliance.

---

## Problema de Negócio

Empresas que operam com grande volume de transações financeiras enfrentam desafios como:

- fraudes que passam despercebidas (*falsos negativos*);
- clientes legítimos bloqueados indevidamente (*falsos positivos*);
- limitação de capacidade humana para análise manual;
- forte desbalanceamento entre eventos legítimos e fraudulentos.

O **FraudWatch** busca endereçar esse cenário priorizando eventos com maior risco, permitindo que equipes concentrem esforços onde há maior impacto operacional.

---

## Escopo Atual da POC (V1.1)

No estágio atual, o projeto contempla:

- tratamento do dataset como **histórico de transações**;
- auditoria e análise exploratória dos dados;
- divisão **temporal** em conjuntos de treino, validação e teste;
- treinamento de modelo baseline (Logistic Regression);
- treinamento e seleção de modelo principal (LightGBM vs XGBoost);
- avaliação orientada a métricas relevantes para **decisão de risco**:
  - Recall,
  - Precision,
  - PR-AUC,
  - matriz de confusão;
- definição explícita de **política de decisão** (*approve / review / block*);
- análise de importância de features e explicabilidade (SHAP);
- persistência de artefatos (datasets processados, modelos e policy).

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
│   └── thumbnail.png
├── src/
│   ├── evaluation.py
│   ├── paths.py
│   └── utils.py
├── notebooks/
│   ├── 01-data_audit_eda.ipynb
│   ├── 02-train_baseline.ipynb
│   ├── 03-train_main_model.ipynb
│   └── 04-policy_decisioning.ipynb
├── models/
│   ├── baseline_logreg.pkl
│   └── champion_lightgbm.pkl
├── references/
│   └── 01_dicionario_de_dados.md
├── reports/
│   ├── metrics/      # métricas dos modelos (baseline e campeão, valid/test)
│   ├── policy/       # política de decisão e thresholds definidos
│   ├── analysis/     # análises de trade-off e comparações entre modelos
│   └── plots/        # visualizações (matriz de confusão, PR curves)
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

* **V1.1 — Modelo e decisão:** concluída
* **V2 — Simulação temporal, monitoramento de drift e retreino:** planejada

---

## Pipeline Atual

O pipeline implementado até o momento segue os seguintes passos:

1. Leitura e auditoria do histórico de transações
2. Análise exploratória com foco em sinais preditivos
3. Divisão temporal dos dados em treino, validação e teste
4. Treinamento e validação de modelos candidatos
5. Seleção do modelo campeão
6. Definição explícita de política de decisão baseada em score
7. Avaliação orientada a trade-offs operacionais
8. Persistência de modelos, métricas e política de decisão

Durante a execução da **V1.1**, o projeto gera artefatos intermediários e finais que documentam de forma estruturada as decisões técnicas e operacionais, incluindo:

* métricas de desempenho do modelo baseline e do modelo campeão (validação e teste);
* comparações entre modelos candidatos;
* análises de trade-off baseadas em matriz de custo;
* política de decisão persistida, com thresholds e regras explícitas;
* visualizações de suporte à análise, como matrizes de confusão e curvas precision–recall.

Esses artefatos são utilizados tanto para **validação técnica** quanto para **documentação e rastreabilidade do processo decisório**, reforçando a governança mínima proposta pela POC.

---

## Próximos Passos Planejados (V2)

As próximas etapas previstas para a evolução da POC incluem:

* validação e refinamento das políticas de decisão definidas;
* simulação temporal do fluxo de decisões em dados históricos;
* monitoramento de drift e estratégia de retreino;
* geração automatizada de relatórios de performance e decisão.

---

## Licença

Este projeto está licenciado sob os termos da **MIT License**. Consulte o arquivo `LICENSE` para mais detalhes.

---

## Disclaimer

O **FraudWatch** é uma Proof of Concept desenvolvida com fins demonstrativos, voltada à documentação e avaliação de abordagens de detecção e priorização de riscos em transações financeiras.

Os dados utilizados são públicos e amplamente difundidos para fins de pesquisa, não contendo informações pessoais, sensíveis ou sigilosas.
Este projeto **não deve ser utilizado em ambientes produtivos**.

---

## Onde me encontrar

[![Website](https://img.shields.io/badge/🌐%20Website-Portfólio-black)](https://jhonathan.me)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Perfil-blue?logo=linkedin&logoColor=white)](https://www.linkedin.com/in/jhonathandomingues)
[![Email](https://img.shields.io/badge/Email-Contato-success?logo=minutemailer&logoColor=white)](mailto:hello@jhonathan.me)