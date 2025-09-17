import requests  # Import the requests library to handle HTTP requests
import json
def emotion_detector(text_to_analyze):  # Function definition. Takes string input (text_to_analyse)
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'  # URL of the emotion detection service
    myobj = { "raw_document": { "text": text_to_analyze } }  # Create a dictionary with the text to be analyzed
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}  # Set the headers required for the API request
    response = requests.post(url, json = myobj, headers=header)  # Send a POST request to the API with the text and headers
    if response.status_code == 400:
         dict_emotion_score = {
             "anger": None,
             "disgust": None,
             "fear": None,
             "joy": None,
             "sadness": None,
             "dominant_emotion": None
         }
         formatted_emotion_score = None
    else:
        formatted_response = json.loads(response.text)  #Parsing the JSON response from the API
        emotion_scores = formatted_response['emotionPredictions'][0]['emotion']
        dominant_emotion = max(emotion_scores, key=emotion_scores.get) # Get dominate score from the response
        dict_emotion_score = {
        "anger": emotion_scores['anger'],
        "disgust": emotion_scores['disgust'],
        "fear": emotion_scores['fear'],
        "joy": emotion_scores['joy'],
        "sadness": emotion_scores['sadness'],
        "dominant_emotion": dominant_emotion
        }    
    # Build the formatted string output
        formatted_emotion_score = (
            f"anger: {emotion_scores['anger']}\n"
            f"disgust: {emotion_scores['disgust']}\n"
            f"fear: {emotion_scores['fear']}\n"
            f"joy: {emotion_scores['joy']}\n"
            f"sadness: {emotion_scores['sadness']}\n"
            f"dominant emotion: {dominant_emotion}"
        )
    return dict_emotion_score, formatted_emotion_score