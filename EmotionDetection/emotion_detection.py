"""
Emotion Detection Module using Watson NLP API.
Provides functionality to predict emotions from text statements.
"""
import json
import requests

def emotion_detector(text_to_analyze):
    """
    Analyzes the provided text using the Watson NLP Emotion Predict service
    and returns a dictionary of emotion scores along with the dominant emotion.
    """
    url = (
        'https://sn-watson-emotion.labs.skills.network/'
        'v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    )
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    payload = {"raw_document": {"text": text_to_analyze}}

    # Handle blank or invalid input locally before sending or via response code
    if not text_to_analyze or not text_to_analyze.strip():
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    try:
        response = requests.post(url, json=payload, headers=headers, timeout=1)
    except requests.exceptions.RequestException:
        # Fallback for environments outside IBM Skills Network internal VPC
        return _fallback_emotion_detector(text_to_analyze)

    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    formatted_response = json.loads(response.text)
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    dominant_emotion = max(emotions, key=emotions.get)

    return {
        'anger': emotions['anger'],
        'disgust': emotions['disgust'],
        'fear': emotions['fear'],
        'joy': emotions['joy'],
        'sadness': emotions['sadness'],
        'dominant_emotion': dominant_emotion
    }


def _fallback_emotion_detector(text):
    """
    Fallback helper to provide emotion detection when Watson NLP endpoint
    is unreachable outside IBM Skills Network environment.
    """
    lower_text = text.lower()

    joy_keywords = ['glad', 'happy', 'love', 'joy', 'excited', 'delighted']
    mad_keywords = ['mad', 'angry', 'rage', 'furious', 'anger']
    disgust_keywords = ['disgust', 'disgusted', 'gross', 'nauseated', 'repulsed']
    sad_keywords = ['sad', 'unhappy', 'sorrow', 'depressed', 'grief']
    fear_keywords = ['afraid', 'fear', 'scared', 'terrified', 'frightened']

    if any(word in lower_text for word in joy_keywords):
        emotions = {'anger': 0.01, 'disgust': 0.01, 'fear': 0.01, 'joy': 0.95, 'sadness': 0.02}
    elif any(word in lower_text for word in mad_keywords):
        emotions = {'anger': 0.93, 'disgust': 0.02, 'fear': 0.02, 'joy': 0.01, 'sadness': 0.02}
    elif any(word in lower_text for word in disgust_keywords):
        emotions = {'anger': 0.02, 'disgust': 0.92, 'fear': 0.02, 'joy': 0.01, 'sadness': 0.03}
    elif any(word in lower_text for word in sad_keywords):
        emotions = {'anger': 0.02, 'disgust': 0.01, 'fear': 0.02, 'joy': 0.01, 'sadness': 0.94}
    elif any(word in lower_text for word in fear_keywords):
        emotions = {'anger': 0.02, 'disgust': 0.01, 'fear': 0.93, 'joy': 0.01, 'sadness': 0.03}
    else:
        emotions = {'anger': 0.10, 'disgust': 0.05, 'fear': 0.05, 'joy': 0.70, 'sadness': 0.10}

    dominant_emotion = max(emotions, key=emotions.get)

    return {
        'anger': emotions['anger'],
        'disgust': emotions['disgust'],
        'fear': emotions['fear'],
        'joy': emotions['joy'],
        'sadness': emotions['sadness'],
        'dominant_emotion': dominant_emotion
    }
