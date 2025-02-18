from flask import Flask, request, jsonify, render_template
import joblib
import pandas as pd
import openai
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Load joblib
model = joblib.load('anomaly_detection_model.joblib')
scaler = joblib.load('scaler.joblib')
label_encoders = joblib.load('label_encoders.joblib')

client = openai.OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

def explain_anomaly(data,is_anomaly):
    status = "anomalous" if is_anomaly else "normal"
    prompt = (
        f"Explain why the following data center metric is {status}:\n\n"
        f"{data}\n\n"
        "Provide a detailed explanation in a clear, bullet-point list for improved readability. "
        "Current date is February 2025."
    )
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that explains why data center metrics are {status}."},
            {"role": "user", "content": prompt}
        ]
    )
    return completion.choices[0].message.content

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json

    # Preprocess
    data['timestamp'] = pd.to_datetime(data['timestamp']).timestamp()

    
    df = pd.DataFrame([data])
    
    
    for col in ['device_id', 'rack_location']:
        df[col] = label_encoders[col].transform(df[col])
        
    
    numerical_cols = ['timestamp', 'cpu_utilization', 'memory_usage', 'disk_io', 'temperature', 'network_traffic', 'power_usage']
    df[numerical_cols] = scaler.transform(df[numerical_cols])
    
    
    features = ['timestamp', 'device_id', 'rack_location'] + ['cpu_utilization', 'memory_usage', 'disk_io', 'temperature', 'network_traffic', 'power_usage']

    #prediction
    prediction = model.predict(df[features])
    is_anomaly = prediction[0] == -1 
    
    explanation = explain_anomaly(data,bool(is_anomaly))
    
    return jsonify({
        'is_anomaly': bool(is_anomaly),
        'explanation': explanation
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
