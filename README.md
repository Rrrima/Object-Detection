# Object-Detection
based on tensorflow learning

#Copyright Xin Lu

## Overview

* 层级关系图
    * Server
    * Script (Our Work)
    * Training
    * Tensorflow-model @edcd29f[^1] []
    * Tensorflow-gpu 
    * Python 2.7, Macos/Linux


## Reference

* Setup:
    * Installation[^1]
    * Configuring an object detection pipeline[^2]
    * Preparing inputs[^3]
  
* Running:
    * Running locally[^4]
    * <del>Running on the cloud</del>
* Extras:
    * Tensorflow detection model zoo[^5]
    * Exporting a trained model for inference
    * Defining your own model architecture
    * Bringing in your own dataset

### Installation

1. 安装tensorflow和依赖包 
2. 编译protobuf接口到python版本 
3. 添加Model到PYTHONPATH, 我额外还加了tensorflow_models/research/object_detection/ 
4. 如何测试.

### Running locally

* 文件目录结构
```
+data
  -label_map file
  -train TFRecord file
  -eval TFRecord file
+models
  + model
    -pipeline config file
    +train
    +eval
```

* Run Eval & Board Job.
    
### Configuring an object detection pipeline

* pipeline := model train\_config eval\_config eval\_input\_reader
* model := num_classes type
* train_config := fine\_tune\_check\_point learning\_rate from\_detection\_checkpoint
* eval\_input\_reader =: input\_path label\_map\_path 

### Preparing inputs
* 如何生成TFRecord files.

### Bringing in your own dataset
* 如何构建自己的数据集生成TFRecord

### Exporting a trained model for inference
* 如何导出一个模型 

### Defining your own model architecture
* 略

### Tensorflow detection model zoo
* 各种模型的优劣



        
## Our Work

### Scripts

```
scripts/
├── board.sh 打开board网页
├── board_eval.sh 打开board_eval网页
├── build_hfs.sh 建立文件目录
├── check_gpu.sh 检查是否能安装GPU版本的TF
├── check_pythonpath.sh 检查PYTHONPATH
├── dependency.sh 安装依赖
├── detect.py 
├── download_model.py
├── eval.sh
├── export.sh
├── gitconfig
├── init_data.sh
├── init_env.sh
└── train.sh
```

### Detect部分

```
├── output_inference_graph.pb
│   ├── checkpoint
│   ├── frozen_inference_graph.pb
│   ├── model.ckpt.data-00000-of-00001
│   ├── model.ckpt.index
│   ├── model.ckpt.meta
│   └── saved_model
│       ├── saved_model.pb
│       └── variables
```

```
detect/
├── RESULT1 某次输出的模型
│   ├── frozen_inference_graph.pb 模型文件
│   └── output 检测生成的图片
├── RESULT2
│   ├── frozen_inference_graph.pb
│   └── output
└── test_images 测试数据集
```

###数据转换部分

```
convert/
├── CameraRollTag.json
├── README.txt
├── convert.py 转换脚本
├── helmet_label_map.pbtxt 类别说明文件
├── new_data 新数据处理,可忽略.
│   ├── CameraRollTag.json
│   ├── console.sh
│   ├── conv2utf8.sh
│   ├── csv2tag.rb
│   ├── drawBox.py
│   └── tag_utf8.csv
├── resize.py 图片尺寸缩放
└── t.json 旧数据测试标签

```

## Experience

1. Tensorflow的GPU版本比CPU版本快太多.
4. 用官方模型初始化速度比随机初始值要快5倍
2. OOM的问题需要缩放图片,pipeline里的ImageResizer不如预想中工作
3. 调整学习率以取得更好的收敛速度
3. LossFunction is Nan的问题原因之一是标注的ymin > ymax.

[^1]: 当时遇到了一个NasNet包找不到的问题, 是缺少`__init__.py`文件导致的. https://github.com/tensorflow/models/issues/2638, 后来官方修复了又折腾出一大堆新的issue.就保持在这个版本了.
