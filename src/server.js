import express from "express";
import dotenv from "dotenv";
import inputRoutes from "./routes/input.js";
import renderRoutes from "./routes/render.js";
import uploadRoutes from "./routes/upload.js";
import postRoutes from "./routes/post.js";

dotenv.config();

const app = express();
app.use(express.json({ limit: "30mb" }));
app.use(express.urlencoded({ extended: true }));

app.use("/input", inputRoutes);
app.use("/render", renderRoutes);
app.use("/upload", uploadRoutes);
app.use("/post", postRoutes);

app.get("/", (req, res) => {
  res.json({ status: "NΞØ FlowOFF NodeMello RUNNING" });
});

const PORT = process.env.PORT || 3001;
app.listen(PORT, () => {
  console.log(`SERVER ONLINE ∆ PORT ${PORT}`);
});

