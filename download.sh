#!/bin/bash
mkdir -p $1
git lfs install --skip-smudge
git clone https://huggingface.co/$1 $1
cd $1
git lfs pull
git lfs install --force
rm -rf .git
pwd
ls -l