document.addEventListener("DOMContentLoaded", () => {
    const btn = document.getElementById("getResultBtn");
    const resultsDiv = document.getElementById("results");

    btn.addEventListener("click", async () => {
        const gender = document.getElementById("gender").value;
        const personality = document.getElementById("personality").value;

        const response = await fetch("http://127.0.0.1:8003/results", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ gender, personality })
        });

        const data = await response.json();

        // Clear previous
        resultsDiv.innerHTML = "";

        // Helper to render dict
        /*const renderDict = (title, dict) => {
            const html = `
                <h3>${title}</h3>
                <ul>${Object.entries(dict).map(([k, v]) => `<li>${k} (DLC: ${v})</li>`).join('')}</ul>
            `;
            resultsDiv.innerHTML += html;
        };*/

        const renderDictList = (title, itemList) => {
            const html = `
                <h3>${title}</h3>
                <div class="item-grid">
                    ${itemList.map(item => `
                        <div class="item-card">
                            <img src="${item.image}" alt="${item.name}" /*width="50" height="50"*/>
                            <p><strong>${item.name}</strong></p>
                            <p>DLC: ${item.dlc}</p>
                        </div>
                    `).join('')}
                </div>
            `;
            resultsDiv.innerHTML += html;
        };

        renderDictList("Foods", data.foods);
        renderDictList("Snacks", data.snacks);
        renderDictList("Characters", data.characters);
        renderDictList("Characters with Unknown Personality", data.unknown_personality_characters);
    });
});