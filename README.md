<img src="https://storage.googleapis.com/ultralytics/UltralyticsLogoName1000×676.png" width="200">  

# Introduction

This directory contains software developed by Ultralytics LLC. For more information on Ultralytics projects please visit:
http://www.ultralytics.com  

# PETSYS

The https://github.com/ultralytics/petsys repo contains analysis of gamma scatters on LYSO crystals coupled to SiPMs. This data was collected at PETSYS labs in Lisbon, Portugal in 2017. This code performs energy calibration and timing resolution analysis of the data.

# Requirements

MATLAB with the following toolbox installed:  

- ```Statistics and Machine Learning Toolbox```
- ```Signal Processing Toolbox```

Ultralytics MATLAB common functions must also be cloned and added to the MATLAB path:

1. From a shell: ```$ git clone https://github.com/ultralytics/matlab-common```
2. From MATLAB Command Window: ```>> apppath(genpath('/matlab-common'))```

# Running PETSYS analysis
Run ```testSingles.m``` in MATLAB.

![Alt](https://github.com/ultralytics/petsys/results.png "results")

# Contact

For questions or comments please contact Glenn Jocher at glenn.jocher@ultralytics.com or visit us at http://www.ultralytics.com/contact
