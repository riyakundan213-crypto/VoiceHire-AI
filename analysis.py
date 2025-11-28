# analysis.py
import re
from textblob import TextBlob

FILLERS = ["um", "uh", "like", "you know", "so", "actually", "basically", "right"]

def count_fillers(text):
    text = text.lower()
    return sum(len(re.findall(r'\b' + f + r'\b', text)) for f in FILLERS)

def words_per_minute(words, duration):
    if duration <= 0:
        return 0
    return round(words / (duration / 60), 1)

def structural_score(text):
    keywords = ["situation","task","action","result","challenge","problem","solved"]
    score = sum(1 for k in keywords if k in text.lower())
    return min(100, (score / len(keywords)) * 100)

def compute_scores(transcript, duration=0):
    words = transcript.split()
    word_count = len(words)
    fillers = count_fillers(transcript)
    wpm = words_per_minute(word_count, duration)

    polarity = TextBlob(transcript).sentiment.polarity
    structure = structural_score(transcript)

    score = 50
    score += structure * 0.2
    score -= fillers * 2
    score += (polarity * 3)

    score = max(0, min(100, round(score, 1)))

    breakdown = {
        "word_count": word_count,
        "fillers": fillers,
        "wpm": wpm,
        "structure_score": round(structure,1),
        "sentiment_polarity": round(polarity,2),
        "overall_score": score
    }
    return score, breakdown

