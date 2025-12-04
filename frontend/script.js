document.getElementById("analyzeBtn").addEventListener("click", async () => {
    const fileInput = document.getElementById("resume");
    const jobDesc = document.getElementById("jobDescription").value;

    if (!fileInput.files.length) {
        alert("Please upload a resume PDF.");
        return;
    }

    if (jobDesc.trim() === "") {
        alert("Please enter a job description.");
        return;
    }

    const formData = new FormData();
    formData.append("resume", fileInput.files[0]);
    formData.append("job_description", jobDesc);

    try {
        const response = await fetch("http://127.0.0.1:8000/resume/analyze-resume", {
            method: "POST",
            body: formData
        });

        if (!response.ok) {
            throw new Error("Backend error: " + response.status);
        }

        const result = await response.json();

        // Save in browser storage
        localStorage.setItem("analysisResult", JSON.stringify(result));

        // Redirect to results page
        window.location.href = "results.html";

    } catch (error) {
        console.error(error);
        alert("Failed to analyze resume. Check backend.");
    }
});







