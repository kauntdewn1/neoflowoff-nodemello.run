import express from "express";
import { distribute } from "../distributor/router.js";

const router = express.Router();

router.post("/", async (req, res) => {
  try {
    const result = await distribute(req.body);
    res.json({ ok: true, result });
  } catch (err) {
    res.status(500).json({ ok: false, error: err.message });
  }
});

export default router;

