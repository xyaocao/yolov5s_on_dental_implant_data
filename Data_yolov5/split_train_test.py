import supervision as sv
import shutil
import os

# Load dataset
ds = sv.DetectionDataset.from_yolo(
    images_directory_path="data/original/images/train",
    annotations_directory_path="data/original/labels/train",
    data_yaml_path="data_config.yaml"
)

# Split the dataset
train, test = ds.split(split_ratio=0.8, random_state=42, shuffle=True)

# Define directories for train and test datasets
train_images_dir = "data/train/images"
train_labels_dir = "data/train/labels"
test_images_dir = "data/test/images"
test_labels_dir = "data/test/labels"

# Create directories if they don't exist
os.makedirs(train_images_dir, exist_ok=True)
os.makedirs(train_labels_dir, exist_ok=True)
os.makedirs(test_images_dir, exist_ok=True)
os.makedirs(test_labels_dir, exist_ok=True)

# Function to copy images and labels separately
def copy_files(dataset, images_dir, labels_dir, annotations_source_dir):
    for image_path, _, _ in dataset:
        # Copy image file to the images directory
        if isinstance(image_path, str) and os.path.isfile(image_path):
            shutil.copy(image_path, images_dir)
        
        # Construct the label file path based on the image file name
        label_path = os.path.join(annotations_source_dir, os.path.basename(image_path).replace('.jpg', '.txt'))
        
        # Copy label file to the labels directory if it exists
        if os.path.isfile(label_path):
            shutil.copy(label_path, labels_dir)

# Copy train and test images/annotations to respective directories
copy_files(train, train_images_dir, train_labels_dir, "data/original/labels/train")
copy_files(test, test_images_dir, test_labels_dir, "data/original/labels/train")

# Print the sizes of the train and test datasets
print(len(train), len(test))
