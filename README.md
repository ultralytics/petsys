<img src="https://storage.googleapis.com/ultralytics/UltralyticsLogoName1000×676.png" width="200">  

# Ultralytics PETSYS Analysis Project README 📈

## Introduction

Welcome to the Ultralytics PETSYS Analysis Project repository! This project focuses on the analysis of gamma scatter events on LYSO crystals coupled to Silicon Photomultipliers (SiPMs). The data for this analysis was meticulously collected at PETSYS Electronics's testing labs in Lisbon, Portugal, during the year 2017. We aim to delve into energy calibration and timing resolution analysis to extract insightful information from the experimental data, which is pivotal for advancements in the field of particle physics and medical imaging technologies.

## Project Description 📊

This repository, [ultralytics/petsys](https://github.com/ultralytics/petsys), is home to a sophisticated analysis workflow for processing experimental gamma scatter data. It includes MATLAB scripts capable of performing energy calibration and determining the timing resolution of LYSO crystal and SiPM assemblies. By utilizing this codebase, researchers can better understand the response of these detector systems under varying experimental conditions.

## Requirements 🛠️

To successfully run the code in this repository, you will need:

- [MATLAB](https://www.mathworks.com/products/matlab.html) version 2018a or later.
- Access to the common functions repo via `$ git clone https://github.com/ultralytics/functions-matlab`, and subsequently adding it to the MATLAB path through the command `>> addpath(genpath('/functions-matlab'))`.

Additionally, ensure that the following MATLAB toolboxes are installed:
- `Statistics and Machine Learning Toolbox`
- `Signal Processing Toolbox`

## Running the Analysis 🔍

To execute the analysis, navigate to MATLAB's command window and enter: 

```matlab
>> testSingles
```

This command initiates the script that processes the experimental data, resulting in output that visualizes the energy calibration and timing resolution.

Here's a glimpse of the kind of results you can expect to generate:

<img src="https://github.com/ultralytics/petsys/blob/master/results.png">

## Citation 📑

If you use this project's code or data for your research, please consider citing it:

[![DOI](https://zenodo.org/badge/133869433.svg)](https://zenodo.org/badge/latestdoi/133869433)

This work is licensed under the AGPL-3.0 License. Please verify the [LICENSE](https://github.com/ultralytics/petsys/blob/master/LICENSE) for more details.

## Support ✉️

For any issues, queries, or suggestions regarding this repository, please utilize the [GitHub Issues](https://github.com/ultralytics/petsys/issues) section. We strive to address your feedback with promptness and accuracy.

For additional information or other inquiries, kindly visit our contact page at https://contact.ultralytics.com — we're here to help!

###### Please note: The information in this README is relevant up to the knowledge cutoff date, and it will be maintained to integrate any subsequent significant developments.
