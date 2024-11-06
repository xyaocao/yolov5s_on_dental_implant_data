# Implant detection using Yolov5 model
Data preparation, training model, detection result all under Data_yolov5 folder.

## Data preparation
Under data folder has the original dataset with yolov5 format. Using split_train_test.py to split the training/testing dataset, 80%(212 images) for training, 20%(53 images) for testing.
training dataset is under train folder, testing dataset is under test folder. All the images are the same size: 340 * 410 (Width * height)

## Training Yolov5s model
This section is under the training_yolov5 folder.
Added several yolov5 files to help train our dataset. 
Details in the file yolov5s_training.ipynb to show the steps to train Yolov5s model to detect crown and screw and draw corresponding bounding box. The trained yolov5s model is under the training_yolov5/runs/exp0_yolov5s_pre/weights folder, took 14.858 hours to finish this training.

## Detection result
This section is under the detection_result folder.
Using the trained model in the detect_bounding box.ipynb file to detect on the test and train data seperately, generated two folders under inference path. The test_output and train_output folder include images with bounding box and .txt file which includes bouding box information in yolo format.

I changeed the yolo format into pixel format and saved it under the bounding_boxes folder. 

## If you only want to get the images with bounding box infomation, then check the detection_result/bounding_boxes folder, it has everything you need, coordinates for screw/crown, also images show you the bounding box.


