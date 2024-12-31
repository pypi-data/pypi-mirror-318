from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import warnings
import os
import logging

# Suppress warnings
warnings.filterwarnings("ignore")

# Suppress TensorFlow logs
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
logging.getLogger('tensorflow').setLevel(logging.FATAL)

# Suppress transformers logging
logging.getLogger('transformers').setLevel(logging.ERROR)

class Spam:
    def __init__(self, cache_dir=None, device=None):
        self.device = device if device else torch.device("cuda" if torch.cuda.is_available() else "cpu")
        try:
            # First try loading the tokenizer
            self.tokenizer = AutoTokenizer.from_pretrained("ZachBeesley/Spam-Detector", cache_dir=cache_dir)
            
            # Try loading the model directly first
            try:
                self.model = AutoModelForSequenceClassification.from_pretrained(
                    "ZachBeesley/Spam-Detector",
                    cache_dir=cache_dir
                ).to(self.device)
            except Exception as e:
                # If direct loading fails, try with from_tf=True
                try:
                    self.model = AutoModelForSequenceClassification.from_pretrained(
                        "ZachBeesley/Spam-Detector",
                        cache_dir=cache_dir,
                        from_tf=True
                    ).to(self.device)
                except Exception as inner_e:
                    # If both attempts fail, try forcing CPU device
                    self.device = torch.device("cpu")
                    self.model = AutoModelForSequenceClassification.from_pretrained(
                        "ZachBeesley/Spam-Detector",
                        cache_dir=cache_dir
                    ).to(self.device)
        except Exception as e:
            raise RuntimeError(f"Failed to initialize the model: {str(e)}\nTry installing tf-keras with 'pip install tf-keras'")

    def predict(self, text):
        inputs = self.tokenizer(text, return_tensors="pt", truncation=True, padding=True).to(self.device)
        outputs = self.model(**inputs)
        logits = outputs.logits
        probabilities = torch.softmax(logits, dim=1)
        spam_score = probabilities[0][1].item()
        return True if spam_score > 0.5 else False

    def filter(self, paragraph):
        sentences = paragraph.split('. ')
        inputs = self.tokenizer(sentences, return_tensors="pt", truncation=True, padding=True).to(self.device)
        outputs = self.model(**inputs)
        logits = outputs.logits
        probabilities = torch.softmax(logits, dim=1)
        spam_scores = probabilities[:, 1].tolist()
        non_spam_sentences = [sentence for sentence, score in zip(sentences, spam_scores) if score <= 0.5]
        return '. '.join(non_spam_sentences)