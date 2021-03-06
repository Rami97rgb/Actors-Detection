# Actors-Detection
* Made an app that given a video sequence, it processes it and ouputs another video with actors detections and timestamps of these detections.
* This app uses the YOLOv4 object detector that has been trained on the Darkenet deep learning framework, and for inference, the OpenCV dnn module has been used.
* The model can be easily retrained for the purpose of detecting other objects.

## Data Collection
Three Classes of images have been manually collected and then labeled using LabelImg. The dataset was later uploaded to Roboflow for preprocessing and to make it easily accessible later for training.

## Training
* I used the Darknet deep learning framework because it is fast, GPU accelerated and flexible, but most importantly it is a low level framework that provides a good understanding of how neural nets work.
* I choose the YOLOv4 object detector because, although it is relatively slow, it is also one of the best performing ones: This is perfectly adequate for our use case since our app does not run in real-time. To get a better understanding of the algorithm I recommend reading The original YOLO and the new YOLOv4 research papers linked in the resources bellow.
* The model has been trained on a Google Colab GPU for about 8 hours using pretrained YOLOv4 weights.

## Inference
The OpenCV computer vision library and its dnn module have been used to process images and videos for detections and make timestamps for detections.

Here is a sample of the video after the detections have been overlayed:

![](https://github.com/Rami97rgb/Actors-Detection/blob/master/images/act1.png)

And some timestamps:

![](https://github.com/Rami97rgb/Actors-Detection/blob/master/images/act2.png)

## Usage
For videos:

`python yolo_video.py --input videos/in_video_name.mp4 --output output/out_video_name.avi --yolo yolo-coco`

For images:

`python yolo.py --image images/img_name.jpg --yolo yolo-coco`

## Resources:
Training: https://blog.roboflow.com/training-yolov4-on-a-custom-dataset/

Inference: https://www.pyimagesearch.com/2018/11/12/yolo-object-detection-with-opencv/

Original YOLO paper: https://arxiv.org/abs/1506.02640

YOLOv4 paper: https://arxiv.org/abs/2004.10934
