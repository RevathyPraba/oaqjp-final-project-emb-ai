''' Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def detect_emotion():
    """
    Detects the emotion
    """
    try:
        text_to_analyse = request.args.get('textToAnalyze')
        result = emotion_detector(text_to_analyse)
        if result['dominant_emotion'] is None:
            return "Invalid text! Please try again!."
        return (
            f"For the given statement, the system response is "
            f"'anger': {result['anger']}, "
            f"'disgust': {result['disgust']}, "
            f"'fear': {result['fear']}, "
            f"'joy': {result['joy']}, "
            f"'sadness': {result['sadness']}. "
            f"The dominant emotion is {result['dominant_emotion']}."
        )
    except NameError:
        return "Enter a valid string."

@app.route("/")
def render_index_page():
    """
    Renders the index.html on running the application
    """
    return render_template('index.html')

if __name__ == "__main__":
    #Provide the host and port where the app will run
    app.run(host="0.0.0.0", port=4102)
