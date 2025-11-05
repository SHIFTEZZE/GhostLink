import express from "express";
import multer from "multer";
import path from "path";
import fs from "fs";

const upload = multer({ dest: "uploads/" });
const app = express();

app.post("/upload", upload.single("audio"), (req, res) => {
  if (!req.file) return res.status(400).send("No file uploaded.");
  const fileUrl = `/uploads/${req.file.filename}`;
  res.json({ success: true, url: fileUrl });
});

app.use("/uploads", express.static(path.join(process.cwd(), "uploads")));
