from .coco import CocoDataset
from .builder import DATASETS

@DATASETS.register_module
class MyDataset(CocoDataset):
  CLASSES = ('Warplane', 'Plane', 'Tank', 'Warship', 'Ship', 'Person', 'MilitaryTruck', 'MilitaryJeep') ## ADD ALL YOUR CLASSES