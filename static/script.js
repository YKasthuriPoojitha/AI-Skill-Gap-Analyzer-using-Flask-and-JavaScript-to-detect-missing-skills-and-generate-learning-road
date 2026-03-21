async function analyze() {
    const fileInput = document.getElementById("file").files[0];
    const resume = document.getElementById("resume").value;
    const jobRole = document.getElementById("jobRole").value;

    let response;

    if (fileInput) {
        const formData = new FormData();
        formData.append("file", fileInput);
        formData.append("jobRole", jobRole);

        response = await fetch("/analyze", {
            method: "POST",
            body: formData
        });

    } else {
        response = await fetch("/analyze", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                resume: resume,
                jobRole: jobRole
            })
        });
    }

    const data = await response.json();

    document.getElementById("output").innerText =
        "Score: " + data.score + "%\n\n" +
        "Missing Skills: " + data.missing_skills.join(", ") + "\n\n" +
        "Roadmap:\n" + data.roadmap.join("\n");
}