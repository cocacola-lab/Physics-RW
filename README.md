<div align="center">
    <h2> Bridging the Reality Gap: A Benchmark for Physical Reasoning in General World Models with Various Physical Phenomena beyond Mechanics </h2>
</div>
Physics-RW benchmark is a physical reasoning dataset constructed from real-world videos. Encompassing a broad spectrum of real-world phenomena—mechanics, thermodynamics, electromagnetism, and optics—Physics-RW offers a comprehensive evaluation platform.

-----
## The dataset is organized as follows.
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
## Downloading the Physics-RW dataset
Our data is stored in Physics-RW. Currently, only part of the data has been uploaded. Once the review process is complete, we will update all the data. 
**Dataset URL**: [https://www.modelscope.cn/datasets/pengyz/Physics-RW]

There are two methods for downloading:

1. Download via the ModelScope library.
```bash
from modelscope.msdatasets import MsDataset
ds =  MsDataset.load('pengyz/Physics-RW')
```
2.  Download via GiT.
```
git clone https://www.modelscope.cn/datasets/pengyz/Physics-RW.git
```
