from object_detection.utils import dataset_util
from object_detection.utils import label_map_util

import os
import random
import tensorflow as tf
from PIL import Image
import io

def SplitTag(tag, test_ratio):
  total_num = len(tag)
  test_num = int(test_ratio * total_num)

  keys = set(tag.keys())
  test_keys = random.sample(keys, test_num)
  train_keys = keys - set(test_keys)

  return train_keys, test_keys

def ReadImage(filename):
  with open(filename, 'rb') as f:
    data = f.read()
  return data

class ExampleMaker:
  def __init__(self, label_map_path, image_dir, tag_path):
    self.IMAGE_DIR = image_dir
    self.LABEL_MAP = label_map_util.get_label_map_dict(label_map_path)
    with open(tag_path, 'r') as f:
      self.TAG = eval(f.read())

  def GetExample(self, filename, encoded_image_data, boxes):
    image = Image.open(io.BytesIO(encoded_image_data))
    height = image.height # Image height
    width = image.width # Image width
    image_format = b'jpeg' # b'jpeg' or b'png'

    xmins = [] # List of normalized left x coordinates in bounding box (1 per box)
    xmaxs = [] # List of normalized right x coordinates in bounding box
             # (1 per box)
    ymins = [] # List of normalized top y coordinates in bounding box (1 per box)
    ymaxs = [] # List of normalized bottom y coordinates in bounding box
             # (1 per box)
    classes_text = [] # List of string class name of bounding box (1 per box)
    classes = [] # List of integer class id of bounding box (1 per box)

    for box in boxes:
      xmins.append(box['xmin'])
      xmaxs.append(box['xmax'])
      ymins.append(box['ymin'])
      ymaxs.append(box['ymax'])
      classes_text.append(box['class'].encode('utf8'))
      classes.append(self.LABEL_MAP[box['class']])

    tf_example = tf.train.Example(features=tf.train.Features(feature={
      'image/height': dataset_util.int64_feature(height),
      'image/width': dataset_util.int64_feature(width),
      'image/filename': dataset_util.bytes_feature(filename),
      'image/source_id': dataset_util.bytes_feature(filename),
      'image/encoded': dataset_util.bytes_feature(encoded_image_data),
      'image/format': dataset_util.bytes_feature(image_format),
      'image/object/bbox/xmin': dataset_util.float_list_feature(xmins),
      'image/object/bbox/xmax': dataset_util.float_list_feature(xmaxs),
      'image/object/bbox/ymin': dataset_util.float_list_feature(ymins),
      'image/object/bbox/ymax': dataset_util.float_list_feature(ymaxs),
      'image/object/class/text': dataset_util.bytes_list_feature(classes_text),
      'image/object/class/label': dataset_util.int64_list_feature(classes),
    }))
    """
    print("height:" + str(height) + "\n",
    "width:" + str(width) + "\n",
    "filename:" + str(filename) + "\n",
    "image_format:" + str(image_format) + "\n",
    "xmins:" + str(xmins) + "\n",
    "xmaxs:" + str(xmaxs) + "\n",
    "ymins:" + str(ymins) + "\n",
    "ymaxs:" + str(ymaxs) + "\n",
    "classes_text:" + str(classes_text) + "\n",
    "classes:" + str(classes) + "\n")
    """
    return tf_example

  def CreateRecord(self, keys, output):
    writer = tf.python_io.TFRecordWriter(output)

    for iname in keys:
      print('processing ' + iname)
      data = ReadImage(os.path.join(self.IMAGE_DIR, iname))
      boxes = self.TAG[iname]['boxes']
      tfexample = self.GetExample(iname, data, boxes)
      writer.write(tfexample.SerializeToString())
      #break
    writer.close()
    return

  def CreateAllRecord(self, test_ratio, train_path, test_path):
    train_keys, test_keys = SplitTag(self.TAG,test_ratio)
    print(train_keys, test_keys)
    self.CreateRecord(train_keys, train_path)
    self.CreateRecord(test_keys, test_path)

if __name__ == '__main__':
  LABEL_MAP_FILE = 'helmet_label_map.pbtxt'
  IMAGE_DIR = 'images'
  TAG_FILE = 'CameraRollTag.json'
  TEST_RATIO = 0.2
  TRAIN_OUTPUT = 'helmet_train.record'
  VAL_OUTPUT = 'helmet_val.record'

  maker = ExampleMaker(LABEL_MAP_FILE, IMAGE_DIR, TAG_FILE)
  maker.CreateAllRecord(TEST_RATIO, TRAIN_OUTPUT, VAL_OUTPUT)




