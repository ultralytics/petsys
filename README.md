<img src="https://storage.googleapis.com/ultralytics/UltralyticsLogoName1000×676.png" width="200">

# Introduction ✨

Welcome to the official repository for PETsys analytics! This repo is your gateway to exploring gamma scatter analysis on LYSO crystals coupled to Silicon Photomultipliers (SiPMs). The data utilized here is the result of innovative research conducted at PETsys Electronics S.A. in Lisbon, Portugal in 2017. Our code facilitates detailed analysis, such as energy calibration and timing resolution, providing insights into the intricate world of PET (Positron Emission Tomography) systems.

# Description 📝

This repository—[ultralytics/petsys](https://github.com/ultralytics/petsys)—houses the analytical tools necessary to process and examine gamma scatter data on LYSO crystals. By visiting our repo, you will dive into sophisticated techniques employed to improve the performance of PET detectors, which have critical applications in medical imaging and beyond.

Our codebase is designed to be user-friendly, enabling both experts and enthusiasts to perform comprehensive energy calibration and evaluate timing resolution with the datasets provided.

# Requirements 🛠️

Before you begin, ensure you have the following prerequisites:

- [MATLAB](https://www.mathworks.com/products/matlab.html) version 2018a or later.
  
You will also need to include our common functions repository in your MATLAB environment:

```bash
$ git clone https://github.com/ultralytics/functions-matlab
```

Add the repository to your MATLAB path with:

```matlab
>> addpath(genpath('/functions-matlab'))
```

Don't forget the essential MATLAB toolboxes:
- `Statistics and Machine Learning Toolbox`
- `Signal Processing Toolbox`

# Running the Code 🏃‍♂️

To initiate the analysis, simply execute the following command from your MATLAB console:

```matlab
>> testSingles
```

Follow the prompts and watch as the software processes the data, leading up to a depiction of the analysis results similar to the image below.

<img src="https://github.com/ultralytics/petsys/blob/master/results.png" alt="Analysis Results Visualization">

# Citation 📖

If you find this repository helpful in your research or work, we encourage citing it using the DOI provided:

[![DOI](https://zenodo.org/badge/133869433.svg)](https://zenodo.org/badge/latestdoi/133869433)

# Contributing 🤝

Your contributions are what make this project thrive. For bug reports, feature requests, or discussions, please open an issue directly in the repository. We value your input and are keen to collaborate with you to enhance this project further.

# License 🔒

This project is released under the AGPL-3.0 license. Please refer to the `LICENSE` file for more details.

# Connect with Us 🌐

While direct email support is not available, we warmly welcome you to our community here on GitHub. We encourage you to participate in issues for any discussions, questions, or feedback. Moreover, visit us at our homepage for more exciting projects and updates from Ultralytics!

Join the journey to advancing PET imaging technology. Let's innovate together! 🚀
