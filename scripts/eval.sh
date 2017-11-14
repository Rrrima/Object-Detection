TENSORFLOW_MODEL_PATH=${TENSORFLOW_MODEL_PATH:-~/Documents/WorkSpace/tensorflow_models/research}
echo TENSORFLOW_MODEL_PATH=$TENSORFLOW_MODEL_PATH

PATH_TO_YOUR_PIPELINE_CONFIG=models/model/pipeline
PATH_TO_TRAIN_DIR=models/train
PATH_TO_EVAL_DIR=models/eval
# From the tensorflow/models/research/ directory
python ${TENSORFLOW_MODEL_PATH}/object_detection/eval.py \
    --logtostderr \
    --pipeline_config_path=${PATH_TO_YOUR_PIPELINE_CONFIG} \
    --checkpoint_dir=${PATH_TO_TRAIN_DIR} \
    --eval_dir=${PATH_TO_EVAL_DIR}
