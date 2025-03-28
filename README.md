<a href="https://www.ultralytics.com/"><img src="https://raw.githubusercontent.com/ultralytics/assets/main/logo/Ultralytics_Logotype_Original.svg" width="320" alt="Ultralytics logo"></a>

# 🚀 Introduction

Welcome to the official Ultralytics repository dedicated to analyzing gamma scatter interactions on Lutetium–Yttrium Oxyorthosilicate (LYSO) crystals. This project leverages Ultralytics' expertise in data-driven research to advance understanding in [particle physics](https://home.cern/science/physics) and imaging technology.

[![Ultralytics Actions](https://github.com/ultralytics/petsys/actions/workflows/format.yml/badge.svg)](https://github.com/ultralytics/petsys/actions/workflows/format.yml)
[![Ultralytics Discord](https://img.shields.io/discord/1089800235347353640?logo=discord&logoColor=white&label=Discord&color=blue)](https://discord.com/invite/ultralytics)
[![Ultralytics Forums](https://img.shields.io/discourse/users?server=https%3A%2F%2Fcommunity.ultralytics.com&logo=discourse&label=Forums&color=blue)](https://community.ultralytics.com/)
[![Ultralytics Reddit](https://img.shields.io/reddit/subreddit-subscribers/ultralytics?style=flat&logo=reddit&logoColor=white&label=Reddit&color=blue)](https://reddit.com/r/ultralytics)

## 📜 Description

Our goal is to push the boundaries of particle detection and imaging. This repository, [Ultralytics PETSYS](https://github.com/ultralytics/petsys), focuses on the detailed analysis of gamma scatter phenomena observed on LYSO crystals coupled with Silicon Photomultipliers (SiPMs). The dataset originates from PETSYS electronics in Lisbon, Portugal, collected in 2017. It forms the basis for our algorithms designed to perform energy calibration and assess the timing resolution of these sophisticated detection systems, crucial for applications like Positron Emission Tomography (PET).

## 📦 Requirements

To explore the intricacies of scintillation and photo-detection with our tools, you'll need specific software and toolboxes. Ensure you have [MATLAB](https://www.mathworks.com/products/matlab.html) version 2018a or newer installed. Additionally, certain MATLAB toolboxes focused on statistical analysis and signal processing are required.

Get started by:

1.  Cloning our common functions repository:
    ```bash
    git clone https://github.com/ultralytics/functions-matlab
    ```
2.  Adding the repository path to your MATLAB environment:
    ```matlab
    addpath(genpath('/path/to/functions-matlab')) % Replace /path/to/ with the actual directory
    ```
3.  Ensuring the following MATLAB toolboxes are installed:
    - `Statistics and Machine Learning Toolbox`
    - `Signal Processing Toolbox`

With these prerequisites met, you're ready for high-fidelity analysis!

## 🏃‍♀️ Running the Code

Initiating the analysis is simple. Execute the following command in your MATLAB console:

```matlab
testSingles  % This script starts the analysis of the gamma scatter dataset
```

The script will generate graphical outputs and insights, including visualizations like the one shown below:

<img src="https://raw.githubusercontent.com/ultralytics/petsys/main/results.png" alt="Gamma scatter analysis results visualization">

## 📑 Citation

If you find this dataset or our analysis tools beneficial for your research, please acknowledge our work by citing the DOI provided:

[![DOI](https://zenodo.org/badge/133869433.svg)](https://zenodo.org/badge/latestdoi/133869433)

## 🤝 Contribute

Contributions from the community are highly encouraged! Whether it's fixing bugs, proposing new features, or enhancing documentation, your input helps us improve. Please see our [Contributing Guide](https://docs.ultralytics.com/help/contributing/) for details on how to get started. We'd also appreciate hearing about your experience using Ultralytics products through our [Survey](https://www.ultralytics.com/survey?utm_source=github&utm_medium=social&utm_campaign=Survey). A heartfelt 🙏 thank you to all our contributors!

[![Ultralytics open-source contributors](https://raw.githubusercontent.com/ultralytics/assets/main/im/image-contributors.png)](https://github.com/ultralytics/ultralytics/graphs/contributors)

## ©️ License

Ultralytics provides two licensing options to accommodate diverse needs:

- **AGPL-3.0 License**: An [OSI-approved](https://opensource.org/license/agpl-v3) open-source license ideal for students and enthusiasts keen on contributing to open projects. See the [LICENSE](https://github.com/ultralytics/ultralytics/blob/main/LICENSE) file for details.
- **Enterprise License**: Designed for commercial applications, this license permits the integration of Ultralytics software and AI models into commercial products and services without the open-source stipulations of AGPL-3.0. For commercial use inquiries, please contact us via [Ultralytics Licensing](https://www.ultralytics.com/license).

## 📬 Contact Us

For bug reports, feature suggestions, and contributions, please visit [GitHub Issues](https://github.com/ultralytics/petsys/issues). For broader questions and discussions related to this project or other Ultralytics initiatives, join our active community on [Discord](https://discord.com/invite/ultralytics)!

<br>
<div align="center">
  <a href="https://github.com/ultralytics"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-github.png" width="3%" alt="Ultralytics GitHub"></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="3%" alt="space">
  <a href="https://www.linkedin.com/company/ultralytics/"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-linkedin.png" width="3%" alt="Ultralytics LinkedIn"></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="3%" alt="space">
  <a href="https://twitter.com/ultralytics"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-twitter.png" width="3%" alt="Ultralytics Twitter"></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="3%" alt="space">
  <a href="https://youtube.com/ultralytics"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-youtube.png" width="3%" alt="Ultralytics YouTube"></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="3%" alt="space">
  <a href="https://www.tiktok.com/@ultralytics"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-tiktok.png" width="3%" alt="Ultralytics TikTok"></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="3%" alt="space">
  <a href="https://ultralytics.com/bilibili"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-bilibili.png" width="3%" alt="Ultralytics BiliBili"></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="3%" alt="space">
  <a href="https://discord.com/invite/ultralytics"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-discord.png" width="3%" alt="Ultralytics Discord"></a>
</div>
