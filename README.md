# smart-surveillance-cv

🧠 Smart Surveillance System using Computer Vision

📌 Project Overview

This project implements a Smart Surveillance System using Computer Vision techniques.
The system analyzes video input to detect motion, identify humans, extract features, and track objects in real time.

It demonstrates a complete computer vision pipeline, covering fundamental to advanced concepts from the syllabus.

⸻

🎯 Objectives
- Perform image preprocessing and enhancement
- Detect motion in video streams
- Extract image features
- Detect humans using machine learning techniques
- Track moving objects
- Analyze motion using optical flow

⸻

🚀 Features
- 🎥 Real-time video processing
- 🟩 Motion detection using frame differencing
- 🔴 Optical flow for motion analysis
- 🔍 Feature extraction using ORB
- 🧍 Human detection using HOG
- 🆔 Basic object tracking with IDs
- 💾 Output video saving

🛠️ Tech Stack
- Python
- OpenCV
- NumPy

⸻

📁 Project Structure

smart-surveillance-cv/
│
├── src/
│   ├── main.py
│   ├── preprocessing.py
│   ├── motion.py
│   ├── detection.py
│   ├── features.py
│   ├── tracking.py
│
├── requirements.txt
├── README.md
└── report.pdf

⚙️ Installation & Setup

1. Clone the Repository
```bash
git clone https://github.com/your-username/smart-surveillance-cv
cd smart-surveillance-cv
```

2. Install Dependencies
```bash
pip install -r requirements.txt
```

▶️ How to Run

```bash
python src/main.py --input sample_video.mp4 --output result.mp4
```

Arguments:
- `--input` → Path to input video
- `--output` → Output video file (optional)

📸 Output

The system displays:
- Final processed video with detections
- Motion mask window
- Optical flow visualization

It also saves the output video file.

⸻

📊 Methodology

Step 1: Preprocessing
- Convert frames to grayscale
- Apply Gaussian blur

Step 2: Motion Detection
- Frame differencing
- Thresholding and contour detection

Step 3: Optical Flow
- Farneback method used for motion estimation

Step 4: Feature Extraction
- ORB (Oriented FAST and Rotated BRIEF)

Step 5: Object Detection
- HOG-based human detection

Step 6: Tracking
- Centroid-based tracking algorithm

⸻

📈 Results
- Successfully detects motion and humans in video
- Tracks moving objects with IDs
- Visualizes motion using optical flow
- Works in real-time on standard videos

⸻

⚠️ Limitations
- Basic tracking (no re-identification)
- HOG detector may miss small/distant humans
- Performance depends on video quality

📄 Project Report

A detailed report explaining methodology, results, and analysis is included in the repository.

⸻

👨‍💻 Author

Milin Patel  
B.Tech CSE (AI & ML)  
VIT Bhopal University