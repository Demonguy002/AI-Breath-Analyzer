const mongoose = require("mongoose");

const sensorDataSchema = new mongoose.Schema({
  mq135: {
    type: Number,
    required: true
  },

  temperature: {
    type: Number,
    required: true
  },

  humidity: {
    type: Number,
    required: true
  },

  heartRate: {
    type: Number,
    required: true
  },

  spo2: {
    type: Number,
    required: true
  },

  createdAt: {
    type: Date,
    default: Date.now
  }
});

module.exports = mongoose.model("SensorData", sensorDataSchema);