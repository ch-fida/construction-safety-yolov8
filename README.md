# Smart PPE Detector 🧢🦺 | YOLOv8 Model for Construction Safety Compliance

[![HF Space](https://img.shields.io/badge/Try%20Demo-HuggingFace-blue.svg)](https://huggingface.co/spaces/chfida/construction-safety-yolov8)

This project showcases a **YOLOv8-based object detection model** that identifies whether workers at a construction site are wearing **safety helmets (hats)** and **safety jackets** — a critical step in ensuring Personal Protective Equipment (PPE) compliance and minimizing site hazards.

---

## 🚀 Live Demo

Run the model directly in your browser using Hugging Face Spaces:

🔗 **Demo Link**: [Construction Safety Gear Detection](https://huggingface.co/spaces/chfida/construction-safety-yolov8)

📦 **Embed iFrame** (for blogs or dashboards):

```html
<iframe
  src="https://chfida-construction-safety-yolov8.hf.space"
  frameborder="0"
  width="100%"
  height="500">
</iframe>
```
## 📊 Dataset Overview

- Classes Detected:
    - 🧢 Helmet (Hat)
    - 🦺 Safety Jacket
- Instances:
    - 5000 per class for training
    - 3000 per class for validation
    - 2000 per class for testing
- Annotation Format: YOLO format

## 🧠 Model Summary

- Architecture: YOLOv8
- Training Epochs: 100
- Train Accuracy: 97%
- Train F1 Score: 96%
- Test Accuracy: 95%
- Test F1 Score: 93%

## ⚙️ How to Use
No installation required.

Simply open the demo on Hugging Face and upload an image. The app will return bounding boxes around detected hats and jackets, helping assess whether construction workers are wearing required PPE.

🔗 [Launch the Demo](https://huggingface.co/spaces/chfida/construction-safety-yolov8)

## 📁 Repository Contents

```bash
📦 construction-safety-yolov8
├── app.py             # Gradio app code (demo only)
├── README.md          # Project documentation
├── images             # Example Images
```
> **Note:**: This repository does not include model weights or local inference support. All inference runs in the cloud via Hugging Face Spaces.

## ✍️ Author
Fida Muhammad <br>
🔗 [Hugging Face](https://huggingface.co/chfida)<br>
🔗 [Hugging Face Space](https://huggingface.co/chfida/spaces)


## 📜 License
This project is licensed under the MIT License.
You are free to use, modify, and share the code for non-commercial and research purposes.

## 🙏 Acknowledgements
[Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics)<br>
[Gradio](https://www.gradio.app/)<br>
[Hugging Face Spaces](https://huggingface.co/spaces)