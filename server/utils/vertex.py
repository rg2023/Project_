from google.cloud import aiplatform

def analyze_text(text):
    aiplatform.init(project="YOUR_PROJECT_ID", location="us-central1")
    model = aiplatform.TextGenerationModel.from_pretrained("text-bison")
    response = model.predict(text)
    return response.text
