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

document.getElementById("options").addEventListener("change", function () {
  const otherField = document.getElementById("otherText");
  otherField.style.display = this.value === "Other" ? "block" : "none";
});

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
        "<p style='color:green;'>Complaint submitted successfully!</p>";
      form.reset();
    })
    .catch(error => {
      document.getElementById("complaint-response").innerHTML =
        `<p style="color:red;">${error.message}</p>`;
    });
});

document.getElementById("trackingForm").addEventListener("submit", function (e) {
  e.preventDefault();
  const complaintId = document.getElementById("complaint-id").value;

  fetch(`https://break-the-silence.onrender.com/track-complaint?complaint_id=${complaintId}`)
    .then(response => {
      if (!response.ok) throw new Error("Complaint not found");
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

function toggleContent() {
  const content = document.getElementById("additionalContent");
  content.style.display = content.style.display === "block" ? "none" : "block";
}
