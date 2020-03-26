#!/usr/bin/env python
# -*- coding: utf-8 -*-
import gpt_2_simple as gpt2
import os
import sys

model_name = "345M"

def download_model():
    if not os.path.isdir(os.path.join("models", model_name)):
        print("Downloading {model_name} model...")
        gpt2.download_gpt2(model_name=model_name)   # model is saved into current directory under /models/124M/


def train(filename):
    sess = gpt2.start_tf_sess()
    gpt2.finetune(sess,
                  filename,
                  model_name=model_name,
                  steps=1000)   # steps is max number of training steps

    gpt2.generate(sess)

if __name__ == '__main__':
    download_model()
    args = sys.argv[1:]
    if len(args) != 1:
        print('The .txt to train joko on is a required arg for train.py')
        sys.exit(1)
    train(args[0])
