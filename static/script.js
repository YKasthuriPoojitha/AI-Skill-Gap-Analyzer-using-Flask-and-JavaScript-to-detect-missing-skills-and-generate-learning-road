async function analyze() {
    const resume = document.getElementById("resume").value;
    const jobRole = document.getElementById("jobRole").value;
    const output = document.getElementById("output");

    output.innerText = "Analyzing...";

    try {
        const response = await fetch("/analyze", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                resume: resume,
                jobRole: jobRole
            })
        });

        const data = await response.json();

        output.innerText =
            "Skills: " + data.skills.join(", ") + "\n\n" +
            "Missing Skills: " + data.missing_skills.join(", ") + "\n\n" +
            "Roadmap: " + data.roadmap.join(", ") + "\n\n" +
            "Score: " + data.score + "%";

    } catch (error) {
        output.innerText = "Error: " + error;
    }
}