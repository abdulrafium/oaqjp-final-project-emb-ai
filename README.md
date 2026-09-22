# Final Project - Emotion Detector

## oaqjp-final-project-emb-ai

This is the final project submission for the IBM AI Application Development with Python and Flask course. The Emotion Detector is an AI-based web application that uses the Watson Natural Language Processing (NLP) library to detect emotions from text statements and deploys the model via a Flask web application.

## Project Overview

This application evaluates customer or user sentiment by classifying text into five fundamental emotional dimensions:
- **Anger**
- **Disgust**
- **Fear**
- **Joy**
- **Sadness**

In addition to individual emotion scores, the system identifies the **dominant emotion** (the one with the highest confidence level).

## Features
- **Watson NLP Integration**: Connects to the Watson Emotion Predict service to extract emotion confidence scores.
- **Output Formatting**: Parses raw response objects into a structured Python dictionary.
- **Robust Error Handling**: Handles blank inputs and status code 400 gracefully, returning `None` values.
- **Modular Packaging**: Packaged under the `EmotionDetection` module for easy reuse.
- **Unit Testing**: Verified with `unittest` test suite covering five emotional states.
- **Flask Web Deployment**: Deployed with an interactive web UI on port 5000.
- **Code Quality**: Validated with `pylint` achieving a 10.00/10 static analysis score.

## Directory Structure
```
oaqjp-final-project-emb-ai/
├── EmotionDetection/
│   ├── __init__.py
│   └── emotion_detection.py
├── static/
│   └── mywebscript.js
├── templates/
│   └── index.html
├── test_emotion_detection.py
├── server.py
├── README.md
└── requirements.txt
```

## Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/abdulrafium/oaqjp-final-project-emb-ai.git
   cd oaqjp-final-project-emb-ai
   ```

2. **Install required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run Unit Tests:**
   ```bash
   python -m unittest test_emotion_detection.py
   ```

4. **Start the Flask Application:**
   ```bash
   python server.py
   ```
   Access the web interface at `http://localhost:5000`.

5. **Static Code Analysis:**
   ```bash
   pylint server.py
   ```