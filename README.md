# Bird Vocalization Classification

## Overview
This repository contains code and data for the AI Capstone Project on bird vocalization classification. The project applies supervised and unsupervised learning methods to classify bird species based on their vocalizations. The dataset is sourced from [Xeno-canto](https://xeno-canto.org/), and features extraction is performed using Mel-Frequency Cepstral Coefficients (MFCCs).

## Repository Structure
```
.
│── data_download.ipynb    # Jupyter Notebook for downloading the dataset
│── data/                  # Contains the audio dataset (4 ZIP files of WAV files)
│   │── species1.zip
│   │── species2.zip
│   │── species3.zip
│   │── species4.zip
│── 111550182/             # User own traing code included
│── 110550205/
│── README.md
```

## Dataset
The `data/` folder contains ZIP files, each corresponding to a bird species. These files must be extracted before running the scripts.

## References
- Xeno-canto: [https://xeno-canto.org/](https://xeno-canto.org/)

