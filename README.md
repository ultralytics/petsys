<img src="https://storage.googleapis.com/ultralytics/UltralyticsLogoName1000×676.png" width="200">  

# Introduction

This directory contains software developed by Ultralytics LLC. For more information on Ultralytics projects please visit:
http://www.ultralytics.com/projects

# Description

The https://github.com/ultralytics/petsys repo contains analysis of gamma scatters on LYSO crystals coupled to SiPMs. This data was collected at PETSYS labs in Lisbon, Portugal in 2017. This code performs energy calibration and timing resolution analysis of the data.

# Requirements

[MATLAB](https://www.mathworks.com/products/matlab.html) >= 2018a with a common functions repo `$ git clone https://github.com/ultralytics/functions-matlab` added to the MATLAB path `>> addpath(genpath('/functions-matlab'))` and the following toolboxes:

- `Statistics and Machine Learning Toolbox`
- `Signal Processing Toolbox`

# Running

From MATLAB: `>> testSingles`

<img src="https://github.com/ultralytics/petsys/blob/master/results.png">

# Citation

[![DOI](https://zenodo.org/badge/126519968.svg)](https://zenodo.org/badge/latestdoi/126519968)

# Contact

Issues should be raised directly in the repository. For additional questions or comments please email Glenn Jocher at glenn.jocher@ultralytics.com or visit us at https://contact.ultralytics.com.
