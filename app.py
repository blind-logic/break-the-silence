from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Complaint and Feedback System!"

@app.route('/submit-complaint', methods=['POST'])
def submit_complaint():
    data = request.form  # Retrieve form data from the POST request
    
    # Extract the values from the form data
    full_name = data.get('fullName', 'Anonymous')
    email = data.get('email', '')
    description = data.get('description')
    incident_date = data.get('incidentDate')
    location = data.get('location', 'Unknown')
    involved_parties = data.get('involvedParties', '')
    severity = data.get('severity')
    witnesses = data.get('witnesses', '')
    preferred_action = data.get('preferredAction', '')

    # Validate required fields
    if not description or not incident_date or not severity:
        return jsonify({"error": "Description, Date, and Severity are required!"}), 400

    # Generate a unique complaint ID
    complaint_id = str(uuid.uuid4())[:8]  # Shorten the UUID for readability

    # Store the complaint in memory (this could go into a database in a real app)
    complaints[complaint_id] = {
        "full_name": full_name,
        "email": email,
        "description": description,
        "incident_date": incident_date,
        "location": location,
        "involved_parties": involved_parties,
        "severity": severity,
        "witnesses": witnesses,
        "preferred_action": preferred_action,
        "status": "Pending",
        "date_of_submission": incident_date
    }

    # Respond with the complaint ID and a success message
    return jsonify({
        "message": "Complaint submitted successfully!",
        "complaint_id": complaint_id
    }), 200


if __name__ == '__main__':
    app.run(debug=True)
