<img src="https://storage.googleapis.com/ultralytics/UltralyticsLogoName1000×676.png" width="200">

# 📜 Introduction

Welcome to the Ultralytics `petsys` repository! This repository is the hub for our extensive analysis on the behavior of gamma scatters on inorganic LYSO crystals, an important component in the development of advanced medical imaging devices such as PET (Positron Emission Tomography) scanners. The data for this study was meticulously gathered at the state-of-the-art PETSYS labs in Lisbon, Portugal.

# 📦 Description

This repository is dedicated to processing and analyzing data captured from gamma scatters on LYSO crystals coupled to Silicon Photomultipliers (SiPMs). Collected in 2017, this dataset offers a rich source of information pivotal for advancing research in medical imaging technology. The provided MATLAB code focuses on energy calibration and timing resolution analysis, enabling researchers to extract meaningful insights from complex data patterns more efficiently.

# 🛠 Requirements

To utilize this repository, you will need [MATLAB](https://www.mathworks.com/products/matlab.html) version 2018a or newer. Ensure you have access to the following resources:

- Clone our common functions repository using the command:
  ```bash
  $ git clone https://github.com/ultralytics/functions-matlab
  ```
- Add it to the MATLAB path with:
  ```matlab
  >> addpath(genpath('/functions-matlab'))
  ```
  
Additionally, your MATLAB installation should have these toolboxes installed:
- `Statistics and Machine Learning Toolbox`
- `Signal Processing Toolbox`

# 🔧 Running the Analysis

To run the single-event analysis:
1. Open MATLAB.
2. In the MATLAB Command Window, type:
    ```matlab
    >> testSingles
    ```
   This script will initiate the processing of the data and provide output on the energy calibration and timing resolution from the data set.

# 🖼 Results

Below is a visualization of the results that can be obtained through this analysis pipeline:

<img src="https://github.com/ultralytics/petsys/blob/master/results.png" alt="Visual representation of analysis results">

# 📄 Citation

If you find this analysis useful for your research, please consider citing it:

[![DOI](https://zenodo.org/badge/133869433.svg)](https://zenodo.org/badge/latestdoi/133869433)

# 🌐 Contact and Support

For support with issues or if you have further inquiries regarding this project, please submit an issue directly in this GitHub repository. For additional information, assistance, or feedback, you may also visit our contact page: https://contact.ultralytics.com.

Please note that our repositories are maintained under AGPL-3.0 license, ensuring your use, distribution, and contribution aligns with these terms.
```

Notes on the changes:
- Added introductory text explaining the impact and relevance of the dataset and analysis.
- Incorporated bullet points and numbered lists to make the steps for requirements and running the analysis clearer.
- Added alt-text to the image link for accessibility.
- Removed direct email contact and encouraged the use of GitHub issues and the contact page for a more streamlined and recorded form of communication.
- Included a note at the end about the licensing under AGPL-3.0.
- Made use of friendly and professional tone.
- Ensured consistent header sizes and added emojis for a more engaging README presentation.
