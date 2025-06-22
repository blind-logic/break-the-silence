from flask import Flask, request, jsonify
import uuid

app = Flask(_name_)

# In-memory storage (for demo purposes only)
complaints = {}
feedbacks = {}

@app.route('/')
def home():
    return "Welcome to the Complaint and Feedback System!"

@app.route('/submit-complaint', methods=['POST'])
def submit_complaint():
    data = request.form

    full_name = data.get('full-name', 'Anonymous')
    email = data.get('email', '')
    description = data.get('incident-description')
    incident_date = data.get('incident-date')
    location = data.get('incident-location', 'Unknown')
    involved_parties = data.get('involved-parties', '')
    severity = data.get('severity')
    witness = data.get('witness', '')
    preferred_action = data.get('preferred-action', '')
    other_input = data.get('otherInput', '')

    if not description or not incident_date or not severity:
        return jsonify({"error": "Description, Date, and Severity are required!"}), 400

    complaint_id = str(uuid.uuid4())[:8]
    complaints[complaint_id] = {
        "full_name": full_name,
        "email": email,
        "description": description,
        "incident_date": incident_date,
        "location": location,
        "involved_parties": involved_parties,
        "severity": severity,
        "witness": witness,
        "preferred_action": preferred_action if preferred_action != 'Other' else other_input,
        "status": "Pending",
    }

    return jsonify({
        "message": "Complaint submitted successfully!",
        "complaint_id": complaint_id
    }), 200

@app.route('/track-complaint', methods=['GET'])
def track_complaint():
    complaint_id = request.args.get('complaint_id')
    if complaint_id in complaints:
        return jsonify({
            "complaint_id": complaint_id,
            "status": complaints[complaint_id]['status']
        }), 200
    else:
        return jsonify({"error": "Complaint not found"}), 404

@app.route('/submit-feedback', methods=['POST'])
def submit_feedback():
    data = request.form

    feedback_id = str(uuid.uuid4())[:8]
    feedbacks[feedback_id] = {
        "name": data.get('name', ''),
        "email": data.get('email', ''),
        "feedback_type": data.get('feedback-type', ''),
        "rating": data.get('rating', ''),
        "likes": data.get('likes', ''),
        "suggestions": data.get('suggestions', ''),
        "issues": data.get('issues', '')
    }

    return jsonify({
        "message": "Feedback submitted successfully!",
        "feedback_id": feedback_id
    }), 200

if _name_ == '_main_':
    app.run(debug=True)