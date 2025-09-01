import requests  # Import the requests library to handle HTTP requests
import json
def emotion_detector(text_to_analyze):  # Function definition. Takes string input (text_to_analyse)
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'  # URL of the emotion detection service
    myobj = { "raw_document": { "text": text_to_analyze } }  # Create a dictionary with the text to be analyzed
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}  # Set the headers required for the API request
    response = requests.post(url, json = myobj, headers=header)  # Send a POST request to the API with the text and headers
    return response.text  # Return the response text from the API

 #Parsing the JSON response from the API
    formatted_response = json.loads(response.text)
    # Extracting sentiment label and score from the response
   
    #anger = formatted_response[0:0]
    #disgust = formatted_response[1:1]
    #fear = formatted_response[2:2]
    #joy = formatted_response[3:3]
    #sadness = formatted_response[4:4]
    #dominant_emotion = formatted_response['emotionPredictions'][0]
    
    # Returning a dictionary containing sentiment analysis results
    return {'emotion': emotion_prediction, 'score': score_prediction} 
