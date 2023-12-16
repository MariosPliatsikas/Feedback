from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  # You can customize this as needed
from flask_cors import CORS  # Import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/api/feedback', methods=['POST'])
def store_feedback():
    data = request.get_json()

    # Process and store the feedback data in your database (to be implemented)

    return jsonify({'message': 'Feedback received and stored successfully!'})

if __name__ == '__main__':
    app.run(debug=True)

