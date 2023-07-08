mkdir intfloat
git lfs install --skip-smudge
git clone https://huggingface.co/intfloat/e5-large-v2 intfloat/e5-large-v2
cd intfloat/e5-large-v2
git lfs pull
git lfs install --force
rm model.safetensors
rm -rf .git
pwd
ls -l