import requests, json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = input_json, headers = headers)
    if response.status_code == 200:
        emotion_result = json.loads(response.text)
        emotion_score = emotion_result["emotionPredictions"][0]["emotion"]
        emotion_score['dominant_emotion'] = max(emotion_score, key=emotion_score.get)
    elif response.status_code == 400:
        emotion_score = {
            "anger": None, 
            "disgust": None, 
            "fear": None, 
            "joy": None, 
            "sadness": None, 
            "dominant_emotion": None
        }
    return emotion_score