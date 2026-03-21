async function analyze() {

    const resume = document.getElementById("resume").value;
    const jobRole = document.getElementById("jobRole").value;

    const loader = document.getElementById("loader");
    const output = document.getElementById("output");

    // Show loader
    loader.style.display = "block";
    output.innerText = "";

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

        // Handle backend errors
        if (!response.ok) {
            const text = await response.text();
            throw new Error(text);
        }

        const data = await response.json();

        // Hide loader
        loader.style.display = "none";

        // Show result nicely
        output.innerText = 
            "Skills: " + data.skills + "\n\n" +
            "Missing Skills: " + data.missing_skills + "\n\n" +
            "Roadmap: " + data.roadmap + "\n\n" +
            "Score: " + data.score;

    } catch (error) {
        loader.style.display = "none";
        output.innerText = "Error: " + error.message;
    }
}