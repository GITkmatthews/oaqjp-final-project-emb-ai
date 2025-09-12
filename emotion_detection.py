import requests  # Import the requests library to handle HTTP requests
import json
def emotion_detector(text_to_analyze):  # Function definition. Takes string input (text_to_analyse)
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'  # URL of the emotion detection service
    myobj = { "raw_document": { "text": text_to_analyze } }  # Create a dictionary with the text to be analyzed
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}  # Set the headers required for the API request
    response = requests.post(url, json = myobj, headers=header)  # Send a POST request to the API with the text and headers
    #Parsing the JSON response from the API
    formatted_response = json.loads(response.text)
    emotion_scores = formatted_response['emotionPredictions'][0]['emotion']
    # Get dominate score from the response
    dominant_emotion = max(emotion_scores, key=emotion_scores.get)
    display_emotion_score = {
    "anger": emotion_scores['anger'],
    "disgust": emotion_scores['disgust'],
    "fear": emotion_scores['fear'],
    "joy": emotion_scores['joy'],
    "sadness": emotion_scores['sadness'],
    "dominant_emotion": dominant_emotion
    }    
    # Returning a dictionary containing sentiment analysis results
    return display_emotion_score 
