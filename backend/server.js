const express = require("express");
const cors = require("cors");
const dotenv = require("dotenv");

dotenv.config();

const connectDB = require("./config/db");

const sensorRoutes = require("./routes/sensorRoutes");
const aiRoutes = require("./routes/aiRoutes");

connectDB();

const app = express();

app.use(cors());
app.use(express.json());

app.use("/api/sensor", sensorRoutes);
app.use("/api/ai", aiRoutes);

app.get("/", (req, res) => {
  res.send("AI Breath Analyzer Backend Running 🚀");
});

const PORT = process.env.PORT || 5000;

app.listen(PORT, "0.0.0.0", () => {
  console.log(`Server running on port ${PORT}`);
});