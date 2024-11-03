# SeaTurtleID2022

COMP9517 Group Project

Checkout to your own branch to work individually. It is actually really hard to merge conflicted versions of jupyter notebook, so please immediately merge back to main when done and rebase your own branch regularly! Use git fetch to get updates for all branches. For git tools, I highly recommend https://git-fork.com/

Do not upload the dataset and any other unnecessary files. For consistency, please make the file structure of this project looks like this:

```
.
├── README.md
├── utils
│   ├── data_exploration.ipynb
│   └── dataloader.ipynb
├── train.ipynb
└── turtles-data                     <-- Zip file from online dataset downloaded from Kaggle
    └── data
        ├── annotations.json
        ├── images
        ├── metadata.csv
        └── metadata_splits.csv
```

Setup Instructions:

1. Follow the file structure above to get this repo to work for you, if you have any questions or any cells don't run properly please let us know in the groupchat.
   
2. Please read through train.ipynb first and run through all the cells yourself to ensure you know what has been done and what hasn't yet been done. This will be the single notebook where we will implement all our code and train our models.

3. It is also equally important to run the cell in "Dataset Cleanup & Re-validation" as this will create a new json for us with the cleaned up dataset (removal of all datapoints without turtle, which was found to have flaws during data exploration).

4. Please remember to merge back everytime you finish a small feature and pull from main before you work.