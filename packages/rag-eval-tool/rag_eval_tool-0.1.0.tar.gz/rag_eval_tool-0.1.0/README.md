# rag_eval_tool

rag_eval_tool is a Python library designed for comprehensive evaluation of Retrieval-Augmented Generation (RAG) systems and Large Language Models (LLMs). It offers a wide array of metrics to evaluate generated text across fluency, diversity, semantic similarity, readability, hallucination, and bias detection.

---

## Features

- **Text Similarity Metrics**: BLEU, ROUGE, BERTScore, METEOR, CHRF.
- **Fluency and Coherence**: Perplexity using GPT-2.
- **Lexical Metrics**: Diversity and Entropy.
- **Readability Scores**: Flesch Reading Ease, Flesch-Kincaid Grade Level.
- **Bias Detection**: Racial bias evaluation using a zero-shot classification model.
- **Hallucination Metrics**: Quantify unsupported content in generated text.
- **Precision/Recall/F1**: Measure token overlap between response and reference.

---

## Installation

Install the library directly from PyPI:

```bash
pip install rag_eval_tool
