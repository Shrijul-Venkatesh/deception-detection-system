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
