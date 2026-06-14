const express = require("express");
const router = express.Router();

const SensorData = require("../models/SensorData");

// POST Sensor Data
router.post("/", async (req, res) => {

  console.log("Received Sensor Data:");
  console.log(req.body);

  try {
  

    const sensorData = await SensorData.create({
      mq135: req.body.mq135,
      temperature: req.body.temperature,
      humidity: req.body.humidity,
      heartRate: req.body.heartRate,
      spo2: req.body.spo2
    });

    res.status(201).json({
      success: true,
      data: sensorData
    });

  } catch (error) {

    res.status(500).json({
      success: false,
      error: error.message
    });

  }
});

// GET Last 20 Records
router.get("/", async (req, res) => {
  try {

    const data = await SensorData.find()
      .sort({ createdAt: -1 })
      .limit(20);

    res.status(200).json({
      success: true,
      data
    });

  } catch (error) {

    res.status(500).json({
      success: false,
      error: error.message
    });

  }
});

// GET Latest Record
router.get("/latest", async (req, res) => {
  try {

    const latest = await SensorData.findOne()
      .sort({ createdAt: -1 });

    res.status(200).json({
      success: true,
      data: latest
    });

  } catch (error) {

    res.status(500).json({
      success: false,
      error: error.message
    });

  }
});

module.exports = router;