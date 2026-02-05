# Dicionário de dados

Fonte dos dados: [Kaggle](https://www.kaggle.com/mlg-ulb/creditcardfraud)

| Nome da coluna | Descrição             | Tipo de dado |
|----------------|-----------------------|--------------|
| `Time`         | Intervalo em segundos entre cada transação e a primeira transação da base | float     |
| `V1` - `V28`   | Componentes principais resultantes de transformação PCA | float   |
| `Amount`       | Valor monetário da transação | float         |
| `Class`        | Indica se a transação é legítima (0) ou fraudulenta (1) | int        |

## Observações sobre as variáveis

- As variáveis originais não são disponibilizadas por motivos de confidencialidade.
- As colunas `V1` a `V28` são resultado de uma transformação de Análise de Componentes Principais (PCA), aplicada para reduzir a dimensionalidade e preservar a maior parte da informação estatística.
- As componentes não possuem interpretação semântica direta, sendo analisadas exclusivamente sob a ótica estatística e operacional.