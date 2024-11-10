import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import os

# Paths for single image and annotation
image_path = "./turtles-data/data/images/t001/anuJvqUqBB.JPG"
label_path = "./turtles-data/labels/anuJvqUqBB.txt"
output_dir = "./turtles-data/visualized/"
os.makedirs(output_dir, exist_ok=True)

# Load the image
image = plt.imread(image_path)
img_height, img_width = image.shape[:2]

# Create a plot with Matplotlib
fig, ax = plt.subplots()
ax.imshow(image)


# Helper function to draw a bounding box or polygon on the plot
def draw_yolo_annotation(
    ax, annotation, img_width, img_height, color="green", alpha=0.5
):
    parts = annotation.strip().split()
    class_id = int(parts[0])

    # Check if this annotation is a bounding box or a polygon
    if len(parts) == 5:
        # Bounding box
        x_center = float(parts[1]) * img_width
        y_center = float(parts[2]) * img_height
        width = float(parts[3]) * img_width
        height = float(parts[4]) * img_height

        # Calculate top-left corner
        x1 = x_center - width / 2
        y1 = y_center - height / 2

        # Add the rectangle as an overlay
        rect = patches.Rectangle(
            (x1, y1),
            width,
            height,
            linewidth=1,
            edgecolor=color,
            facecolor=color,
            alpha=alpha,
        )
        ax.add_patch(rect)
        ax.text(
            x1,
            y1 - 10,
            f"Class {class_id}",
            color="white",
            fontsize=10,
            weight="bold",
            backgroundcolor="black",
        )

    else:
        # Polygon (pairs of x, y coordinates)
        points = []
        for i in range(1, len(parts), 2):
            x = float(parts[i]) * img_width
            y = float(parts[i + 1]) * img_height
            points.append((x, y))

        # Draw the polygon
        polygon = patches.Polygon(
            points,
            closed=True,
            linewidth=1,
            edgecolor=color,
            facecolor=color,
            alpha=alpha,
        )
        ax.add_patch(polygon)
        if points:
            ax.text(
                points[0][0],
                points[0][1] - 10,
                f"Class {class_id}",
                color="white",
                fontsize=10,
                weight="bold",
                backgroundcolor="black",
            )


# Load and draw annotations
with open(label_path, "r") as f:
    annotations = f.readlines()

for annotation in annotations:
    draw_yolo_annotation(ax, annotation, img_width, img_height)

# Save and display the annotated image
output_path = os.path.join(output_dir, os.path.basename(image_path))
plt.savefig(output_path)
plt.show()
