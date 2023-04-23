# PLN-analise_de_sentimentos

![](/img/Enunciado-do-Projeto.png)

### Fonte de Dados: 
Para realizar a análsie de sentimentos solicitada, coletou-se dados de avaliações feitas para o curso "Sequence Models", capacitação que faz parte da especialização em "Deep Learning da plataforma on-line de cursos da "Coursera"(*), cujo endereço é o "https://www.coursera.org/learn/nlp-sequence-models". Foram capturadas 6.467 avaliações em 21/03/2023 por um programa elaborado em python, fazendo uso da biblioteca "Scrapy", a partir do endereço "https://www.coursera.org/learn/nlp-sequence-models/reviews?page=1". 
Os dados foram armazenados no arquivo "Coursera.csv" e, em um segundo momento, pré-processados por rotinas python em uma seção específica de um "notebook", realizando ajustes nos dados coletados, a exemplo do realizado para tornar a informação do número de estrelas um dado numérico e também a modificação que acabou por atribuir às avaliações de uma a três estrelas o conceito de uma avaliação "ruim", enquanto que tanto as avaliações atribuídas com quatro quanto aquelas com cinco estrelas receberam o conceito  de uma "boa" avaliação. Esses novos conceitos foram adotados, sobretudo, para incrementar o número de instâncias de treinamento ditas como de avaliação "ruim", dada a grande discrepância existente nos dados comparativamente às avaliações com quatro e cinco estrelas.

(*) © 2023 Coursera Inc. All rights reserved.

## Análise de Sentimentos comparando uso do SVM e BERT

Como pode ser visto na imagem abaixo, a abordagem fazendo uso do Bert supera em muito o desempenho alcançado com a melhor variação do SVM aplicada aos dados coletados. Notadamente, infere-se que o fato do Bert ser um modelo pré-treinado, no qual os dados coletados foram utilizados apenas para realizar um "fine-tunning", aparenta ter feito toda a diferença. Mesmo atribuindo o conceito "ruim" para as avaliações de uma a três estrelas, será possível perceber pelos resultados apresentados mais adiante que todos os experimentos com variações do SVM não são satisfatórios para classificar uma avaliação como "ruim". Observa-se, no caso do Bert, que a acurácia é alçada a níveis mais elevados que os 92% do SVM, chegado a 97%. O F1-score é superior  para uma "boa" avaliação, 0.98 a 0.96, e é extremamente melhor no F1-score para uma avaliação "ruim", 0.82 contra os 0.08 do SVM. Os detalhes da implementação usando o BERT estão no arquivo "notebook" "PLN_2_Bert.ipynb", enquanto que os experimentos feitos com o SVM estão no arquivo "notebook" "PLN_SVM02.ipynb".

![](/img/BERTxSVM-bow-linear.png)


## Análise de Sentimentos fazendo uso do SVM+BOW
Para os dados trabalhados nesta classificação, percebe-se não haver grande diferença entre o uso de um kernel linear e outro não linear para os experimentos realizados com a representação do texto pela técnica de "Bag-of_words" (BOW). Dada a similaridade dos resultados alcançados, considerando o F1-score levemente superior e a abordagem de processamento mais simples, entre as duas variações opta-se por escolher o modelo linear. Os detalhes da implementação usando o SVM+BOW estão no arquivo "notebook" "PLN_SVM02.ipynb".

![](/img/SVM-BOW.png)


## Análise de Sentimentos fazendo uso do SVM+Embeddings
Para os dados trabalhados nesta classificação, não se percebe um grande ganho no uso da representação textual com "Embeddings", quando comparamos o melhor resultado alcançado com aqueles pontuados ao usarmos "Bag-of-words". Na realidade, ambos são muito similares e foram os melhores resultados dos experimentos com SVM. Optou-se por usar o SVM+BOW para comparar com o BERT por darmos preferência ao modelo mais simples sempre que os resultados se assemelham. Considerando a variação SVM+Embeddings, o resultado com o modelo não linear foi ligeiramente superior ao alcançado com o Linear. Os detalhes da implementação usando o SVM+Embeddings também estão no arquivo "notebook" "PLN_SVM02.ipynb".

![](/img/SVM-Embeddings.png)


## Análise de Sentimentos fazendo uso do SVM+TF-IDF
Embora o Projeto não pedisse que fosse avaliada a classificação usando a abordagem TF-IDF, isto é, "term frequency–inverse document frequency", fizemos uso desta outra técnica de representação dos dados textuais também apenas por curiosidade. Como atestam os resultados apresentados na imagem abaixo, eles ficaram piores do que aqueles alcançados com as outras abordagens. O modelo não conseguiu realizar nenhuma classificação correta para as sentenças de avaliação "ruim" apresentadas no teste do experimento, seja com o kernel linear, seja com o kernel não linear do SVM. Os detalhes da implementação usando o SVM+TF-IDF também estão no arquivo "notebook" "PLN_SVM02.ipynb".
![](/img/SVM-TF-IDF.png)


## Experimento Bônus: usando o ChatGPT e a API da OpenAI para o GPT 3.5 turbo

OpenAI_GPT_3_5_turbo.ipynb
![](/img/ChatGPT.png)
