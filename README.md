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
├── utils
│   ├── data_exploration.ipynb
│   └── dataloader.ipynb
├── models
│   ├── dataset.pth                  <-- Dataset loaded in from dataVisualiation.ipynb
│   └── best_models.pth              <-- TODO: 
├── dataVisualisation.ipynb          <-- Preliminary dataset investigation
├── knn.ipynb                        <-- Model 1: TODO: KNN
├── deeplab.ipynb                    <-- Model 2: Deeplab V3+
├── maskrcnn.ipynb                   <-- Model 3: TODO: TBD @Lxx156 @jxiong968 please merge your code thnx
├── yolo.ipynb                       <-- Model 4: TODO: Yolo Segmentation
└── turtles-data                     <-- Zip file from online dataset downloaded from Kaggle - DO NOT UPLOAD
    └── data
        ├── annotations.json
        ├── images
        ├── metadata.csv
        └── metadata_splits.csv
```

<br />

#### Setup Instructions:

---

1. Follow the file structure above to get this repo to work for you, if you have any questions or any cells don't run properly please let us know in the groupchat.
   
2. Please read through dataVisualisation.ipynb first and run through all the cells yourself to ensure you know what has been done and what hasn't yet been done. This section will be the part where we modify our dataset as we need to, so please make sure you run this and use this dataloader so we all use the same dataset for consistency.

3. In particular, it is important to run the cell in "Dataset Cleanup & Re-validation" as this will create a new json for us with the cleaned up dataset (removal of all datapoints without turtle, which was found to have flaws during data exploration). 

4. Please remember to merge back everytime you finish a small feature and pull from main before you work.


<br />

#### Run Order for Markers : 

---

In order to run each cell in this repository, please follow the instructions below. If you are missing a module, please install it, all modules are available with pip install and do not require you to compile it yourself.

1. Follow the steps above to make sure you have the exact same tree structure in your local files as shown above. 

2. Investigate dataVisualisation.ipynb, where the steps we have taken to investigate the dataset occurs. Note that at the end, there will be a new updated_annotations.json file in place of the original. It is worth noting that some cells will render each and every photo of the dataset, so it is highly recommended to kill the cells after a few photos...

3. If all cells were executed correctly, note the creation of a new dataset.pth file inside of /models, which is where the processed dataset will be saved in. This will be used later to train ALL of the models.  

4. 