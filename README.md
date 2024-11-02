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