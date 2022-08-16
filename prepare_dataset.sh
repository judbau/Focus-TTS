#!/usr/bin/env bash

set -e

: ${DATA_DIR:=prosody-control}
: ${ARGS="--extract-mels"}

python prepare_dataset.py --wav-text-filelists filelists/pc_audio_text_train.txt filelists/pc_audio_text_val.txt --n-workers 16 --batch-size 1 --dataset-path $DATA_DIR --extract-pitch --f0-method pyin $ARGS