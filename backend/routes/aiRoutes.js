const express = require("express");
const router = express.Router();

const SensorData = require("../models/SensorData");

const { spawn } = require("child_process");
const path = require("path");

router.get("/latest", async (req, res) => {
  try {

    const latest = await SensorData.findOne()
      .sort({ createdAt: -1 });

    if (!latest) {
      return res.status(404).json({
        success: false,
        message: "No sensor data found"
      });
    }

    const python = spawn(
      "python",
      [
        path.join(__dirname, "../ai/predict.py"),
        JSON.stringify({
          mq135: latest.mq135,
          temperature: latest.temperature,
          humidity: latest.humidity,
          heartRate: latest.heartRate,
          spo2: latest.spo2
        })
      ]
    );

    let result = "";

    python.stdout.on("data", (data) => {
      result += data.toString();
    });

    python.stderr.on("data", (data) => {
      console.error(data.toString());
    });

    python.on("close", () => {

      const prediction = JSON.parse(result);

      res.json({
        success: true,
        sensorData: latest,
        prediction
      });

    });

  } catch (error) {

    res.status(500).json({
      success: false,
      error: error.message
    });

  }
});

module.exports = router;