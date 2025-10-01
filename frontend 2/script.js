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
  const form = e.target;
  const formData = new FormData(form);

  fetch("https://break-the-silence.onrender.com/submit-complaint", {
    method: "POST",
    body: formData
  })
    .then(response => {
      if (!response.ok) throw new Error("Submission failed");
      return response.json();
    })
    .then(result => {
      document.getElementById("complaint-response").innerHTML =
        `<p style='color:green;'>✅ Complaint submitted successfully! Your Complaint ID: <strong>${result.complaint_id}</strong></p>`;
      form.reset();
      document.getElementById("otherText").style.display = "none"; // hide "Other" field after submit
    })
    .catch(error => {
      document.getElementById("complaint-response").innerHTML =
        `<p style="color:red;">${error.message}</p>`;
    });
});

// -------------------------------
// 4️⃣ Track Complaint Form
// -------------------------------
document.getElementById("trackingForm").addEventListener("submit", function (e) {
  e.preventDefault();
  const complaintId = document.getElementById("complaint-id").value.trim();

  fetch(`https://break-the-silence.onrender.com/track-complaint?complaint_id=${complaintId}`)
    .then(response => {
      if (!response.ok) throw new Error("Complaint ID not found");
      return response.json();
    })
    .then(data => {
      document.getElementById("complaint-status").innerHTML =
        `<p>Status: ${data.status}</p>`;
    })
    .catch(err => {
      document.getElementById("complaint-status").innerHTML =
        `<p style="color:red;">${err.message}</p>`;
    });
});

// -------------------------------
// 5️⃣ Submit Feedback Form
// -------------------------------
document.getElementById("feedbackForm").addEventListener("submit", function(e) {
  e.preventDefault();
  const form = e.target;
  const formData = new FormData(form);

  fetch("https://break-the-silence.onrender.com/submit-feedback", {
    method: "POST",
    body: formData
  })
    .then(response => {
      if (!response.ok) throw new Error("Feedback submission failed");
      return response.json();
    })
    .then(result => {
      document.getElementById("feedback-response").innerHTML =
        `<p style='color:green;'>🌟 Feedback received! Thank you, your feedback ID: <strong>${result.feedback_id}</strong></p>`;
      form.reset();
    })
    .catch(err => {
      document.getElementById("feedback-response").innerHTML =
        `<p style='color:red;'>${err.message}</p>`;
    });
});

// -------------------------------
// 6️⃣ Toggle Laws Additional Content
// -------------------------------
function toggleContent() {
  const content = document.getElementById("additionalContent");
  content.style.display = content.style.display === "block" ? "none" : "block";
}
