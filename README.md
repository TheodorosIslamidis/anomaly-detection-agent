Anomaly Detection AI Agent

This is an anomaly detection AI agent for a data center.The data contain timestamp,device id,cpu utilization,memory usage,disk io,temperature,network traffic, power usage. The data are syntheticaly generated via the syntheticData.py. Optionaly you can use it to make your own data and use them instead,but be careful with the names and where you put them inside this project.

Installation and Requirements
Python 3.8+
pip (Python Package Manager)
Docker

Running with Docker
Build docker image
docker build -t anomaly-detection-agent_4.0 .
Run the container
docker run -p 5000:5000 -e OPENAI_API_KEY=YOUR_API_KEY anomaly-detection-agent_4.0
Open the browser at http://localhost:5000 and you will see the agent running.

Running locally
Create a Virtual Environment
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
Create a .env file in the project root and add your OpenAI API key:
OPENAI_API_KEY=your_api_key_here
Train the Model
python model_train.py
Run the Agent
python app.py
Flask will start on http://127.0.0.1:5000