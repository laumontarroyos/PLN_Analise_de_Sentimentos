# PLN-analise_de_sentimentos

![](/img/Enunciado-do-Projeto.png)

### Fonte de Dados: 
####Para realizar a análsie de sentimentos solicitada, coletou-se dados de avaliações feitas para o curso "Sequence Models", capacitação ####que faz parte da especialização em "Deep Learning da plataforma on-line de cursos da "Coursera", cujo endereço é o ####"https://www.coursera.org/learn/nlp-sequence-models". Foram capturadas 6467 avaliações em 21/03/2023 por um programa elaborado em ####python, fazendo uso da biblioteca "Scrapy", a partir do endereço "https://www.coursera.org/learn/nlp-sequence-models/reviews?page=1". 
####Os dados foram armazenados no arquivo "Coursera.csv" e, em um segundo momento, pré-processados por rotinas python em uma seção ####específica de um "notebook", realizando ajustes nos dados coletados, a exemplo do realizado para tornar a informação do número de ####estrelas um dado numérico e também a modificação que acabou por atribuir às avaliações de uma a três estrelas o conceito de uma ####avaliação "ruim", enquanto que tanto as avaliações atribuídas com quatro quanto aquelas com cinco estrelas receberam o conceito  de ####uma "boa" avaliação. Esses novos conceitos foram adotados, sobretudo, para incrementar o número de instâncias de treinamento ditas ####como de avaliação "ruim", dada a grande discrepância existente nos dados comparativamente às avaliações com quatro e cinco estrelas.


## Análise de Sentimentos comparando uso do SVM e Bert em dados coletados de avaliações de  um Curso da "Coursera"

![](/img/BERTxSVM-bow-linear.png)

PLN_2_Bert.ipynb

PLN_SVM02.ipynb

![](/img/SVM-BOW.png)

![](/img/SVM-Embeddings.png)

![](/img/SVM-TF-IDF.png)

![](/img/ChatGPT.png)

OpenAI_GPT_3_5_turbo.ipynb
