import os
from pycocotools.coco import COCO
from pycocotools import mask as maskUtils
from pathlib import Path
import numpy as np
import cv2  # Make sure OpenCV is installed for contour extraction

# Load the COCO dataset
coco = COCO("./turtles-data/data/updated_annotations.json")

# Define paths
labels_dir = "./turtles-data/labels/"
Path(labels_dir).mkdir(
    parents=True, exist_ok=True
)  # Create the directory if it doesn't exist

# Get category IDs and create a mapping for YOLO class IDs
category_ids = coco.getCatIds()
categories = coco.loadCats(category_ids)
category_mapping = {cat["id"]: idx for idx, cat in enumerate(categories)}

# Iterate over all images in the dataset
image_ids = coco.getImgIds()
for image_id in image_ids:
    # Load image information
    image_info = coco.loadImgs(image_id)[0]
    img_width, img_height = image_info["width"], image_info["height"]
    image_name = Path(image_info["file_name"]).stem

    # Get all annotations for the current image
    ann_ids = coco.getAnnIds(imgIds=image_id)
    annotations = coco.loadAnns(ann_ids)

    # Initialize a list to hold YOLO-format data for this image
    yolo_annotations = []

    for ann in annotations:
        category_id = ann["category_id"]
        yolo_class_id = category_mapping[category_id]

        if "segmentation" in ann and ann["segmentation"]:
            if (
                isinstance(ann["segmentation"], dict)
                and "counts" in ann["segmentation"]
            ):
                # Handle unencoded RLE format by encoding it first
                rle = maskUtils.frPyObjects(ann["segmentation"], img_height, img_width)
                binary_mask = maskUtils.decode(rle)  # Decode the RLE to binary mask

                # Find contours from the binary mask
                contours, _ = cv2.findContours(
                    binary_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
                )

                for contour in contours:
                    if (
                        len(contour) >= 3
                    ):  # Ensure it has at least 3 points to form a polygon
                        yolo_format_points = []
                        for point in contour:
                            x, y = point[0]
                            x_normalized = x / img_width
                            y_normalized = y / img_height
                            yolo_format_points.extend([x_normalized, y_normalized])

                        # Add the class ID at the beginning of the line, followed by the points
                        yolo_annotations.append(
                            f"{yolo_class_id} " + " ".join(map(str, yolo_format_points))
                        )

        elif "bbox" in ann:
            # Fallback to bounding box if no segmentation (bbox format: [x_min, y_min, width, height])
            bbox = ann["bbox"]
            x_center = (bbox[0] + bbox[2] / 2) / img_width
            y_center = (bbox[1] + bbox[3] / 2) / img_height
            width = bbox[2] / img_width
            height = bbox[3] / img_height

            # Format as YOLO bounding box: [class_id, x_center, y_center, width, height]
            yolo_annotations.append(
                f"{yolo_class_id} {x_center} {y_center} {width} {height}"
            )

    # Write annotations to YOLO format file
    label_file_path = os.path.join(labels_dir, f"{image_name}.txt")
    with open(label_file_path, "w") as f:
        f.write("\n".join(yolo_annotations))
