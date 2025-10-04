// -------------------------------
// 1️⃣ Background Music Toggle
// -------------------------------
function toggleMusic() {
    const audio = document.getElementById("bg-music");
    const button = document.getElementById("toggleButton");

    if (audio.paused) {
        audio.play();
        button.textContent = "Pause Music";
    } else {
        audio.pause();
        button.textContent = "Play Music";
    }
}

// -------------------------------
// 2️⃣ Preferred Action "Other" Field
// -------------------------------
document.getElementById("preferredAction").addEventListener("change", function () {
    const otherField = document.getElementById("otherText");
    otherField.style.display = this.value === "Other" ? "block" : "none";
});

// -------------------------------
// 3️⃣ Submit Complaint Form
// -------------------------------
document.getElementById("complaintForm").addEventListener("submit", function (e) {
    e.preventDefault();

    // reference to the form
    const form = e.target;

    // fake complaint id (you can replace with backend response later)
    const result = { complaint_id: Math.floor(Math.random() * 10000) };

    // show success message
    document.getElementById("complaint-response").innerHTML =
        `<p style='color:green;'>✅ Complaint submitted successfully! 
        Your Complaint ID: <strong>${result.complaint_id}</strong></p>`;

    // reset the form
    form.reset();
});

// -------------------------------
// 4️⃣ Track Complaint Form
// -------------------------------
document.getElementById("trackingForm").addEventListener("submit", function (e) {
    e.preventDefault();

    alert("Complaint ID not found")
});

// -------------------------------
// 5️⃣ Submit Feedback Form
// -------------------------------
document.getElementById("feedbackForm").addEventListener("submit", function (e) {
    e.preventDefault();

    const form = e.target;

    // temporary feedback_id (replace with backend response later)
    const result = { feedback_id: Math.floor(Math.random() * 10000) };

    document.getElementById("feedback-response").innerHTML =
        `<p style='color:green;'>🌟 Feedback received! Thank you, your feedback ID: 
        <strong>${result.feedback_id}</strong></p>`;

    form.reset();
});

// -------------------------------
// 6️⃣ Toggle Laws Additional Content
// -------------------------------
function toggleContent() {
    const content = document.getElementById("additionalContent");
    content.style.display = content.style.display === "block" ? "none" : "block";
}
