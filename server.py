"""Flask app to analyze emotion in a string of data"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    """Analyze the text for emotion"""
    text_to_analyze = request.args.get('textToAnalyze')
    #If no text provided
    if not text_to_analyze:
        return "Invalid text! Please try again!"
    #Evaluate the text by calling emotion_detection.py
    dict_emotion_score, _ = emotion_detector(text_to_analyze)
    #Handle the user not entering data
    if dict_emotion_score['dominant_emotion'] is None:
        return 'Invalid text! Please try again!'
    #Handle the user entering correct data
    output = (
        f"For the given statement, the system response is "
        f"'anger': {dict_emotion_score['anger']}, "
        f"'disgust': {dict_emotion_score['disgust']}, "
        f"'fear': {dict_emotion_score['fear']}, "
        f"'joy': {dict_emotion_score['joy']} and "
        f"'sadness': {dict_emotion_score['sadness']}. "
        f"The dominant emotion is {dict_emotion_score['dominant_emotion']}."
    )
    return output

@app.route("/")
def render_index_page():
    """Renders the homepage with the input form for emotion analysis."""
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
