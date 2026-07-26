import requests 
import json

def emotion_detector(text_to_analyse): # URL of the sentiment analysis service 
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Constructing the request payload in the expected format 
    myobj = { "raw_document": { "text": text_to_analyse } }

    # Custom header specifying the model ID for the sentiment analysis service 
    header =  {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Sending a POST request to the sentiment analysis API 
    response = requests.post(url, json=myobj, headers=header)

    # Parsing the JSON response from the API 
    formatted_response = json.loads(response.text)
    predictions =  formatted_response["emotionPredictions"][0]["emotion"]
    return {
        'anger': predictions["anger"],
        'disgust': predictions["disgust"],
        'fear': predictions["fear"],
        'joy': predictions["joy"],
        'sadness': predictions["sadness"],
        'dominant_emotion': max(predictions, key =predictions.get)
        }
