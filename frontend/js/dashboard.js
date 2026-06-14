const API_URL = "http://localhost:5000/api/sensor/latest";

async function loadSensorData() {

    try {

        const response = await fetch(API_URL);

        const result = await response.json();
        const result = await response.json();

        console.log("API Response:");
        console.log(result);

        if (!result.success) {
            return;
        }

        const data = result.data;

        document.getElementById("heartRate").textContent =
            data.heartRate ? `${data.heartRate} BPM` : "--";

        document.getElementById("spo2").textContent =
            data.spo2 ? `${data.spo2}%` : "--";

        document.getElementById("temperature").textContent =
            data.temperature ? `${data.temperature} °C` : "--";

        document.getElementById("humidity").textContent =
            data.humidity ? `${data.humidity}%` : "--";

        document.getElementById("mq135").textContent =
            data.mq135 ?? "--";

        updateSensorColors(data);

    } catch (error) {

        console.error("API Error:", error);

        document.getElementById("deviceStatus").textContent =
            "Disconnected";
    }
}

function updateSensorColors(data) {

    const spo2Card =
        document.getElementById("spo2").parentElement;

    const heartCard =
        document.getElementById("heartRate").parentElement;

    if (data.spo2 >= 95) {
        spo2Card.style.borderLeft = "5px solid #10B981";
    }
    else if (data.spo2 >= 90) {
        spo2Card.style.borderLeft = "5px solid #F59E0B";
    }
    else {
        spo2Card.style.borderLeft = "5px solid #EF4444";
    }

    if (data.heartRate >= 60 && data.heartRate <= 100) {
        heartCard.style.borderLeft = "5px solid #10B981";
    }
    else {
        heartCard.style.borderLeft = "5px solid #EF4444";
    }
}

const startBtn =
document.getElementById("startAnalysisBtn");

if(startBtn)
{
    startBtn.addEventListener("click", () => {
        window.location.href = "analysis.html";
    });
}
console.log("Loading sensor data...");
loadSensorData();

setInterval(loadSensorData, 3000);