Pegasus-CopyNet: A novel Summarization Generation Framework for Scientific and Technological Texts
This study applies text summarization techniques to scientific and technological texts. This enables precise matching of relevant information, which holds significant importance in the handling and practical use of technological data. However, existing models lack specificity and
effectiveness in handling text summarization tasks for scientific and technological information, particularly in their ability to extract semantic features from complex texts. Therefore, this study
introduces an automatic summarization model for scientific and technological texts based on the Pegasus-CopyNet framework, the framework consists of three key components. Firstly, this paper
designs a multi-dimensional sentence masking strategy to achieve the fine-tuning of the Pegasus model on specific domain datasets,enabling it to generate word embedding vectors enriched with contex-tual semantic information. Secondly, these word embeddings are used as input to the
CopyNet model, where an enhanced CNN module performs local feature extraction. Finally, a technological terminology vocabulary and an optimized vocabulary selection mechanism are integrated, making the model’s summaries in scientific and technological domains more professional
and accurate. It can be concluded from the analysis of each experimental result, compared to baseline models, the r ouge scores in the field of scientific and technological information long-text summarization were improved in this paper, reaching 41.62% (ROUGE-1), 22.06% (ROUGE-2),and 36.41% (ROUGE-L).

The overall architecture of the model is illustrated in the figure below：

<p align="center">
  <img src="https://github.com/user-attachments/assets/ad88a67e-3382-47a4-bae0-04bd5701bdf8" width="100%">
</p>

The main contributions of the model are as follows:

• Using a dataset of scientific and technological texts and employing MLM and GSG tasks, the Pegasus model was fine-tuned. The MLM task made domain-specific adjustments to the masking
parameters, while in the GSG task, a multi-dimensional sentence-level masking strategy was designed based on the characteristics of scientific and technological texts.

• The construction strategy of the input text vocabulary, the scoring mechanism, and the probability transformation of the CopyNet model were optimized. Unique words in the input text were constructed into an additional vocabulary that can be utilized by the model, and their positions in the vocabulary were adjusted and enhanced based on their occurrence frequency. A penalty mechanism was incorporated into the scoring function for vocabulary selection, and Top-K sampling was used to select output words.

• In the state update mechanism module of the CopyNet model, CNN convolutional neural networks are utilized. By leveraging CNN, the local feature extraction of the decoder output and its contextual information in the scientific and technological texts is achieved, enhancing the understanding of scientific and technological text terminology and improving the quality of summary generation.

The flowchart of the GSG task is shown below:

<p align="center">
  <img src="https://github.com/user-attachments/assets/e99c1590-de9c-45eb-8b35-a2c079d219f7" width="80%">
</p>

The overall architecture of the summary generation layer is shown in the figure:

<p align="center">
  <img src="https://github.com/user-attachments/assets/6e2a63a0-3943-44b5-b360-271431d44a30" width="80%">
</p>

The details of all the datasets used in this study are summarized as follows:

| Dataset Name             | Avg Text Length | Avg Summary Length | Training Set Size | Test Set Size |
|--------------------------|-----------------|---------------------|-------------------|---------------|
| NLPCC2017                | 990             | 44                  | 10,000            | 10,000        |
| Fund Project             | 500             | 20                  | 9,000             | 1,000         |
| Sci-Tech Assmt. Project  | 5,000           | 400                 | 9,000             | 1,000         |
| CSL                      | 250             | 20                  | 10,000            | 1,000         |
| Chinese Patent           | 1,500           | 280                 | 10,000            | 1,000         |

The evaluation metrics used in this study mainly include ROUGE, BLEU, and BERTScore. The experimental results of the comparative models on scientific and technological short-text datasets are as follows:

| Model           | ROUGE-1 | ROUGE-2 | ROUGE-L | BLEU-1 | BLEU-2 | BLEU-4 | BERTScore(F1) |
|----------------|---------|---------|---------|--------|--------|--------|---------------|
| Seq2Seq         | 31.07%  | 18.06%  | 27.23%  | 43.91% | 33.15% | 25.33% | 72.18%        |
| BART            | 44.16%  | 20.33%  | 38.41%  | 56.03% | 44.43% | 34.70% | 79.03%        |
| BERT SUM        | 40.63%  | 19.71%  | 36.59%  | 51.24% | 40.84% | 32.53% | 77.52%        |
| PGN             | 36.56%  | 18.94%  | 32.06%  | 49.45% | 37.28% | 29.04% | 76.38%        |
| UniLM           | 40.58%  | 19.02%  | 37.75%  | 55.04% | 43.79% | 35.70% | 79.66%        |
| T5              | 41.62%  | 20.51%  | 38.55%  | 57.91% | 44.29% | 36.72% | 80.47%        |
| Pegasus-CopyNet | 41.40%  | 20.65%  | 37.23%  | 59.72% | 46.62% | 37.45% | 81.72%        |

The evaluation metrics used in this study mainly include ROUGE, BLEU, and BERTScore. The experimental results of the comparative models on scientific and technological long-text datasets are as follows:

| Model           | ROUGE-1 | ROUGE-2 | ROUGE-L | BLEU-1 | BLEU-2 | BLEU-4 | BERTScore(F1) |
|----------------|---------|---------|---------|--------|--------|--------|---------------|
| Seq2Seq         | 28.55%  | 13.71%  | 23.89%  | 42.17% | 31.32% | 24.08% | 70.38%        |
| BART            | 39.22%  | 19.63%  | 34.44%  | 53.47% | 42.83% | 33.54% | 75.62%        |
| BERTSUM         | 37.62%  | 15.61%  | 30.88%  | 49.66% | 37.92% | 29.13% | 74.43%        |
| PGN             | 34.37%  | 14.96%  | 29.51%  | 47.04% | 36.10% | 27.42% | 72.24%        |
| UniLM           | 38.78%  | 17.92%  | 33.08%  | 52.17% | 42.97% | 34.48% | 77.19%        |
| T5              | 40.50%  | 21.55%  | 34.93%  | 54.07% | 43.50% | 34.28% | 78.26%        |
| Pegasus-CopyNet | 41.62%  | 21.83%  | 36.41%  | 55.27% | 44.88% | 35.72% | 79.74%        |

The above scientific and technological text datasets were constructed by the authors. To obtain the datasets, please contact the authors directly. In addition, this study also conducts experiments on several publicly available datasets, and the results are shown in the table below:

| Model           | ROUGE-1 | ROUGE-2 | ROUGE-L | BLEU-4 | BERTScore(F1) |
|----------------|---------|---------|---------|--------|---------------|
| Seq2Seq         | 31.07%  | 18.06%  | 27.23%  | 30.49% | 71.93%        |
| BART            | 44.16%  | 20.33%  | 38.41%  | 37.28% | 79.34%        |
| BERTSUM         | 40.63%  | 19.71%  | 36.59%  | 35.77% | 78.82%        |
| PGN             | 36.56%  | 18.94%  | 32.06%  | 34.94% | 76.53%        |
| UniLM           | 40.58%  | 19.02%  | 37.75%  | 39.71% | 80.61%        |
| T5              | 41.62%  | 20.51%  | 38.55%  | 40.38% | 82.03%        |
| Pegasus-CopyNet | 41.40%  | 20.65%  | 37.23%  | 43.21% | 81.46%        |


| Model           | ROUGE-1 | ROUGE-2 | ROUGE-L | BLEU-4 | BERTScore(F1) |
|----------------|---------|---------|---------|--------|---------------|
| Seq2Seq         | 32.15%  | 15.28%  | 28.39%  | 29.91% | 72.83%        |
| BART            | 41.58%  | 22.75%  | 37.25%  | 36.92% | 76.92%        |
| BERTSUM         | 38.55%  | 19.83%  | 38.82%  | 35.27% | 76.03%        |
| PGN             | 37.82%  | 17.36%  | 35.48%  | 33.79% | 75.38%        |
| UniLM           | 41.52%  | 23.26%  | 36.57%  | 39.07% | 77.19%        |
| T5              | 40.25%  | 22.80%  | 38.20%  | 30.16% | 78.37%        |
| Pegasus-CopyNet | 45.29%  | 22.73%  | 39.46%  | 41.37% | 80.16%        |
| Model           | ROUGE-1 | ROUGE-2 | ROUGE-L | BLEU-4 | BERTScore(F1) |


| Model           | ROUGE-1 | ROUGE-2 | ROUGE-L | BLEU-4 | BERTScore(F1) |
|----------------|---------|---------|---------|--------|---------------|
| Seq2Seq         | 32.15%  | 15.28%  | 28.39%  | 29.91% | 72.83%        |
| BART            | 41.58%  | 22.75%  | 37.25%  | 36.92% | 76.92%        |
| BERTSUM         | 38.55%  | 19.83%  | 38.82%  | 35.27% | 76.03%        |
| PGN             | 37.82%  | 17.36%  | 35.48%  | 33.79% | 75.38%        |
| UniLM           | 41.52%  | 23.26%  | 36.57%  | 39.07% | 77.19%        |
| T5              | 40.25%  | 22.80%  | 38.20%  | 30.16% | 78.37%        |
| Pegasus-CopyNet | 45.29%  | 22.73%  | 39.46%  | 41.37% | 80.16%        |


This paper mainly describes a text summarization framework for the field of scientific and technological information management, which integrates the Pegasus and Copynet models to handle complex scientific texts. This study conducted customized retraining and fine-tuning of the Pegasus model,
using a dataset specifically designed for scientific texts. The selection strategy of masked sentences was optimized in the GSG training task, targeting the specific needs of scientific and technological
information texts. This improved the model’s ability to generate high-quality word embedding representation vectors. These vectors were subsequently used as inputs for the Copynet model, utilizing its efficient replication and generation mechanism to provide accurate and semantically rich summaries
for technological information texts. 

Meanwhile, at the summary generation layer, this study optimized the vocabulary construction,
vocabulary scoring, and state update modules of the Copynet model. These improvements enabled the model to more accurately identify key information and effectively copy essential terms from the
original text while generating coherent and semantically complete summary content. The experimental results on professional datasets in the field of scientific and technological management provide strong support for this method, with the model showing superior performance across various evaluation
metrics, especially in handling long texts and science data with dense specialized terminology
