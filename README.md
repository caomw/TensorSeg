# TensorSeg
TensorSeg is a toolkit for building Segmentation approachs in Tensorflow.


# Run Segmentation on Kitti Data

```
$ git clone --recursive https://github.com/MarvinTeichmann/TensorSeg
$ cd TensorSeg
$ python download_data.py
$ python train.py
```

**Important:** Please use `git clone --recursive` to clone this repository. Otherwise the submodules `TensorVision` and `tensorflow_fcn` will not be loaded.


# Configuration 

http://tensorvision.readthedocs.io/en/master/user/configuration.html