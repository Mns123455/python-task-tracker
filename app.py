from flask import Flask, jsonify

app = Flask(__name__)

tasks = [
    {"id": 1, "task": "Learn Git", "status": "completed"},
    {"id": 2, "task": "Build Docker Image", "status": "pending"},
    {"id": 3, "task": "Deploy with Jenkins", "status": "pending"}
]

@app.route("/")
def home():
    return jsonify(
        application="Python Task Tracker",
        status="running",
        version="1.0"
    )

@app.route("/health")
def health():
    return jsonify(status="UP")

@app.route("/tasks")
def get_tasks():
    return jsonify(tasks)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
