TENSORFLOW_MODEL_PATH=${TENSORFLOW_MODEL_PATH:-~/Documents/WorkSpace/tensorflow_models/research}
echo TENSORFLOW_MODEL_PATH=$TENSORFLOW_MODEL_PATH
# From tensorflow/models/research/
wget http://host.robots.ox.ac.uk/pascal/VOC/voc2012/VOCtrainval_11-May-2012.tar
tar -xvf VOCtrainval_11-May-2012.tar

python ${TENSORFLOW_MODEL_PATH}/object_detection/create_pascal_tf_record.py \
      --label_map_path=${TENSORFLOW_MODEL_PATH}/object_detection/data/pascal_label_map.pbtxt \
          --data_dir=VOCdevkit --year=VOC2012 --set=train \
              --output_path=data/pascal_train.record
python ${TENSORFLOW_MODEL_PATH}/object_detection/create_pascal_tf_record.py \
      --label_map_path=${TENSORFLOW_MODEL_PATH}/object_detection/data/pascal_label_map.pbtxt \
          --data_dir=VOCdevkit --year=VOC2012 --set=val \
              --output_path=data/pascal_val.record

cp $TENSORFLOW_MODEL_PATH/object_detection/data/pascal_label_map.pbtxt data/pascal_label_map.pbtxt
