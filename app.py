from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'  # replace with your database URI
db = SQLAlchemy(app)

class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(50), nullable=False)
    feedback = db.Column(db.Text, nullable=False)

@app.route('/')
def home():
    return "Welcome to the Feedback App!"

@app.route('/feedback', methods=['POST'])
def handle_feedback():
    data = request.get_json()
    feedback = Feedback(user_id=data['user_id'], feedback=data['feedback'])
    db.session.add(feedback)
    db.session.commit()
    return jsonify({"message": "Feedback received"}), 200

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
