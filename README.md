# SeaTurtleID2022

<br />

#### COMP9517 Group Project

---

Checkout to your own branch to work individually. It is actually really hard to merge conflicted versions of jupyter notebook, so please immediately merge back to main when done and rebase your own branch regularly! Use git fetch to get updates for all branches. For git tools, I highly recommend https://git-fork.com/

Do not upload the dataset and any other unnecessary files. For consistency, please make the file structure of this project looks like this:

<br />


```
.
├── README.md
├── models
│   ├── dataset.pth                  <-- Dataset loaded in from dataVisualiation.ipynb
│   └── best_models.pth              <-- TODO: Save best models here.
│
├── turtles-data                     <-- Zip file from online dataset downloaded from Kaggle - DO NOT UPLOAD
│   └── data
│       ├── annotations.json
│       ├── images
│       ├── metadata.csv
│       └── metadata_splits.csv
│
├── utils
│   ├── COCO2YOLO.py
│   ├── data_exploration.ipynb
│   ├── dataloader.ipynb
│   └── drawAndTest.py
│
├── yolo-dataset
│   ├── images
│   │   ├── train
│   │   └── test
│   ├── labels
│   │   ├── train
│   │   └── test
│   └── seaturtle-seg.yaml
│
├── dataVisualisation.ipynb          <-- Preliminary dataset investigation
├── knn.ipynb                        <-- Model 1: TODO: KNN
├── deeplab.ipynb                    <-- Model 2: Deeplab V3+
├── maskrcnn.ipynb                   <-- Model 3: Mask R-CNN
├── yolo.ipynb                       <-- Model 4: YOLOv8-Segmentation
└──
```

<br />

#### Setup Instructions:

---

1. Follow the file structure above to get this repo to work for you, if you have any questions or any cells don't run properly please let us know in the groupchat.
   
2. Please read through dataVisualisation.ipynb first and run through all the cells yourself to ensure you know what has been done and what hasn't yet been done. This section will be the part where we modify our dataset as we need to, so please make sure you run this and use this dataloader so we all use the same dataset for consistency.

3. In particular, it is important to run the cell in "Dataset Cleanup & Re-validation" as this will create a new json for us with the cleaned up dataset (removal of all datapoints without turtle, which was found to have flaws during data exploration). 

4. Please remember to merge back everytime you finish a small feature and pull from main before you work.


<br />

#### Run Order : 

---

In order to run each cell in this repository, please follow the instructions below. If you are missing a module, please install it, all modules are available with pip install and do not require you to compile it yourself.

1. Follow the steps above to make sure you have the exact same tree structure in your local files as shown above. 

2. Investigate dataVisualisation.ipynb, where the steps we have taken to investigate the dataset occurs. Note that at the end, there will be a new updated_annotations.json file in place of the original. It is worth noting that some cells will render each and every photo of the dataset, so it is highly recommended to kill the cells after a few photos...

3. Make sure to keep the split dataset as defined in the open-set splitting of the dataset into training, validation, and test subsets as defined by the creators in the metadata.

4. Each model can act separately once dataVisualisation.ipynb has finished running.