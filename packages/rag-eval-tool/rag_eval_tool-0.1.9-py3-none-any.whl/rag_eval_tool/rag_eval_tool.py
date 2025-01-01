import torch
from sacrebleu import corpus_bleu
from rouge_score import rouge_scorer
from bert_score import score
from transformers import GPT2LMHeadModel, GPT2Tokenizer, pipeline
import nltk
from nltk.util import ngrams
from nltk.tokenize import word_tokenize
from nltk.translate.meteor_score import meteor_score
from nltk.translate.chrf_score import sentence_chrf
from textstat import flesch_reading_ease, flesch_kincaid_grade
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics import precision_score, recall_score, f1_score
from nltk.corpus import stopwords
from collections import Counter
import numpy as np


class RAG_Eval_Tool:
    def __init__(self):
        """Initialize the RAG_Eval_Tool class and ensure required resources are available."""
        # Download required NLTK resources
        self.ensure_nltk_data()

        # Load GPT-2 model and tokenizer
        self.gpt2_model, self.gpt2_tokenizer = self.load_gpt2_model()

        # Initialize the bias detection pipeline
        self.bias_pipeline = pipeline("zero-shot-classification", model="Hate-speech-CNERG/dehatebert-mono-english")

    def ensure_nltk_data(self):
        """Ensure required NLTK resources are downloaded."""
        try:
            nltk.data.find('tokenizers/punkt')
        except LookupError:
            nltk.download('punkt', quiet=True)

        try:
            nltk.data.find('corpora/stopwords')
        except LookupError:
            nltk.download('stopwords', quiet=True)

        # Handle punkt_tab gracefully
        try:
            nltk.data.find('tokenizers/punkt_tab')
        except LookupError:
            try:
                nltk.download('punkt_tab', quiet=True)
            except Exception as e:
                print(f"punkt_tab not available: {e}")

        # Optional: Prevent errors from other NLTK dependencies like wordnet
        try:
            nltk.data.find('corpora/wordnet')
        except LookupError:
            nltk.download('wordnet', quiet=True)

    def load_gpt2_model(self):
        """Load GPT-2 model and tokenizer."""
        model = GPT2LMHeadModel.from_pretrained('gpt2')
        tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
        return model, tokenizer

    def evaluate_bleu_rouge(self, candidates, references):
        bleu_score = corpus_bleu(candidates, [references]).score
        scorer = rouge_scorer.RougeScorer(['rouge1', 'rouge2', 'rougeL'], use_stemmer=True)
        rouge_scores = [scorer.score(ref, cand) for ref, cand in zip(references, candidates)]
        rouge1 = sum([score['rouge1'].fmeasure for score in rouge_scores]) / len(rouge_scores)
        return bleu_score, rouge1

    def evaluate_bert_score(self, candidates, references):
        P, R, F1 = score(candidates, references, lang="en", model_type='bert-base-multilingual-cased')
        return P.mean().item(), R.mean().item(), F1.mean().item()

    def evaluate_perplexity(self, text):
        encodings = self.gpt2_tokenizer(text, return_tensors='pt')
        max_length = self.gpt2_model.config.n_positions
        stride = 512
        lls = []
        for i in range(0, encodings.input_ids.size(1), stride):
            begin_loc = max(i + stride - max_length, 0)
            end_loc = min(i + stride, encodings.input_ids.size(1))
            trg_len = end_loc - i
            input_ids = encodings.input_ids[:, begin_loc:end_loc]
            target_ids = input_ids.clone()
            target_ids[:, :-trg_len] = -100
            with torch.no_grad():
                outputs = self.gpt2_model(input_ids, labels=target_ids)
                log_likelihood = outputs[0] * trg_len
            lls.append(log_likelihood)
        ppl = torch.exp(torch.stack(lls).sum() / end_loc)
        return ppl.item()

    def evaluate_diversity(self, texts):
        all_tokens = [tok for text in texts for tok in text.split()]
        unique_bigrams = set(ngrams(all_tokens, 2))
        diversity_score = len(unique_bigrams) / len(all_tokens) if all_tokens else 0
        return diversity_score

    def evaluate_racial_bias(self, text):
        results = self.bias_pipeline([text], candidate_labels=["hate speech", "not hate speech"])
        bias_score = results[0]['scores'][results[0]['labels'].index('hate speech')]
        return bias_score

    def evaluate_meteor(self, candidates, references):
        meteor_scores = [
            meteor_score([word_tokenize(ref)], word_tokenize(cand))
            for ref, cand in zip(references, candidates)
        ]
        return sum(meteor_scores) / len(meteor_scores) if meteor_scores else 0

    def evaluate_chrf(self, candidates, references):
        chrf_scores = [sentence_chrf(ref, cand) for ref, cand in zip(references, candidates)]
        return sum(chrf_scores) / len(chrf_scores) if chrf_scores else 0

    def evaluate_readability(self, text):
        try:
            flesch_ease = flesch_reading_ease(text)
            flesch_grade = flesch_kincaid_grade(text)
        except Exception as e:
            print(f"Error in readability calculation: {e}")
            flesch_ease = 0
            flesch_grade = 0
        return flesch_ease, flesch_grade

    def evaluate_hallucination(self, response, reference):
        stop_words = set(stopwords.words('english'))
        response_tokens = set(word_tokenize(response.lower())) - stop_words
        reference_tokens = set(word_tokenize(reference.lower())) - stop_words
        hallucinated_tokens = response_tokens - reference_tokens
        hallucination_ratio = len(hallucinated_tokens) / len(response_tokens) if response_tokens else 0
        return hallucination_ratio

    def evaluate_precision_recall_f1(self, response, reference):
        true_tokens = set(reference.split())
        response_tokens = set(response.split())
        precision = len(true_tokens & response_tokens) / len(response_tokens) if response_tokens else 0
        recall = len(true_tokens & response_tokens) / len(true_tokens) if true_tokens else 0
        f1 = (2 * precision * recall) / (precision + recall) if (precision + recall) > 0 else 0
        return precision, recall, f1

    def evaluate_entropy(self, texts):
        all_tokens = [tok for text in texts for tok in text.split()]
        token_counts = Counter(all_tokens)
        total_tokens = sum(token_counts.values())
        entropy = -sum((count / total_tokens) * np.log2(count / total_tokens) for count in token_counts.values())
        return entropy

    def evaluate_all(self, response, reference):
        candidates = [response]
        references = [reference]
        bleu, rouge1 = self.evaluate_bleu_rouge(candidates, references)
        bert_p, bert_r, bert_f1 = self.evaluate_bert_score(candidates, references)
        perplexity = self.evaluate_perplexity(response)
        diversity = self.evaluate_diversity(candidates)
        racial_bias = self.evaluate_racial_bias(response)
        meteor = self.evaluate_meteor(candidates, references)
        chrf = self.evaluate_chrf(candidates, references)
        flesch_ease, flesch_grade = self.evaluate_readability(response)
        hallucination = self.evaluate_hallucination(response, reference)
        precision, recall, f1 = self.evaluate_precision_recall_f1(response, reference)
        entropy = self.evaluate_entropy(candidates)

        return {
            "BLEU": bleu,
            "ROUGE-1": rouge1,
            "BERT P": bert_p,
            "BERT R": bert_r,
            "BERT F1": bert_f1,
            "Perplexity": perplexity,
            "Diversity": diversity,
            "Racial Bias": racial_bias,
            "METEOR": meteor,
            "CHRF": chrf,
            "Flesch Reading Ease": flesch_ease,
            "Flesch-Kincaid Grade": flesch_grade,
            "Hallucination": hallucination,
            "Precision": precision,
            "Recall": recall,
            "F1": f1,
            "Entropy": entropy
        }
