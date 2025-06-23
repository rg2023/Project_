from flask import Flask, request, jsonify
from utils.storage import upload_file
from utils.secrets import get_secret
from utils.database import insert_data
from utils.vertex import analyze_text

app = Flask(__name__)

@app.route('/')
def home():
    return "Backend is running!", 200

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    bucket_name = "bucket-sandbox-lz-rachelge"
    upload_file(bucket_name, file)
    return jsonify({"message": "File uploaded"}), 200

@app.route('/upload', methods=['GET'])
def upload():
    bucket_name = "bucket-sandbox-lz-rachelge"
    files = get_files(bucket_name)
    return jsonify({"files": files}), 200

@app.route('/save', methods=['POST'])
def save():
    data = request.json
    insert_data(data['name'], data['value'])
    return jsonify({"message": "Saved to DB"}), 200

@app.route('/analyze', methods=['POST'])
def analyze():
    text = request.json.get('text')
    result = analyze_text(text)
    return jsonify({"result": result}), 200

if __name__ == '__main__':
    app.run(debug=True)
