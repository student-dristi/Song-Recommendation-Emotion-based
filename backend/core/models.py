from transformers import pipeline
from functools import lru_cache

@lru_cache()
def load_model():
    # Load Hugging Face emotion classification model
    return pipeline(
        "text-classification",
        model="j-hartmann/emotion-english-distilroberta-base",
        top_k=None
    )

def predict_emotion(text):
    clf = load_model()
    preds = clf(text)[0]  # Get predictions
    preds = sorted(preds, key=lambda x: x['score'], reverse=True)
    top = preds[0]['label']
    return {"emotion": top, "scores": preds}
