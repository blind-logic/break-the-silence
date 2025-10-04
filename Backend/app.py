from flask import Flask, request, jsonify
from flask_cors import CORS
import uuid, time

app = Flask(__name__)
CORS(app)   # allow cross-origin requests from your frontend

# -----------------------------------------------------------
# In-memory storage (cleared whenever the server restarts!)
# -----------------------------------------------------------
complaints = {}   # { complaint_id: {data…} }
feedbacks = {}    # { feedback_id: {data…} }

# Helper to create IDs that all *look* the same (homogeneous)
def generate_complaint_id():
    # BTS- + 8 uppercase hex characters (e.g. BTS-A1B2C3D4)
    return "BTS-" + uuid.uuid4().hex[:8].upper()

@app.route("/")
def home():
    return "Break the Silence backend is running."


# -----------------------------------------------------------
# 1️⃣ Submit a Complaint
# -----------------------------------------------------------
@app.route("/submit-complaint", methods=["POST"])
def submit_complaint():
    data = request.form

    # Make sure the names here match your <input name="..."> in index.html
    full_name        = data.get("full_name", "Anonymous")
    email            = data.get("email", "")
    description      = data.get("incident_description")
    incident_date    = data.get("incident_date")
    location         = data.get("incident_location", "Unknown")
    involved_parties = data.get("involved_parties", "")
    severity         = data.get("severity")
    witness          = data.get("witness", "")
    preferred_action = data.get("preferred_action", "")
    other_input      = data.get("other_input", "")

    if not description or not incident_date or not severity:
        return jsonify({"error": "Description, Date and Severity are required."}), 400

    complaint_id = generate_complaint_id()
    complaints[complaint_id] = {
        "full_name": full_name,
        "email": email,
        "description": description,
        "incident_date": incident_date,
        "location": location,
        "involved_parties": involved_parties,
        "severity": severity,
        "witness": witness,
        "preferred_action": preferred_action if preferred_action != "Other" else other_input,
        # track when it was created so we can fake a timeline
        "created_at": time.time(),
        "status": "Received",
    }

    return jsonify({
        "message": "✅ Your complaint has been recorded.",
        "complaint_id": complaint_id
    }), 200


# -----------------------------------------------------------
# 2️⃣ Track a Complaint
# -----------------------------------------------------------
@app.route("/track-complaint", methods=["GET"])
def track_complaint():
    complaint_id = request.args.get("complaint_id", "")
    if complaint_id not in complaints:
        return jsonify({"error": "Complaint ID not found."}), 404

    # --- Simple fake “timeline”: status advances with time ---
    created = complaints[complaint_id]["created_at"]
    elapsed = time.time() - created
    if elapsed > 60*2:          # 2 minutes
        complaints[complaint_id]["status"] = "Resolved – appropriate action taken."
    elif elapsed > 60*1:      # >1 minutes
        complaints[complaint_id]["status"] = "Processing – authorities reviewing."
    else:
        complaints[complaint_id]["status"] = "Received – pending review."

    return jsonify({
        "complaint_id": complaint_id,
        "status": complaints[complaint_id]["status"]
    }), 200


# -----------------------------------------------------------
# 3️⃣ Submit Feedback
# -----------------------------------------------------------
@app.route("/submit-feedback", methods=["POST"])
def submit_feedback():
    data = request.form
    feedback_id = str(uuid.uuid4())[:8].upper()

    feedbacks[feedback_id] = {
        "name": data.get("name", "Anonymous"),
        "email": data.get("email", ""),
        "feedback_type": data.get("feedback_type", ""),
        "rating": data.get("rating", ""),
        "likes": data.get("likes", ""),
        "suggestions": data.get("suggestions", ""),
        "issues": data.get("issues", "")
    }

    return jsonify({
        "message": "🌟 Thank you for sharing your feedback! "
                   "Your thoughts help us make the campus safer.",
        "feedback_id": feedback_id
    }), 200


if __name__ == "__main__":
    app.run(debug=True)
