import tensorflow as tf
import numpy as np

from bert4keras.backend import keras
from bert4keras.models import build_transformer_model, Transformer
from bert4keras.tokenizers import Tokenizer

bert_tokenizer = Tokenizer("./pretrain_weights/ancient_chinese_base/vocab.txt")

bert = build_transformer_model(
    config_path="./pretrain_weights/ancient_chinese_base/bert_config.json",
    checkpoint_path="./pretrain_weights/ancient_chinese_base/bert_model.ckpt",
    model="bert",
    # with_mlm='linear', 
    return_keras_model=True,
)