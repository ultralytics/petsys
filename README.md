<img src="https://storage.googleapis.com/ultralytics/UltralyticsLogoName1000×676.png" width="200">

## :sparkles: Introduction

Welcome to Ultralytics! We are thrilled to share our software with you. Ultralytics LLC is a dynamic team of experts committed to delivering cutting-edge analytical solutions. To explore more of our innovative projects, please check out our [website](http://www.ultralytics.com/projects).

## :page_with_curl: Project Description

The [ultralytics/petsys](https://github.com/ultralytics/petsys) repository is dedicated to the analysis of gamma scatter interactions within LYSO crystals connected to Silicon Photomultipliers (SiPMs). The experimental data we use was meticulously gathered at PETSYS labs in Lisbon, Portugal, back in 2017. Our codebase is designed to perform sophisticated tasks, such as energy calibration and timing resolution analysis on this dataset.

## :hammer_and_wrench: Requirements

Before you dive into running the software, ensure you have the following prerequisites fulfilled:

1. [MATLAB](https://www.mathworks.com/products/matlab.html) (version 2018a or later).
2. Clone our common functions repository with the following command:
   ```bash
   git clone https://github.com/ultralytics/functions-matlab
   ```
   Once cloned, add the repo to your MATLAB path using:
   ```matlab
   addpath(genpath('/path/to/functions-matlab'))
   ```
   Replace `/path/to/` with the directory where you've cloned the repo.
3. Ensure that you have the necessary MATLAB toolboxes installed:
   - `Statistics and Machine Learning Toolbox`
   - `Signal Processing Toolbox`

## :running: How to Run the Code

To initiate the analysis within MATLAB, simply execute the `testSingles` script by entering the following command in your MATLAB command window:
```matlab
>> testSingles
```
When you run this script, MATLAB will process the data according to the algorithms defined in our codebase, and you will be able to observe the results firsthand!

<img src="https://github.com/ultralytics/petsys/blob/master/results.png" alt="Analysis Results">

## :bookmark_tabs: Citation

If our project contributes to your research or if you find the dataset and code useful, please consider citing our work using the Zenodo DOI badge below:

[![DOI](https://zenodo.org/badge/133869433.svg)](https://zenodo.org/badge/latestdoi/133869433)

## :bell: Stay Connected

If you encounter any issues or have queries, please feel free to raise them directly in the repository under the *Issues* section. Although we do not provide direct contact via email, Ultralytics offers a dedicated [contact platform](https://contact.ultralytics.com) where we are more than happy to assist you.

---

**License:**

This project is distributed under the AGPL-3.0 license. Please ensure you comply with the terms of the license when using or modifying the code. 

**Acknowledgements:**

We would like to extend our gratitude to the researchers and staff at PETSYS labs for their valuable contributions to the dataset and their collaboration in this project.

Enjoy exploring and analyzing gamma scatters with Ultralytics!
