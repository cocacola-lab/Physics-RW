<div align="center">
    <h2> Bridging the Reality Gap: A Benchmark for Physical Reasoning in General World Models with Various Physical Phenomena beyond Mechanics </h2>
</div>
Physics-RW benchmark is a physical reasoning dataset constructed from real-world videos. Encompassing a broad spectrum of real-world phenomena—mechanics, thermodynamics, electromagnetism, and optics—Physics-RW offers a comprehensive evaluation platform.

-----
## 0. Contents
- [0. Contents](#0-contents)
- [1. The Organized Structure of Dataset](#1-the-organized-structure-of-dataset)
- [2. Download Dataset](#2-download-dataset)
- [3. Benchmark Evaluation](#3-benchmark-evaluate)

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
## 3. Benchmark Evaluation <a id="benchmark-evaluate"></a>
We primarily evaluate existing methods based on accuracy (ACC), F1 score, and Fréchet Video Distance (FVD) metrics. Considering the large size of content files in video generation tasks, we provide subsequent videos for evaluation. However, for classification task types, we do not provide ground truth. Users are required to store the model-generated content in the "prediction" field of JSON files and then submit the results following the dataset structure (excluding video files). We will conduct evaluations promptly and return the assessment results. In the future, we plan to establish an evaluation website to showcase both evaluated model results and the results provided by users.
## 4. Baseline Models
We have evaluated the representative models, and the code is available at the following link:
| Model Name | Paper or Project | Code Link | License |
| ---------- | ------------ | ---------- | ----------|
| LLaMA-Adapter | [LLaMA-Adapter: Efficient Fine-tuning of Language Models with Zero-init Attention](https://arxiv.org/pdf/2303.16199) | [code](https://github.com/OpenGVLab/LLaMA-Adapter/tree/main/imagebind_LLM) |GPL-3.0 license|
| Large World Model | [World Model on Million-Length Video and Language with Blockwise RingAttention](https://arxiv.org/abs/2402.08268)| [code](https://github.com/LargeWorldModel/LWM) |Apache License 2.0|
| VideoChat | [VideoChat : Chat-Centric Video Understanding](https://arxiv.org/abs/2305.06355) | [code](https://github.com/OpenGVLab/Ask-Anything/tree/main/video_chat) |MIT License|
| VideoChat2 | [MVBench: A Comprehensive Multi-modal Video Understanding Benchmark](https://arxiv.org/abs/2311.17005)| [code](https://github.com/OpenGVLab/Ask-Anything/tree/main/video_chat2) |MIT License|
| Video-LLaMA | [Video-LLaMA: An Instruction-tuned Audio-Visual Language Model for Video Understanding](https://arxiv.org/abs/2306.02858) | [code](https://github.com/DAMO-NLP-SG/Video-LLaMA) |BSD 3-Clause License|
| Video-ChatGPT | [Video-ChatGPT: Towards Detailed Video Understanding via Large Vision and Language Models](https://arxiv.org/abs/2306.05424) | [code](https://github.com/mbzuai-oryx/Video-ChatGPT) | CC-BY-4.0 License|
| Video-LLaVA | [Video-LLaVA: Learning United Visual Representation by Alignment Before Projection](https://arxiv.org/abs/2311.10122) | [code](https://github.com/PKU-YuanGroup/Video-LLaVA) | Apache License 2.0|
| MiniGPT4-Video | [MiniGPT4-Video: Advancing Multimodal LLMs for Video Understanding with Interleaved Visual-Textual Tokens](https://arxiv.org/abs/2404.03413) | [code](https://github.com/Vision-CAIR/MiniGPT4-video) | BSD 3-Clause License|
| Gemini 1.5 Pro | [Gemini 1.5: Unlocking multimodal understanding across millions of tokens of context](https://arxiv.org/pdf/2403.05530) | [code](https://github.com/google-gemini/cookbook/blob/main/quickstarts/Video.ipynb) | Apache License 2.0|
| GPT-4o | [GPT-4o](https://openai.com/index/hello-gpt-4o/) | [code](https://github.com/openai/openai-cookbook/blob/main/examples/gpt4o/introduction_to_gpt4o.ipynb) | MIT License |
| NExT-GPT | [NExT-GPT: Any-to-Any Multimodal LLM](https://arxiv.org/abs/2309.05519) | [code](https://github.com/NExT-GPT/NExT-GPT) | BSD 3-Clause License |
| Open-Sora | -------------- | [code](https://github.com/hpcaitech/Open-Sora) | Apache License 2.0 |


## 5. Contact Us
If you have any questions, please feel free to contact us via email at pengyuzhao@bjtu.edu.cn or zhaopengyuh@163.com. (Note: For classification task submissions, please send an email to the above addresses for now. We will set up a website for submissions in the future.)

