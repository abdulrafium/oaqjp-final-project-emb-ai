# EmotionDetection

EmotionDetection is an AI-based web application that detects emotions from text statements using the Watson Natural Language Processing (NLP) library and deploys the model via a Flask web application interface.

## Project Overview

This application evaluates customer or user sentiment by classifying text into five fundamental emotional dimensions:
- **Anger**
- **Disgust**
- **Fear**
- **Joy**
- **Sadness**

In addition to individual emotion scores, the system identifies and outputs the **dominant emotion** with the highest confidence level.

## Features
- **Watson NLP Integration**: Connects to the Watson Emotion Predict service to extract emotion confidence scores.
- **Output Formatting**: Parses raw response objects into a structured Python dictionary.
- **Robust Error Handling**: Handles empty or invalid inputs gracefully, returning `None` values and informing the user.
- **Modular Packaging**: Packaged under the `EmotionDetection` module for reuse across applications.
- **Unit Testing**: Verified with `unittest` test suite covering multiple emotional states.
- **Flask Web Deployment**: Deployed with an interactive web UI.
- **Code Quality**: Validated with `pylint` achieving a 10.00/10 static analysis score.

## Directory Structure
```
EmotionDetection/
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
   git clone https://github.com/abdulrafium/EmotionDetection.git
   cd EmotionDetection
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