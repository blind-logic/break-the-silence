from flask import Flask, request, jsonify
import uuid

app = Flask(__name__)

# In-memory complaint store (this would typically be a database)
complaints = {}

@app.route('/submit-complaint', methods=['POST'])
def submit_complaint():
    data = request.form  # Retrieve form data from the POST request
    
    # Extract the values
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

    # Store complaint in memory (this would go into a database in a real app)
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

    # Respond with the complaint ID
    return jsonify({
        "message": "Complaint submitted successfully!",
        "complaint_id": complaint_id
    }), 200


# New endpoint for tracking complaints
@app.route('/track-complaint', methods=['GET'])
def track_complaint():
    # Retrieve complaint ID from the request query parameters
    complaint_id = request.args.get('complaint_id')
    
    # Check if the complaint ID exists
    if complaint_id not in complaints:
        return jsonify({"error": "Complaint ID not found!"}), 404

    # Get the complaint details
    complaint = complaints[complaint_id]

    # Respond with the complaint details
    return jsonify({
        "complaint_id": complaint_id,
        "status": complaint["status"],
        "date_of_submission": complaint["date_of_submission"],
        "description": complaint["description"],
        "severity": complaint["severity"],
        "location": complaint["location"],
        "witnesses": complaint["witnesses"],
        "preferred_action": complaint["preferred_action"]
    }), 200

# In-memory feedback store (like a temporary database)
feedback_list = []

@app.route('/submit-feedback', methods=['POST'])
def submit_feedback():
    data = request.form

    # Extract form data
    name = data.get('name', 'Anonymous')
    email = data.get('email', '')
    feedback_type = data.get('feedbackType', 'General Feedback')
    rating = data.get('rating', '')
    liked = data.get('liked', '')
    suggestions = data.get('suggestions', '')
    issues = data.get('issues', '')

    # Optional: validate important fields
    if not feedback_type or not rating:
        return jsonify({"error": "Feedback type and rating are required."}), 400

    feedback_entry = {
        "name": name,
        "email": email,
        "feedback_type": feedback_type,
        "rating": rating,
        "liked": liked,
        "suggestions": suggestions,
        "issues": issues
    }

    feedback_list.append(feedback_entry)

    return jsonify({"message": "Feedback submitted successfully!"}), 200

    
if __name__ == '__main__':
    app.run(debug=True)