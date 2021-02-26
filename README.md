古汉语语言模型
===========================

语料：[殆知阁古代文献txt大全集](https://github.com/garychowcmu/daizhigev20)

训练平台：Colab [白嫖Colab训练语言模型教程](https://github.com/genggui001/everyone_can_pretrain_language_model)

基础框架：苏神的[bert4keras](https://github.com/bojone/bert4keras)

框架安装：

```
pip install bert4keras==0.9.9
```

## T5 Encoder版本

### 模型调用代码：

[ancient_chinese_t5s.py](ancient_chinese_t5s.py)

### 模型参数下载地址：

百度网盘：[链接](https://pan.baidu.com/s/1S3UUtwrajNrdtnh-atxxsA) 提取码：15bv

### 模型预训练过程：

两阶段预训练：90%采用128句子长度，10%采用512句子长度

128阶段预训练参数：

```
seq_len = 128
batch_size = 1792
learning_rate = 0.00125
weight_decay_rate = 0.01
num_warmup_steps = 0
num_train_steps = 250000
```

mlm_loss曲线：

![ancient_chinese_t5s_mlm_loss_step_0](images/ancient_chinese_t5s_mlm_loss_step_0.png)

mlm_acc曲线：

![ancient_chinese_t5s_mlm_acc_step_0](images/ancient_chinese_t5s_mlm_acc_step_0.png)

512阶段预训练参数：

```
seq_len = 512
batch_size = 1792
learning_rate = 0.000125
weight_decay_rate = 0.01
num_warmup_steps = 0
num_train_steps = 25000
```

mlm_loss曲线：

![ancient_chinese_t5s_mlm_loss_step_1](images/ancient_chinese_t5s_mlm_loss_step_1.png)

mlm_acc曲线：

![ancient_chinese_t5s_mlm_acc_step_1](images/ancient_chinese_t5s_mlm_acc_step_1.png)


## Bert Base版本

### 模型调用代码：

[ancient_chinese_base.py](ancient_chinese_base.py)

### 模型参数下载地址：

百度网盘：[链接](https://pan.baidu.com/s/1TmWoGVg7tTmNt5NWITSDRA) 提取码：26yh

### 模型预训练过程：

两阶段预训练：90%采用128句子长度，10%采用512句子长度

128阶段预训练参数：

```
seq_len = 128
batch_size = 1792
learning_rate = 0.00125
weight_decay_rate = 0.01
num_warmup_steps = 3125
num_train_steps = 250000
```

mlm_loss曲线：

![ancient_chinese_base_mlm_loss_step_0](images/ancient_chinese_base_mlm_loss_step_0.png)

mlm_acc曲线：

![ancient_chinese_base_mlm_acc_step_0](images/ancient_chinese_base_mlm_acc_step_0.png)

512阶段预训练参数：

```
seq_len = 512
batch_size = 1792
learning_rate = 0.000125
weight_decay_rate = 0.01
num_warmup_steps = 0
num_train_steps = 25000
```

mlm_loss曲线：

![ancient_chinese_base_mlm_loss_step_1](images/ancient_chinese_base_mlm_loss_step_1.png)

mlm_acc曲线：

![ancient_chinese_base_mlm_acc_step_1](images/ancient_chinese_base_mlm_acc_step_1.png)


