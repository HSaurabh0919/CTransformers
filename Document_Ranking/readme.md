## Document to Query Comparison Techniques,Papers, Data and Codes
### Papers:
1. [Pretrained Transformers for Text Ranking: BERT and Beyond](https://arxiv.org/abs/2010.06467)
2. [Multi Stage Ranking with BERT](https://www.researchgate.net/publication/360973402_Multi-Stage_Document_Ranking_with_BERT). Usage of multiple steps prediction helps for faster predictions.
3. [Improving Document Representations by Generating Pseudo Query
Embeddings for Dense Retrieval](https://arxiv.org/pdf/2105.03599.pdf)
4. [Understanding the Behaviors of BERT in Ranking](https://arxiv.org/pdf/1904.07531.pdf). The paper highlights the 4 categries for BERT compairson:
    - Representation based Ranker, (Embed Document d and Query q last layers's [CLS] value Separately and check cosine similarity)
    - Interaction based Ranker,(q and d are concatenated of last layers's [CLS] value and then linearly combine weight w)
    - Multi Interaction based Ranker,(q and d are concatenated of each layers's [CLS] value and then linearly combined with weight w)
    - [Adds a neural ranking network](https://github.com/HSaurabh0919/CTransformers/blob/main/Document_Ranking/Codes/NeuralRanking.ipynb) upon BERT,It first constructs the translation matrix between query and document, using the cosine similarities  between the projections of their contextual embeddings. Then it combines the translation matrices from all layers using mean-pooling and linear combination.


### Code:
1. [ColBERT is a fast and accurate retrieval model, enabling scalable BERT-based search over large text collections in tens of milliseconds](https://github.com/stanford-futuredata/ColBERT/blob/main/docs/intro.ipynb)
2. [Tensorflow For Ranking](https://github.com/tensorflow/ranking/blob/master/docs/tutorials/tfr_bert.ipynb) using Antique Dataset.
3. [Multi Stage Ranking with BERT](https://github.com/castorini/duobert)


### Personal Work and Codes

### Datasets:
1. [MS MARCO](https://microsoft.github.io/msmarco/) is a collection of datasets focused on deep learning in search. The first dataset was a question answering dataset featuring 100,000 real Bing questions and a human generated answer. 
2. [TREC Complex Answer Retrieval Overview](https://trec.nist.gov/pubs/trec26/papers/Overview-CAR.pdf)

### Performance Metrics
1. Mean Average Precision
2. Mean Reciprocal Rank

## Document to Data Comparison Techniques, Papers,Data and Codes
### Paper:
1. [Fine-tuned Siamese Sentence-BERT for
Matching Jobs and Job Seekers](https://arxiv.org/pdf/2109.06501.pdf). Explores Pooling of SBERT using sentence length, take the mean of last 4 layers of [CLS] sentences and taking first 512 tokens of each document(Seems naive but effective as per the author).
2. [Information Retrieval System](http://orion.lcg.ufrj.br/Dr.Dobbs/books/book5/chap14.htm)



## Latency Specific Works

### Papers:
1. [Intra-Document Cascading: Learning to Select Passages
for Neural Document Ranking](https://arxiv.org/pdf/2105.09816.pdf)
