import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler, LabelEncoder
import joblib

#Preprocess
df = pd.read_csv('realistic_data_center_metrics.csv')

df['timestamp'] = pd.to_datetime(df['timestamp']).apply(lambda x: x.timestamp())


label_encoders = {}
for col in ['device_id', 'rack_location']:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    label_encoders[col] = le


numerical_cols = ['timestamp', 'cpu_utilization', 'memory_usage', 'disk_io', 'temperature', 'network_traffic', 'power_usage']

scaler = StandardScaler()
df[numerical_cols] = scaler.fit_transform(df[numerical_cols])

#Training
features = ['timestamp', 'device_id', 'rack_location'] + ['cpu_utilization', 'memory_usage', 'disk_io', 'temperature', 'network_traffic', 'power_usage']
model = IsolationForest(contamination=0.05, random_state=42)
model.fit(df[features])


# Save joblib
joblib.dump(model, 'anomaly_detection_model.joblib')
joblib.dump(scaler, 'scaler.joblib')
joblib.dump(label_encoders, 'label_encoders.joblib')
