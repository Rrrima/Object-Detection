TENSORFLOW_MODEL_PATH=${TENSORFLOW_MODEL_PATH:-~/Documents/WorkSpace/tensorflow_models/research}
echo TENSORFLOW_MODEL_PATH=$TENSORFLOW_MODEL_PATH
PATH_TO_YOUR_PIPELINE_CONFIG=models/model/pipeline
PATH_TO_TRAIN_DIR=models/train
# From the tensorflow/models/research/ directory
python ${TENSORFLOW_MODEL_PATH}/object_detection/train.py \
    --logtostderr \
    --pipeline_config_path=${PATH_TO_YOUR_PIPELINE_CONFIG} \
    --train_dir=${PATH_TO_TRAIN_DIR}
