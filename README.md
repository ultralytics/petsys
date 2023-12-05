<img src="https://storage.googleapis.com/ultralytics/UltralyticsLogoName1000×676.png" width="200">

# Introduction 👋

Welcome to the Ultralytics repository! Here you'll find a collection of innovative software developed by our talented team at Ultralytics. If you're curious about our other projects and endeavors, head over to our website: [Ultralytics Projects](http://www.ultralytics.com/projects).

# Project Description 📖

The [Ultralytics PETsys](https://github.com/ultralytics/petsys) repository is dedicated to the analysis of gamma scatter interactions involving LYSO crystals and Silicon Photomultipliers (SiPMs). The insightful dataset that forms the basis of this analysis was acquired during experiments at the PETSYS Electronics laboratory in Lisbon, Portugal, back in 2017.

In this repository, you will find MATLAB code capable of conducting precise energy calibration and timing resolution analysis. Whether you're a researcher in medical imaging technology or simply curious about PET systems, this repository provides valuable tools for understanding the intricacies of scintillation events and detector response.

# Requirements 🛠

To get started with the provided analysis code, you'll need [MATLAB](https://www.mathworks.com/products/matlab.html) version 2018a or later. Ensure you also have the following toolboxes installed:

- `Statistics and Machine Learning Toolbox`
- `Signal Processing Toolbox`

Additionally, clone our common functions repository and add it to your MATLAB path for full functionality:

```sh
$ git clone https://github.com/ultralytics/functions-matlab
```

Then, in MATLAB, run:

```matlab
>> addpath(genpath('/functions-matlab'))
```

# Running the Analysis 🏃

To perform the analysis, simply start MATLAB and execute the following command:

```matlab
>> testSingles
```

As the code runs, it will process the data and perform the required analytical tasks to generate a results visualization.

Here is an example of the output you can expect:

![Analysis Results](https://github.com/ultralytics/petsys/blob/master/results.png)

# Citation 📚

If you find this analysis tool useful in your research or wish to refer to it in your publications, please use the following citation:

[![DOI](https://zenodo.org/badge/133869433.svg)](https://zenodo.org/badge/latestdoi/133869433)

# Get In Touch 📬

We encourage contributions and feedback! If you encounter any issues or have any suggestions, please file them under the repository's [Issues section](https://github.com/ultralytics/petsys/issues).

For further inquiries, feel free to explore our [Contact Page](https://contact.ultralytics.com) (please note, email contact is not available).

Happy Analyzing!

---

**Note:** All Ultralytics repositories adhere to the AGPL-3.0 license (Affero General Public License), which guarantees your freedom to share and change all versions of the program--to make sure it remains free software for all its users. Hence, any references to other licenses are corrected to AGPL-3.0.
