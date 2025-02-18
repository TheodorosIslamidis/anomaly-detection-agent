# Anomaly Detection AI Agent

Anomaly Detection AI Agent is designed to monitor and detect anomalies in a data center. The dataset includes:
- **Timestamp**
- **Device ID**
- **CPU Utilization**
- **Memory Usage**
- **Disk I/O**
- **Temperature**
- **Network Traffic**
- **Power Usage**

The dataset is synthetically generated using `syntheticData.py`. You can also generate your own dataset, but ensure the naming conventions and file placement align with the project's structure.

---

## Installation and Requirements

Ensure you have the following installed:
- **Python 3.8+**
- **pip (Python Package Manager)**
- **Docker**

---

## Running with Docker

### 1. Build the Docker Image:
```sh
docker build -t anomaly-detection-agent_4.0 .
```

### 2. Run the Container:
```sh
docker run -p 5000:5000 -e OPENAI_API_KEY=YOUR_API_KEY anomaly-detection-agent_4.0
```

### 3. Access the Application:
Open your browser and visit:
```
http://localhost:5000
```

---

## Running Locally

### 1. Create a Virtual Environment:
```sh
python -m venv venv
```

### 2. Activate the Virtual Environment:
#### On Windows:
```sh
venv\Scripts\activate
```
#### On macOS/Linux:
```sh
source venv/bin/activate
```

### 3. Install Dependencies:
```sh
pip install -r requirements.txt
```

### 4. Set Up API Key:
Create a `.env` file in the project root and add:
```
OPENAI_API_KEY=your_api_key_here
```

### 5. Train the Model:
```sh
python model_train.py
```

### 6. Run the Agent:
```sh
python app.py
```
Flask will start on:
```
http://127.0.0.1:5000
```

---

### Happy Coding! 🚀

