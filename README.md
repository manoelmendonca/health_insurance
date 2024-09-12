<h1 align="center">
ESTRATÉGIA DE VENDA-CRUZADA DE SEGUROS<br>
</h1>

<h6>- <a href="README-en.md">ENGLISH VERSION</a></h6>

![banner](img/Seguro_automovel_01.png)


# 1. INTRODUÇÃO

O que é este trabalho? O desafio é criar um método inteligente para selecionar os clientes mais propensos a comprar um novo produto de uma empresa seguradora. Trata-se portanto da análise de um caso de negócio, com o foco em aumentar a receita da empresa, bem assim atender as principais questões da equipe de negócio.

Conforme será apresentado ao longo do trabalho, com o uso do presente projeto foi possível aumentar o desempenho da campanha de vendas em aproximadamente 182%, com aumento estimado de mais de 200% no faturamento, representando incremento absoluto no faturamento da ordem de $ 158 milhões.

Este projeto se baseia em um caso fictício, e faz uso de uma base de dados do [Kaggle](https://www.kaggle.com/datasets/anmolkumar/health-insurance-cross-sell-prediction). Ressalte-se, no entanto, que o FOCO PRINCIPAL não é apenas a criação de uma solução de <i>machine learning</i> para uma competição de ciência de dados, mas a análise do negócio como um todo, buscando compreender os aspectos que impactam no desempenho, com vistas ao aumento da receita e da lucratividade da empresa.


# 2. A EMPRESA E O PRODUTO

Neste contexto fictício, a empresa <b>Insurance All</b> costuma fornecer seguro de saúde para seus clientes, estando atualmente sendo analisada pelo seu time de produtos a possibilidade de iniciar uma nova campanha de marketing para oferecer aos segurados uma modalidade diferente, qual seja, o seguro de automóveis.

O contrato de seguro tem definição no art. 757 do Código Civil Brasileiro, sendo o contrato por meio do qual uma empresa – a seguradora – se compromete a garantir determinado interesse de seu cliente – o segurado – diante do risco de ocorrência de sinistro, tendo como retribuição o pagamento de um prêmio.

Finalmente, cabe esclarecer que a **venda-cruzada** consiste simplesmente na sugestão de um produto para compra, a partir da identificação do interesse da pessoa na compra de outro produto. Tal prática é permitida por lei. Essa prática lícita não deve ser confundida com a **venda-casada**, isto é, a imposição por parte do vendedor da obrigatoriedade de compra de um produto para permitir que o comprador adquira o outro no qual está de fato interessado. Esta última é prática proibida no Brasil por força do disposto no artigo 39, parágrafo primeiro, da Lei de Defesa do Consumidor (Lei nº 8078/1990).


# 3. O PROBLEMA DE NEGÓCIO

Visando a melhorar os resultados da nova campanha de marketing, a equipe de ciência de dados foi encarregada de construir um modelo de <i>machine learning</i> para predizer se o cliente estaria ou não interessado no seguro de automóvel. Como resultado deste modelo, o time de vendas espera conseguir priorizar as pessoas com o maior interesse no novo produto e assim, otimizar a campanha, realizando apenas contatos com os 20 mil clientes identificados como os mais propensos a realizar a compra.

No caso específico do seguro automotivo da empresa <b>Insurance All</b>, foi realizada pesquisa de mercado com cerca de 381 mil clientes quanto ao interesse em aderir a um novo produto, formando-se assim uma base de dados usada no presente ensaio de machine learning.

O time de produtos possui informação sobre outros 127 mil novos clientes, passíveis de receberem a oferta do novo produto por meio de ligações telefônicas. Esse grupo novos clientes é formado por pessoas que não responderam à citada pesquisa de interesse.

Existe no entanto uma RESTRIÇÃO: o time de vendas tem capacidade para telefonar e enviar prospectos para somente <b>20 mil pessoas</b> no período da campanha, sendo portanto crucial, dentre os 127 mil potenciais clientes, selecionar os 20 mil mais propensos a aceitarem a oferta.


# 4. PLANEJAMENTO DA SOLUÇÃO

## 4.1. Produto Final

Conforme descrito no problema de negócio, o objetivo é desenvolver um modelo de ML para avaliar o interesse dos clientes em adquirir seguro de automóvel. Assim, a solução apresentada compreende a entrega dos seguintes resultados:

1. Resultado nº 1 - Insights relacionados ao negócio de seguro automotivo, com base nos dados disponíveis.
2. Resultado nº 2 - Relatório respondendo às seguintes três questões práticas sobre a campanha de vendas: <b>(2.1)</b> dentre as 20 mil ligações realizadas pelo time de vendas, qual deverá ser a porcentagem de clientes interessados em adquirir um seguro de automóvel; <b>(2.2)</b> caso a capacidade do time de vendas seja aumentada para 40 mil ligações, qual a porcentagem de clientes interessados em adquirir o produto; e <b>(2.3)</b> quantas ligações o time de vendas precisa fazer para contactar 80% dos clientes interessados em adquirir um seguro de automóvel?
3. Resultado nº 3 - Planilha excel inteligente, para prospecção de clientes, capaz de aplicar o modelo de <i>machine learning</i> resultante aos dados relativos a futuros clientes.

## 4.2. Estratégia de Solução

O trabalho foi realizado seguindo o método CRISP-DM (ou "<i>Cross Industry Standard Process for Data Mining</i>"), uma abordagem cíclica capaz de aprimorar a qualidade e agilizar a entrega de resultados em projetos de Ciência de Dados. O método pode ser resumido no seguinte conjunto de etapas:

1. Entendimento do negócio
2. Coleta, tratamento e modelagem dos dados
3. Algoritmos de <i>Machine Learning</i>
4. Avaliação dos resultados
5. Entrada em produção.

![banner](img/MetodoCrispDM.png)


# 5. OS DADOS DISPONÍVEIS

Os dados estão disponíveis no arquivo TRAIN.CSV, num conjunto de 381.109 registros, contendo as seguintes colunas:

<table align="center">
  <tr>
    <th align="center">ATRIBUTO</th>
    <th>DESCRIÇÃO E OBSERVAÇÕES</th>
  </tr>
  <tr>
    <td align="center">Id</td>
    <td>Identificador único para cada cliente, num total de 381.109 registros.</td>
  </tr>
  <tr>
    <td align="center">Gender</td>
    <td>Gênero do cliente (Male/Female)</td>
  </tr>
  <tr>
    <td align="center">Age</td>
    <td>Idade do cliente, variando entre 20 e 85 anos.</td>
  </tr>
  <tr>
    <td align="center">Driving_License</td>
    <td>Indicador se o cliente possui carteira de motorista (1: Sim, 0: Não). Tem-se que 99,79% dos clientes possuem licença.</td>
  </tr>
  <tr>
    <td align="center">Region_Code</td>
    <td>Código da região onde o cliente reside. Constam 53 regiões, sem maiores informações geográficas ou sociais.</td>
  </tr>
  <tr>
    <td align="center">Previously_Insured</td>
    <td>Indicador se o cliente já possui seguro anterior (1: Sim, 0: Não). São 54,18% já anteriormente segurados.</td>
  </tr>
  <tr>
    <td align="center">Vehicle_Age</td>
    <td>Idade do veículo, nas categorias: "&lt; 1 Year" (43,24%), "1-2 Year" (52,56%), e "&gt; 2 Years" (4,20%).</td>
  </tr>
  <tr>
    <td align="center">Vehicle_Damage</td>
    <td>Indicador se o veículo foi danificado anteriormente, sendo 50,49% YES e os demais 49,51% NO.</td>
  </tr>
  <tr>
    <td align="center">Annual_Premium</td>
    <td>Prêmio anual pago pelo segurado (entre $2.630 e $540.165).</td>
  </tr>
  <tr>
    <td align="center">Policy_Sales_Channel</td>
    <td>Canal de vendas por meio do qual a apólice foi adquirida. Informação anonimizada, podendo ser referente a carta, telefone, contato pessoal, etc. Na base de dados constam 155 canais distintos, sem maiores informações indicativas de seu significado.</td>
  </tr>
  <tr>
    <td align="center">Vintage</td>
    <td>Número de dias desde que o cliente foi associado à cia seguradora (entre 10 e 299 dias).</td>
  </tr>
  <tr>
    <td align="center">Response</td>
    <td>Resposta do cliente quanto à aceitação do novo produto (1: Sim, 0: Não). A informação de saída binária é típica de problemas de classificação. Além disso, há apenas 12,26% de respostas SIM, indicando classes fortemente desbalanceadas.</td>
  </tr>
</table>


(Fonte: [Kaggle](https://www.kaggle.com/datasets/anmolkumar/health-insurance-cross-sell-prediction), Health Insurance Cross Sell Prediction)

Há ainda disponível o arquivo TEST.CSV, com formato semelhante ao apresentado acima, mas sem o atributo "Response". Por falta deste atributo, esse arquivo não tem utilidade na etapa de elaboração e teste dos modelos de <i>machine learning</i>, sendo possível utilizá-lo ao final apenas como informação de teste para a planilha excel de prospecção de clientes.


# 6. PREPARAÇÃO DOS DADOS

Na inspeção inicial não foi identificada a ocorrência de dados faltantes (NaN). Por outro lado, foram realizadas conversões de alguns atributos, criação de alguns outros atributos, e realizados procedimentos de codificação ("<i>encodings</i>") de outros (seções 3.1, 6.2 e 6.3 do código). Detalhes a seguir.

## 6.1. Conversões simples de variáveis categóricas

Tratam-se aqui de conversões baseadas apenas na informação contida no próprio registro a ser alterado, não gerando possibilidade de ocorrência de vazamento de dados (<i>data leakage</i>).

- A variável "vehicle_damage" teve seu conteúdo de texto "Yes" & "No" convertido para os números 1 & 0.
- A variável "vehicle_age" teve suas categorias renomeadas de ""> 2 Years" para "over_2_years", de "1-2 Years" para "between_1_2_years e de "< 1 Year" para "bellow_1_year".
- A variável "annual_premium" foi dividida em três faixas, criando-se as novas variáveis "annual_premium_f1", "annual_premium_f2" e "annual_premium_f3".


## 6.2. Distribuição bimodal da variável "age"

Tanto na análise descritiva inicial (seção 1.3.2 do código) quanto na análise exploratória (EDA, seção 5.1.1 do código) foi observado que distribuição da variável "age" indicava a existência de dois modos, centrados aos 23 anos e 43 anos. Assim, foram acrescentadas duas novas variáveis para representar a similaridade entre a idade do cliente e cada um daqueles modos. A similaridade foi computada utilizando RBF - <i>radial basis function</i> (Géron<sup>2</sup>, pag. 77-78) para criação das variáveis "age_rbf_23" e "age_rbf_43". O código e o resultado são ilustrados a seguir.

```python
centers = [23, 43]

rbf_23 = rbf_kernel(df3[['age']], [[centers[0]]], gamma=0.030 )
rbf_43 = rbf_kernel(df3[['age']], [[centers[1]]], gamma=0.015 )

df3['age_rbf_23'] = rbf_23
df3['age_rbf_43'] = rbf_43
```

Os valores de gamma podem ser obtidos por otimização, no entanto, no presente caso, esses valores foram obtidos por tentativa e erro usando o gráfico.

![banner](img/variavel_age_rbf.png)

O procedimento trouxe bom resultado, visto que, na etapa de teste de importância das variáveis (seção 7 do código), "age_rbf_23" e "age_rbf_43" mostraram-se especialmente importantes. Sobre isso, veja nossa [postagem](https://www.linkedin.com/posts/manoelmendonca-eng-adv_datascience-machinelearning-radialbasisfunction-activity-7234892553542672385-gukQ?utm_source=share&utm_medium=member_desktop). À epoca da postagem, parecia apropriado utilizar apenas a variável "age_rbf_43". Com a evolução do projeto, o resultado foi dado pela utilização de ambas.

No caso dessas variáveis criadas usando RBF, por fazerem uso de informação de toda a distribuição, foi necessário cuidar para a não ocorrência de <i>data leakage</i>, fazendo seu ajuste nos dados de treino e aplicando o resultado nos conjuntos de validação e teste. Essa providência foi embutida em um objeto criado para essa finalidade (classe DataFitAndTransform, seção 6.1 do código) e usado nos testes de validação cruzada e no teste final do modelo.


## 6.3. Codificação em frequencia da variável "policy_sales_channel"

Trata-se de variável categórica com 155 classes, formadas por dados anonimizados e convertidos em números, sem maiores explicações. Provavelmente, as classes mais importantes entre essas 155 terão ocorrência mais frequente, daí a utilização de <i>frequency encoding</i> para a criação da variável "policy_sales_channel_importance".

```python
# compute KPI
# Policy Sales Channel Importance = (N# of regs by channel) / (Total N# of regs)
aux = df3.loc[:, ['policy_sales_channel', 'id'] ].groupby('policy_sales_channel').count().reset_index()
maxval = aux['id'].max()
aux['policy_sales_channel_importance'] = aux['id'] / maxval
aux = aux.drop(columns=['id'])
# include it in df3
df3 = pd.merge( df3, aux, on='policy_sales_channel', how="left" )
```

Esse processamento foi incluído na nossa classe DataFitAndTransform (seção 6.1 do código) para evitar <i>data leakage</i>.


## 6.4. Codificação das demais variáveis

As variáveis "gender", "region_code" e "vehicle_age" são do tipo categóricas e foram preparadas por meio de <i>encoders</i> (seção 6.1 do código) para sua posterior utilização nos modelos de <i>machine learning</i>.

Às variáveis categóricas "gender" e "vehicle_age" foi aplicada a <i>one hot encoding</i> para converter suas classes em colunas binárias.

Já a variável "region_code" recebeu a <i>leave one out encoding</i>, que é uma técnica semelhante à <i>target encoding</i>, mas que busca reduzir o efeito de <i>overfitting</i> ao excluir dos cálculos o valor-alvo da linha corrente (Lewingson<sup>3</sup>, pag. 555-556).

A variável numérica "annual_premium" e suas derivadas "annual_premium_f1", "annual_premium_f2" e "annual_premium_f3" foram escalonadas utilizando a função StandardScaler(), de modo a apresentarem média zero e variância unitária. Posteriormente, decidiu-se por não utilizar os registros referentes a "annual_premium_f3", por representarem menos de 1% da base e por referirem-se a valores extremamente elevados de prêmios.

As variáveis "age" e "vintage" foram convertidas com MaxMinScaler(), de modo a ficarem limitadas aos limites entre zero e 1, mas sem mudar o formato de suas distribuições originais.


## 6.5. Importância relativa das variáveis

Neste quesito procuramos testar muitas técnicas (seção 7 do código). Algumas não trouxeram benefício e foram deletadas, como foi o caso de <i>Foward Feature Selection</i> e <i>Backward Feature Selection</i> (Lewingson<sup>3</sup>, pag. 620). Outras foram muito interessantes.

Usamos o clássico Boruta em duas versões, uma vez usando como estimador o ExtraTrees e de outra vez usando o LightGBM. Ambos os casos apontaram para o descarte de "driving_license", sendo que com LightGBM foram indicadas outras 3 para descarte.

Outro clássico é utilizar o parâmetro "feature_importances_" dos algoritmos em árvore (Géron<sup>2</sup>, pag. 221). Assim, utilizamos essa técnica também em duas versões, com ExtraTrees e com LightGBM. O resultado foi curioso já que algumas variáveis receberam classificações totalmente divergentes, conforme ressaltado na figura abaixo:

![banner](img/feature_importance_2trees.png)

Na verdade, é compreensível que nem todas as variáveis mais apropriadas em um algoritmo venham a ser igualmente apropriadas nos demais algoritmos. Assim, na falta de uma indicação conclusiva para decidir quanto à importância das variáveis para o algoritmo escolhido, partimos para a força bruta, e codificamos um <i>loop</i> para exclusão gradual de variáveis (seção 7.5 do código), na forma:

```python
for i in range( len( cols_selected_boruta ) ):
    selected_features = cols_selected_boruta[:i] + cols_selected_boruta[i+1:]
    ...
```

Esse procedimento de exclusão gradual (ou "<i>Recursive Feature Elimination</i>") foi aplicado repetidamente ao modelo de melhor desempenho - LogisticRegression - de modo a aprimorá-lo pela retirada de variáveis que não contribuiam para o resultado, ou mesmo que o pioravam. Desse modo, foram excluídas as variáveis "vehicle_age_over_2_years" e "vehicle_age_between_1_2_years", levando a melhoria significativa dos indicadores <i>Precision</i>, <i>Recall</i> e F1. Sobre esse assunto, veja nossa [postagem](https://www.linkedin.com/posts/manoelmendonca-eng-adv_datascience-machinelearning-featureselection-activity-7236360978865545219--TO_?utm_source=share&utm_medium=member_desktop).


## 6.6. Fluxo para transformação e ajuste de dados (*pipeline*)

Durante o desenvolvimento do projeto, a criação de variáveis, sua transformação e codificação foi se avolumando. Ao mesmo tempo, todo esse conjunto de transformações precisava ser (i) realizado sempre numa mesma ordem e (ii) aplicado em diferentes fases do processamento. Por exemplo, as transformações precisavam ser aplicadas tanto para manipulação dos dados de teste na avaliação final do modelo, quanto para manipular os *folds* na etapa de validação cruzada, de modo a evitar vazamento de dados em quaisquer dessas etapas.

Diante desse panorama, decidimos encapsular todos esses procedimentos numa classe, denominada **DataFitAndTransform** (seção 6.1 do código). Em bom tecniquês: um pipeline. O foco era garantir a consistência das transformações aplicadas aos dados, de modo a que os dados de entrada fossem devidamente transformados e padronizados antes de serem utilizados nos vários modelos de *machine learning*.

A classe tem os seguintes métodos principais:

```python
class DataFitAndTransform:
    def __init__(self):
        ...
    def DataFitting(self, in_df, y_train):
        ...
    def DataTransforming(self, in_df):
        ...
    def get_parameters(self):
        ...
```

Na estrutura acima, o método `__init__` define os atributos da classe, reunindo assim os diversos objetos de transformação e escalonamento, como `StandardScaler`, `MinMaxScaler`, `OneHotEncoder`, `LeaveOneOutEncoder`, etc.

O método `DataFitting()` faz o ajuste dos escalonadores e codificadores aos dados de treino e então aplica essas transformações a esse conjunto de dados.

O método `DataTransforming()` faz uso dos objetos de transformação e escalonamento criados no método acima e os aplica aos dados de teste (e também aos de validação, conforme o caso). Desse modo, garante-se a consistência com o procedimento aplicado aos dados de treino. 

O método `get_parameters()` retorna um dicionário contendo todos os escalonadores e encoders ajustados. No presente projeto, foi utilizado para verificação do processmento (debug) e para criação dos arquivos pickle.

Por último, deixo uma observação de ordem prática: os métodos `DataFitting()` e `DataTransforming()` devem manter ordem semelhante de transformações. Durante o desenvolvimento, vários erros de processamento ocorreram em razão da não observância desse aspecto.


# 7. TREINAMENTO DOS ALGORITMOS DE <i>MACHINE LEARNING</i>

O trabalho de seleção e construção do modelo de <i>machine learning</i> foi dividido nas seguintes etapas:
1. busca pelo algoritmo classificação capaz de apresentar o melhor desempenho, entre os seguintes: Logistic Regression, XGBoost, KNN, Random Forest, Extra Trees e LightGBM.
2. utilização do algoritmo eleito na etapa anterior e otimização dos seus hiperparâmetros para se chegar ao modelo definitivo.
3. avaliação em termos de impacto no negócio

Seguem alguns aspectos relativos ao trabalho de busca do algoritmo adequado.


## 7.1. Divisão da base de dados em treino, validação e teste

A base de dados disponível, contendo 381.109 registros, foi dividida em três conjuntos (seção 6.2 do código):

- base de teste, com 127024 registros, de modo a reproduzir a situação descrita pelo cliente.
- base de treino, com 201439 registros, representando 80% dos dados restantes.
- base de validação, com 50817 registros, representando 20% dos dados restantes.

A base de teste permaneceu reservada para uso na avaliação final do algoritmo de ML resultante da presente pesquisa (seção 10 do código). Já as bases de treino e validação foram utilizadas para validação direta dos algoritmos candidatos (seção 8.1 do código). Posteriormente, as duas bases foram utilizadas em conjunto (ou seja, com 252256 registros) para fins de validação cruzada dos referidos algoritmos (seção 8.2 do código).


## 7.2. Tratamento de classes desbalanceadas

A avaliação preliminar da variável alvo "response" indicou tratar-se de um caso de classificação na presença de classes desbalanceadas, estando a classe de interesse presente em apenas 12,26% dos registros (seção 1.3.4 do código).

![banner](img/inbalanced_data.png)

A existência de desequilíbrio entre as classes resulta na redução do desempenho dos modelos de ML, isso porque os modelos pressupõem o equilíbrio e acabam valorando como mais importante a classe mais numerosa, levando a resultado indesejado na otimização do modelo.

Para lidar com dados desbalanceados há diversas técnicas que melhoram o desempenho dos modelos de ML (ver Lewinson<sup>3</sup>, pg. 562-572). Para o presente trabalho, foi aplicada a técnica híbrida combinando SMOTE (ou "<i>Synthetic Minority Over-sampling Technique</i>") e Tomek Links (seção 6.3 do código). Em resumo, SMOTE gera novas instâncias sintéticas da classe minoritária, enquanto Tomek ajuda a delinear as fronteiras entre as classes ao remover instâncias da classe majoritária que estejam mais próximas das instâncias da classe minoritária.


## 7.3. Indicadores de desempenho - Precision & Recall

Os indicadores <i>Precision</i> e <i>Recall</i> são voltados especificamente para os casos de sistemas de classificação binária na presença de classes desbalanceadas, sendo, portanto, os indicadores ideais para o presente projeto (juntamente com F1).

Em resumo, na base de dados deste projeto, 12.26% dos registros se referem à classe-1, a saber, as pessoas interessadas na compra do novo seguro automotivo. Por meio de técnicas de ciência de dados, cria-se uma máquina para prever quais casos pertencem à classe-1. Na prática, a máquina descobre alguns casos corretamente (grupo TP na figura), mas comete dois tipos de erros, já que diz serem da classe-1 alguns casos da classe-0 (grupo FP) e diz serem da classe-0 alguns casos da classe-1 (grupo FN).

A partir do universo de registros realmente pertencentes à classe-1 (TP + FN) é possível calcular o percentual de instâncias da classe-1 efetivamente descobertas (ou recuperadas) pela máquina, sendo esse o indicador <i>Recall</i>.

De modo semelhante, do conjunto de instâncias classificadas pela máquina como da classe-1 (TP + FP) é possível calcular quão precisa foi a máquina, sendo esse o indicador <i>Precision</i>.

Sobre o assunto, preparamos duas postagens: [essa](https://www.linkedin.com/posts/manoelmendonca-eng-adv_precision-recall-activity-7233824260442476544-szPD?utm_source=share&utm_medium=member_desktop) e [essa outra](https://www.linkedin.com/posts/manoelmendonca-eng-adv_datascience-machinelearning-precision-activity-7235632443515392001-DwBK?utm_source=share&utm_medium=member_desktop).


<table align="center">
<tr><td>
<img src="img/precision_recall.png" align="center">
</td></tr>
</table>

Fonte: Grigorev<sup>4</sup>, pg. 128.


## 7.4. Desempenho dos algoritmos testados

Para avaliação dos modelos e escolha do mais adequado, as bases de treino e validação foram utilizadas para validação direta dos algoritmos candidatos (seção 8.1 do código). Os números são apresentados na tabela abaixo e na figura mais abaixo.

<table align="center">
  <tr>
    <th align="center">Model</th>
    <th align="center">Precision</th>
    <th align="center">Recall</th>
    <th align="center">F1</th>
    <th align="center">TP</th>
  </tr>
  <tr>
    <td align="center">Logistic Reg.</td>
    <td align="center">27.55%</td>
    <td align="center">92.03%</td>
    <td align="center">42.41%</td>
    <td align="center">5762</td>
  </tr>
  <tr>
    <td align="center">XGBoost</td>
    <td align="center">28.66%</td>
    <td align="center">69.38%</td>
    <td align="center">40.57%</td>
    <td align="center">4344</td>
  </tr>
  <tr>
    <td align="center">KNN</td>
    <td align="center">34.30%</td>
    <td align="center">50.93%</td>
    <td align="center">41.00%</td>
    <td align="center">3189</td>
  </tr>
  <tr>
    <td align="center">ExtraTrees</td>
    <td align="center">33.55%</td>
    <td align="center">13.34%</td>
    <td align="center">19.09%</td>
    <td align="center">835</td>
  </tr>
  <tr>
    <td align="center">LightGBM</td>
    <td align="center">24.21%</td>
    <td align="center">10.05%</td>
    <td align="center">14.20%</td>
    <td align="center">629</td>
  </tr>
  <tr>
    <td align="center">Random Forest</td>
    <td align="center">34.22%</td>
    <td align="center">9.82%</td>
    <td align="center">15.26%</td>
    <td align="center">615</td>
  </tr>
</table>


Para confirmação do desempenho avaliado pelo procedimento acima, as bases de treino e validação foram utilizadas em conjunto para fins de validação cruzada dos referidos algoritmos (seção 8.2 do código). A tabela traz os resultados, com média e desvio padrão.

<table align="center">
  <tr>
    <th align="center">Model</th>
    <th align="center">Precision</th>
    <th align="center">Recall</th>
    <th align="center">F1</th>
    <th align="center">TP</th>
  </tr>
  <tr>
    <td align="center">Logistic Reg.</td>
    <td align="center">26.93% ± 0.2%</td>
    <td align="center">91.22% ± 0.3%</td>
    <td align="center">41.58% ± 0.3%</td>
    <td align="center">4469</td>
  </tr>
  <tr>
    <td align="center">XGBoost</td>
    <td align="center">27.94% ± 0.4%</td>
    <td align="center">71.65% ± 0.5%</td>
    <td align="center">40.20% ± 0.4%</td>
    <td align="center">3510</td>
  </tr>
  <tr>
    <td align="center">KNN</td>
    <td align="center">32.66% ± 0.4%</td>
    <td align="center">52.07% ± 0.6%</td>
    <td align="center">40.14% ± 0.4%</td>
    <td align="center">2551</td>
  </tr>
  <tr>
    <td align="center">LightGBM</td>
    <td align="center">22.72% ± 1.3%</td>
    <td align="center">17.95% ± 1.9%</td>
    <td align="center">19.98% ± 1.2%</td>
    <td align="center">879</td>
  </tr>
  <tr>
    <td align="center">ExtraTrees</td>
    <td align="center">32.99% ± 0.7%</td>
    <td align="center">13.35% ± 0.2%</td>
    <td align="center">19.00% ± 0.3%</td>
    <td align="center">654</td>
  </tr>
  <tr>
    <td align="center">Random Forest</td>
    <td align="center">33.67% ± 1.1%</td>
    <td align="center">9.94% ± 1.5%</td>
    <td align="center">15.30% ± 1.9%</td>
    <td align="center">487</td>
  </tr>
</table>


Os desempenhos dos modelos de ML após teste e validação podem ser também avaliados por meio da comparação dos gráficos de ganho cumulativo.

<table align="center">
<tr><td>
<img src="img/ml_comparison.png" align="center">
</td></tr>
</table>

CONCLUSÃO: em razão dos resultados dos testes acima, o algoritmo LOGISTIC REGRESSION foi a nossa escolha para uso no presente trabalho, haja vista ter apresentado a maior quantidade de casos de <i>True Positive</i> (TP), o que se reflete nos bons resultados dos indicadores F1, <i>Precision</i> e, notadamente, <i>Recall</i>.


# 8. RESULTADO-I: PRINCIPAIS <i>INSIGHTS</i> DE NEGÓCIO

Conforme apresentado no tópico 4.1, o produto final inclui a elaboração de insights obtidos a partir da análise dos dados disponíveis. Trata-se de aspecto muito importante, por dar base para discussão de novas estratégias de vendas. 

Em se tratando de analisar o mercado de seguros, é importante investigar quais são os eventos que interferem no desempenho do negócio. No mapa mental abaixo são apresentados alguns fenômenos capazes de alterar a demanda. Tem-se:

- Características do cliente: gênero, idade, percepção de risco, local de residência, nível de educação, entre outros.
- Características do veículo: idade, preço de mercado, tecnologia embarcada.
- Características do contrato de seguro: valor do prêmio, campanhas de marketing, competição de mercado.
- Políticas governamentais: incentivos fiscais.
- Fatores externos: percentual de acidentes automotivos, desastres naturais.

![banner](img/MindMapHypothesis_Insurance.png)

No caso do presente projeto, com base na investigação dos dados disponíveis (tópico 5.3 do código), têm-se os seguintes insights mais interessantes:

## Insight nº 1: O gênero do consumidor não tem influência no interesse por seguro.
Hipótese <b>FALSA</B>: Os dados mostram haver um percentual maior de aceitação para o contrato de seguro de automóvel por parte da população masculina, de 13,84% dos homens, contra apenas 10,39% das mulheres. Além disso, a população masculina é um pouco maior (206 mil homens ao lado de 175 mil mulheres). Combinando esses números, tem-se um total de 28.522 homens interessados em seguros, e apenas 18.184 mulheres interessadas.

Conclui-se assim que, contrariamente à hipótese inicial, o gênero da clientela tem algum impacto na demanda por seguros.

## Insight nº 2: O interesse por contratos de seguro aumenta com o aumento da idade
Hipótese <b>VERDADEIRA</B>: Os números indicam que no grupo de pessoas entre 21 e 25 anos, apenas 3,7% delas estão interessadas em contratar seguro de automóvel. Por outro lado, 27,2% das pessoas entre 39 e 47 anos demonstraram interesse na compra do seguro.

Essas relações de interesse em função da idade se refletem nas distribuições da variável "age" versus "response", conforme mostra o gráfico.

![banner](img/age_and_response.png)

Conclui-se assim que, de fato, o interesse por contratos de seguro aumenta com o passar da idade.

## Insight nº 3: As pessoas já possuidoras de contrato de seguros junto a outras companhias tendem a ter menor propensão a se tornarem nossas clientes.
Hipótese <b>VERDADEIRA</B>: Na base de dados disponível, tem-se que 45,8% das pessoas já possuiam contrato de seguro veicular, e 99,91% dessas pessoas responderam negativamente à pesquisa de interesse na oferta de seguro automotivo.

Por outro lado, dos demais 54,2% de pessoas que não possuem seguro veicular, tem-se que 22,55% delas têm interesse no novo produto.

<table align="center">
    <tr>
        <td colspan=2 rowspan=2 align="center"><b>%</b></td>
        <td colspan=2 align="center"><b>response</b></td>
    </tr>
    <tr>
        <td align="center"><b>0</b></td>
        <td align="center"><b>1</b></td>
    </tr>
    <tr>
        <td rowspan=2><b>previously_insured</b></td>
        <td><b>0</b></td>
        <td align="center">77,45%</td>
        <td align="center">22,55%</td>
    </tr>
    <tr>
        <td><b>1</b></td>
        <td align="center">99,91%</td>
        <td align="center">0,09%</td>
    </tr>
</table>


## Insight nº 4: Quanto mais novo o veículo, maior o interesse pelo nosso seguro automotivo.
Hipótese <b>FALSA</B>: Os dados mostram que os clientes com carros mais novos estão menos inclinados a adquirir o seguro veicular. Tomando-se por base apenas o rol de clientes que ainda não possuem seguro automotivo (ou seja, com "previously_insured" = zero), tem-se os seguintes percentuais de pessoas interessadas no nosso produto:

<table align="center">
  <tr>
    <th align="center">"vehicle_age"</th>
    <th align="center">Interessadas</th>
    <th align="center">Não Interessadas</th>
  </tr>
  <tr>
    <td align="center">bellow_1_year</td>
    <td align="center">12,86%</td>
    <td align="center">87,14%</td>
  </tr>
  <tr>
    <td align="center">between_1_2_years</td>
    <td align="center">25,71%</td>
    <td align="center">74,29%</td>
  </tr>
  <tr>
    <td align="center">over_2_years</td>
    <td align="center">29,45%</td>
    <td align="center">70,55%</td>
  </tr>
</table>


Conclui-se assim que, contrariamente à hipótese original, quanto mais novo o veículo, menor o interesse pelo seguro automotivo.


# 9. RESULTADO-II: IMPACTO NA CAMPANHA DE VENDAS

Conforme apresentado no tópico 4.1, o produto final contratado prevê a resposta a três questões relativas à campanha de vendas a ser implantada pela empresa cliente. Para tanto, são apresentados os resultados do processamento sobre os dados de teste, seguindo-se as questões e respectivas respostas.

## 9.1. Resultado da aplicação do modelo aos dados de teste

A ideia é comparar os resultados da estratégia de vendas com e sem o uso de <i>machine learning</i>. 

BASE DE TESTE:
A base de dados de teste contém 127 mil registros (ou 127024), dos quais 15671 (12.34%) referem-se a pessoas interessadas na compra do produto (classe-1). Observar que, devido à randomização dos dados, o valor de 12.34% dessa amostra tem pequena diferença em relação aos 12.26% originalmente esperados.

<table align="center">
  <tr>
    <th>Totais</th>
    <th align="center">valor</th>
  </tr>
  <tr>
    <td>População testada</td>
    <td align="center">127024</td>
  </tr>
  <tr>
    <td>População interessada</td>
    <td align="center">15671 (12.34%)</td>
  </tr>
  <tr>
    <td>Receita total (health-insurance)</td>
    <td align="center">$ 495.457.449,00</td>
  </tr>
</table>


Nos dados acima, a receita total de $ 495 milhões refere-se ao somatório dos valores conhecidos, quais sejam, os prêmio de seguro-saúde dos 15671 registros da classe-1. Para fins de avaliação, essa informação será tomada como estimativa da receita a ser auferida com a venda do novo seguro automotivo.

As questões de negócio e os resultados alcançados são apresentados nos tópicos abaixo, podendo ser resumidas no seguinte gráfico:

![banner](img/business_performance.png)



## 9.2. Questão-1: Com 20 mil ligações, qual deverá ser a porcentagem de clientes interessados no produto?

No caso <b>sem o uso de ML</b>, os 20 mil registros são escolhidos aleatoriamente. O cálculo nessas condições resultou em 2407 pessoas interessadas (12.04% de 20 mil), representando receita de $ 75.612.858,00.

Ao se <b>fazer uso do modelo de ML</b> para ordenamento inteligente da lista de clientes, foi possível encontrar 6921 pessoas interessadas (34.6% de 20 mil), representando receita de $ 234.348.974,00.

Resultado: incremento de 187.5% no número de contratações, e com o triplo da receita (+210%).


## 9.3. Questão-2: E no caso de 40 mil ligações?

No caso <b>sem o uso de ML</b>, os 40 mil registros são escolhidos aleatoriamente. O cálculo nessas condições resultou em 4946 pessoas interessadas (12.36% de 40 mil), representando receita de $ 157.742.884,00.

Ao se <b>fazer uso do modelo de ML</b> para ordenamento inteligente da lista de clientes, foi possível encontrar 12346 pessoas interessadas (30.86% de 40 mil), representando receita de $ 400.301.534,00.

Resultado: incremento de 149.6% no número de contratações, e com incremento de 154% na receita.


## 9.4. Questão-3: Quantas ligações serão necessárias para contactar 80% dos clientes interessados?

Nesse caso, os dados indicam a necessidade de uma amostra de 40922 pessoas, representando 32.22% do total de 127024.


# 10. RESULTADO-III: PLANILHA EXCEL INTELIGENTE

Com o intuito de facilitar o uso do algoritmo de predição por meio de planilha excel, foi construída solução em duas etapas. De um lado, o algoritmo de ML foi implantado como WebService em nuvem, no site da [RENDER](https://render.com/), ficando assim disponível para acesso amplo por meio da URL https://health-insurance-priv.onrender.com/healthinsurance/predict.

De outro lado, construi-se uma rotina em VBA do Excel, para funcionar como cliente do WebService. Do lado do usuário, basta colocar os dados dos clientes na planilha, na ordem apropriada de colunas conforme figura abaixo, selecionar a linha ou linhas para as quais pretende obter a previsão de probabilidade de compra e digitar CONTROL+SHIFT+P.

![banner](img/excel_sheet.png)

Como resultado deste desenvolvimento, tem-se a possibilidade de uso do algoritmo de predição por meio de ferramenta popular, como o MS-Excel, permitindo que o projeto seja integrado ao uso diário da empresa.


# 11. RESULTADOS ALCANÇADOS & CONCLUSÃO

Por meio do presente projeto foi feita a análise de um caso de negócio visando aumentar o alcance de uma campanha de vendas de empresa seguradora. O desafio foi o de criar um método inteligente para selecionar os clientes mais propensos a comprar um novo produto da referida empresa.

Como resultado do trabalho, obteve-se: (i) a elaboração de insights de negócio a partir dos dados, (ii) a construção de uma máquina baseada no algoritmo de <i>Logistic Regression</i> para predição da propensão de compra por parte de um rol de pessoas pesquisadas, tendo capacidade de triplicar o resultado da campanha de vendas, e (iii) a construção de uma planilha Excel integrada com o sistema de predição para obtenção de informações em tempo real.


# 12. PRÓXIMOS PASSOS

Dentre os possíveis aprimoramentos do projeto, tem-se a possibilidade de aprimorar a etapa de coleta de dados, com a inclusão de novas informações de interesse para o negócio, como: características específicas dos contratos de seguro automotivo, características sócio-econômicas das regiões de atuação da empresa, entre outras, conforme abordado no tópico 8 deste documento.


# 13. FERRAMENTAS UTILIZADAS

No desenvolvimento do presente trabalho, as seguintes ferramentas foram utilizadas:
- Linguagem de Programação Python, versão 3.11.9
- Versionador de códigos GIT
- Jupyter Notebook & Visual Studio Code
- Serviço de hospedagem [Render.com](https://render.com/)
- Técnicas de manipulação de dados com Python
- Técnica de seleção de atributos com o Buruta
- Algoritmos de machine learning da biblioteca scikit-learn
- Biblioteca Flask<sup>5</sup>
- ChatGPT 4o

Em tempo, o presente texto na versão em português foi preparado sem a ajuda de IA generativa. Por sua vez, seu versionamento para o inglês foi feito utilizando-se o ChatGPT, com nossa revisão. O <i>brainstorming</i> inicial da seção 8 do presente texto teve também ajuda do ChatGPT. As tabelas escritas em padrão <i>markdown</i> foram convertidas para as tabelas mais versáteis do html usando o ChatGPT. Finalmente, ao longo do desenvolvimento do código, o ChatGPT foi utilizado pontualmente na busca por eventuais erros de codificação no python, ajustes em algumas funções e para embelezamento de alguns gráficos.


# 14. REFERÊNCIAS

1. Sítio do Kaggle, endereço https://www.kaggle.com/datasets/anmolkumar/health-insurance-cross-sell-prediction, consultado em agosto-2024.
2. Livro: "Hands-On Machine Learning with Scikit-Learn, Keras & TensorFlow", Aurelién Géron, 3ª edição, 2023.
3. Livro: "Python for Finance Cookbook", Erik Lewinson, 2ª edição, 2022.
4. Livro: "Machine Learning Bootcamp - Build a portfolio of real-life projects", Alexey Grigorev, 2021
5. Documentação da biblioteca Flask, endereço https://flask.palletsprojects.com/en/2.3.x/api/#flask.Blueprint.route, consultada em 08-fevereiro-2024.

