from __future__ import absolute_import, division, print_function

from .dataset.coco import COCO
from .dataset.coco_hp import COCOHP
from .dataset.kitti import KITTI
from .dataset.pascal import PascalVOC
from .sample.ctdet import CTDetDataset
from .sample.ddd import DddDataset
from .sample.exdet import EXDetDataset
from .sample.multi_pose import MultiPoseDataset

dataset_factory = {"coco": COCO, "pascal": PascalVOC, "kitti": KITTI, "coco_hp": COCOHP}

_sample_factory = {
    "exdet": EXDetDataset,
    "ctdet": CTDetDataset,
    "ddd": DddDataset,
    "multi_pose": MultiPoseDataset,
}


def get_dataset(dataset, task):
    class Dataset(dataset_factory[dataset], _sample_factory[task]):
        pass

    return Dataset
