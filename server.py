from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    text_to_analyze = request.args.get('textToAnalyze')

    if not text_to_analyze:
        return "No text provided for analysis. Please enter a valid statement."

    dict_emotion_score, _ = emotion_detector(text_to_analyze)

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
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)