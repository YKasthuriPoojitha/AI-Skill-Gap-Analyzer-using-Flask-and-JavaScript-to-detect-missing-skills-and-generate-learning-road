async function analyze() {
    const resume = document.getElementById("resume").value;
    const jobRole = document.getElementById("jobRole").value;

    const output = document.getElementById("output");

    output.innerHTML = "Loading...";

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

        output.innerHTML = `
            <h3>Score: ${data.score}%</h3>
            <p><b>Missing Skills:</b> ${data.missing_skills.join(", ")}</p>
            <p><b>Roadmap:</b> ${data.roadmap.join(", ")}</p>
        `;
    } catch (error) {
        output.innerHTML = "Error: " + error;
    }
}