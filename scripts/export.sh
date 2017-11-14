TENSORFLOW_MODEL_PATH=${TENSORFLOW_MODEL_PATH:-~/Documents/WorkSpace/tensorflow_models/research}
echo TENSORFLOW_MODEL_PATH=$TENSORFLOW_MODEL_PATH
PATH_TO_YOUR_PIPELINE_CONFIG=models/model/pipeline
PATH_TO_TRAIN_MODEL=models/train/model.ckpt-200000
# From tensorflow/models/research/
python ${TENSORFLOW_MODEL_PATH}/object_detection/export_inference_graph.py \
  --input_type image_tensor \
  --pipeline_config_path ${PATH_TO_YOUR_PIPELINE_CONFIG} \
  --trained_checkpoint_prefix ${PATH_TO_TRAIN_MODEL} \
  --output_directory output_inference_graph.pb
