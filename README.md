<div align="center">
    <h2> Bridging the Reality Gap: A Benchmark for Physical Reasoning in General World Models with Various Physical Phenomena beyond Mechanics </h2>
</div>
Physics-RW benchmark is a physical reasoning dataset constructed from real-world videos. Encompassing a broad spectrum of real-world phenomena—mechanics, thermodynamics, electromagnetism, and optics—Physics-RW offers a comprehensive evaluation platform.

-----
## 0. Contents
- [0. Contents](#0-contents)
- [1. The Organized Structure of Dataset](#1-the-organized-structure-of-dataset)
- [2. Download Dataset](#2-download-dataset)
- [3. Benchmark Evaluate](#3-benchmark-evaluate)

## 1. The Organized Structure of Dataset <a id="1-the-organized-structure-of-dataset"></a>
The dataset is organized as follows.
```bash
# The data structure in the four folders, i.e., T1-T4, is the same. T1, T2, T3, and T4 represent tasks in mechanics, thermodynamics,
# electromagnetism, and optics, respectively.
-- Mechanics (T1)
    -- classification
        -- video/ # The folder for storing videos used for classification tasks.
        -- classification_en.json # The JSON file contains idx, video_path, the English version of the instruction, and prediction.
                                  # The value of prediction is empty, intended to store the model's output.
        -- classification_zh.json # Similar to the above file, but the instructions are in Chinese.

    -- video_generation
        -- video_gen/
            -- seen_video/ # The folder for storing videos input to the model.
            -- unseen_video/ # The folder for storing reference videos, i.e., subsequent videos.
        -- video_gen_en.json # The JSON file contains idx, video_path, label_path (i.e., the path of subsequent video),
                             # the English version of the instruction, and num_predicted_frame.
        -- video_gen_zh.json ## Similar to the above file, but the instructions are in Chinese.
-- Thermodynamics (T2)
    ...
-- Electromagnetism (T3)
    ...
-- Optics (T4)
    ...
```
## 2. Downloading the Physics-RW dataset <a id="2-download-dataset"></a>
Our data is stored in Physics-RW. Currently, only part of the data has been uploaded. Once the review process is complete, we will update all the data. 
**Dataset URL**: [https://www.modelscope.cn/datasets/pengyz/Physics-RW]

There are two methods for downloading:

2.1. Download via the ModelScope library.
```bash
from modelscope.msdatasets import MsDataset
ds =  MsDataset.load('pengyz/Physics-RW')
```
2.2. Download via GiT.
```
git clone https://www.modelscope.cn/datasets/pengyz/Physics-RW.git
```
## 3. Benchmark Evaluate <a id="benchmark-evaluate"></a>
We primarily evaluate existing methods based on accuracy (ACC), F1 score, and Fréchet Video Distance (FVD) metrics. Considering the large size of content files in video generation tasks, we provide subsequent videos for evaluation. However, for classification task types, we do not provide ground truth. Users are required to store the model-generated content in the "prediction" field of JSON files and then submit the results following the dataset structure (excluding video files). We will conduct evaluations promptly and return the assessment results. In the future, we plan to establish an evaluation website to showcase both evaluated model results and the results provided by users.

