async function analyze() {
    const resume = document.getElementById("resume").value;
    const jobRole = document.getElementById("jobRole").value;
    const output = document.getElementById("output");
    const loader = document.getElementById("loader");

    if (!resume || !jobRole) {
        output.innerText = "⚠️ Please fill all fields!";
        return;
    }

    loader.style.display = "block";
    output.innerText = "";

    try {
        const response = await fetch("http://127.0.0.1:5000/analyze", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                resume: resume,
                job_role: jobRole
            })
        });

        const data = await response.json();

        loader.style.display = "none";

        const total = data.missing_skills.length + data.roadmap.length / 3;
        const match = Math.round((1 - data.missing_skills.length / total) * 100);

        output.innerText =
            "🎯 Match Score: " + data.match_score + "%\n\n" +
            "🧠 Skills Found:\n" + data.skills_found.join(", ") +
            "\n\n❌ Missing Skills:\n" + data.missing_skills.join(", ") +
            "\n\n📌 Roadmap:\n" + data.roadmap.join("\n");

    } catch (error) {
        loader.style.display = "none";
        output.innerText = "❌ Error connecting to backend";
    }
}