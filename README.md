# SeaTurtleID2022

<br />

#### COMP9517 Group Project

---

Checkout to your own branch to work individually. It is actually really hard to merge conflicted versions of jupyter notebook, so please immediately merge back to main when done and rebase your own branch regularly! Use git fetch to get updates for all branches. For git tools, I highly recommend https://git-fork.com/ (it's free!)

Do not upload the dataset and any other unnecessary files. For consistency, please make the file structure of this project looks like this:

<br />


```
.
├── README.md
├── requirements.txt                 <-- A list of all requirements to run this repository, PLEASE UPDATE!
│
├── models                           <-- Trained Models
│   ├── dataset.pth                  <-- Dataset loaded in from dataVisualiation.ipynb
│   ├── best_deeplab.pth             <-- Best Models : DeepLabV3+
│   ├── best_maskrcnn.pth            <-- Best Models : Mask R-CNN
│   └── best_YOLO.pt                 <-- Best Models : YOLO
│
├── turtles-data                     <-- File from online dataset downloaded from Kaggle - DO NOT UPLOAD
│   └── data
│       ├── annotations.json
│       ├── images
│       ├── metadata.csv
│       └── metadata_splits.csv
│
├── yolo-dataset                     <-- This will be automatically generated after running the yolo.ipynb notebook
│   ├── images
│   │   ├── train
│   │   └── test
│   ├── labels
│   │   ├── train
│   │   └── test
│   └── seaturtle-seg.yaml
│
├── dataVisualisation.ipynb          <-- Preliminary dataset investigation
├── knn.ipynb                        <-- Model 1: K-Nearest Neighbours
├── deeplab.ipynb                    <-- Model 2: Deeplab V3+
├── mask-rcnn.ipynb                  <-- Model 3: Mask R-CNN
└── yolo.ipynb                       <-- Model 4: YOLOv8-Segmentation
```

<br />

#### Setup Instructions:

---

1. Follow the file structure above to get this repo to work for you, if you have any questions or any cells don't run properly please let us know in the groupchat.

2. Run requirements.txt to install all the dependencies to get this repository fully functional. Do this with ```pip install -r requirements.txt ```
   
3. Please read through dataVisualisation.ipynb first and run through all the cells yourself to ensure you know what has been done and what hasn't yet been done. This section will be the part where we modify our dataset as we need to, so please make sure you run this and use this dataloader so we all use the same dataset for consistency.

4. In particular, it is important to run the cell in "Dataset Cleanup & Re-validation" as this will create a new json for us with the cleaned up dataset (removal of all datapoints without turtle, which was found to have flaws during data exploration). 
   
5. Make sure to keep the split dataset as defined in the open-set splitting of the dataset into training, validation, and test subsets as defined by the creators in the metadata! This is important as it was explicitly stated as a requirement in the specifications.

6. Please remember to merge back everytime you finish a small feature and pull from main before you work.


<br />

#### Run Order / Markers Guide : 

---

In order to travel through this repository to understand what has been done and for marking, please follow the instructions below.

1. Follow the steps above to make sure you have the exact same tree structure in your local files as shown above.
   
2. Install all the requirements, this can be done with ```pip install -r requirements.txt ```

3. Investigate dataVisualisation.ipynb, where the steps we have taken to investigate the dataset occurs. Note that at the end, there will be a new updated_annotations.json file in place of the original. It is worth noting that some cells will render each and every photo of the dataset (all 8000+ instances), so it is highly recommended to kill the cells after a few photos...

4. Each model can act separately once dataVisualisation.ipynb has finished running, so feel free to explore around with any of the four models included!