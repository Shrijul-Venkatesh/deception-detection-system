# Deception detection system using micro-expression and verbal cue analysis

## Overview

This system combines the realms of understanding and classifying micro-expressions using deep learning and computer vision techniques as well as extracting features from verbal cues using Mel Frequency Cepstrum Coefficient (MFCC) based systems, to detect signs of deception in individuals.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Dataset](#dataset)
- [Contributing](#contributing)
- [License](#license)

## Features

- Utilizes MATLAB based functions to perform MFCC extraction on the audio files

## Installation

This project makes use of the MATLAB software. You can install the software [here](https://www.mathworks.com/help/install/ug/install-products-with-internet-connection.html). Also note, MATLAB is pay-to-use software. However, it also has a 30 day free trial which you can make use of, for the sake of this project

To install the necessary python dependencies, you can use pip:

```bash
pip install -r requirements.txt

```

The audio engine also requires a MATLAB add-on called "Audio Toolbox". To add this add-on to MATLAB, follow the given steps:

- Open MATLAB
- Go to the "Add-Ons" menu
- Select "Get Add-Ons"
- Search for "Audio Toolbox"
- Click on "Install" to install the toolbox

After installing the necessary software, the MU3D dataset must be installed, which can be found [here](https://sc.lib.miamioh.edu/handle/2374.MIA/6067). Although the dataset is licensed under the Creative Commons License, it is required to send a usage agreement to the owner of the dataset Emily Paige Lloyd (Miami University) in order to gain access to the dataset. Once authorized, download the dataset into the same parent directory as the project and split the videos into 2 folders, namely the "audio_set" and the "video_set", by running the extract_audio.py file.

create a new empty csv file called mfcc_features.csv in the deception-detection-engine folder
move the extract_audio.py to the MU3D-Package folder and then execute
