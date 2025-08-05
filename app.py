import gradio as gr
import torch
from collections import Counter
from ultralyticsplus import YOLO, render_result
from huggingface_hub import login, hf_hub_download
import os



# Log in to Hugging Face with your token
login(token=os.environ.get('Token', None))

torch.hub.download_url_to_file(
    'https://github.com/ch-fida/construction-safety-yolov8/blob/main/images/Example-1.jpg?raw=true', 'one.jpg')
torch.hub.download_url_to_file(
    'https://github.com/ch-fida/construction-safety-yolov8/blob/main/images/Example-2.jpg?raw=true', 'two.jpg')
torch.hub.download_url_to_file(
    'https://github.com/ch-fida/construction-safety-yolov8/blob/main/images/Example-3.jpg?raw=true', 'three.jpg')

def yoloV8_func(image: gr.Image = None,
                image_size: gr.Slider = 640,
                conf_threshold: gr.Slider = 0.4,
                iou_threshold: gr.Slider = 0.50):

    model = YOLO(hf_hub_download(repo_id=os.environ.get('Model', None), filename=os.environ.get('ID', None)))
    # Perform object detection on the input image using the YOLOv8 model
    results = model.predict(image,
                            conf=conf_threshold,
                            iou=iou_threshold,
                            imgsz=image_size)

    # Print the detected objects' information (class, coordinates, and probability)
    box = results[0].boxes

    # Render the output image with bounding boxes around detected objects
    render = render_result(model=model, image=image, result=results[0])
    # Detections = []
    # for x in box.cls.cpu().tolist():
    #     Detections.append(results[0].names[x])
    # det_str = "\n".join(Detections)
    Detections = [results[0].names[item] for item in box.cls.cpu().tolist()]
    counts = Counter(Detections)
    # Generate the sentence
    if not box.cls.cpu().tolist():
        result = "No detection."
    else:
        result = " and ".join([f"{count} {item}(s)" for item, count in counts.items()]) + " are detected."

    return render,result


inputs = [
    gr.Image(type="filepath", label="Input Image"),
    gr.Slider(minimum=320, maximum=1280, value=640,
                     step=32, label="Image Size"),
    gr.Slider(minimum=0.25, maximum=1.0, value=0.5,
                     step=0.05, label="Confidence Threshold"),
    gr.Slider(minimum=0.2, maximum=0.7, value=0.5,
                     step=0.05, label="IOU Threshold"),
]


outputs = [gr.Image(type="filepath", label="Output Image"),
           gr.Label()]

title = "Construction Safety Gear Detection using YOLOv8"


examples = [['one.jpg', 640, 0.3, 0.7],
            ['two.jpg', 800, 0.5, 0.6],
            ['three.jpg', 900, 0.4, 0.5]]

yolo_app = gr.Interface(
    fn=yoloV8_func,
    inputs=inputs,
    outputs=outputs,
    title=title,
    examples=examples,
    cache_examples=True,
)

# Launch the Gradio interface in debug mode with queue enabled
yolo_app.launch(debug=True, share=True,show_api=True,show_error=True)
