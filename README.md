# TensorSeg
TensorSeg is a toolkit for building Segmentation approachs in Tensorflow.

## Train on Kitti Segmentation Data

1. Clone the repository: `git clone https://github.com/MarvinTeichmann/TensorSeg && cd TensorSeg`
2. Initialize all submodules: `git submodule update --init --recursive`
3. Install numpy, scipy, pillow and matplotlib 
(e.g. `pip install numpy scipy pillow matplotlib`)
4. Retrieve kitti data url here: `http://www.cvlibs.net/download.php?file=data_road.zip`
3. Download and prepared data by running: `python download_data.py --kitti_url http://kitti.is.tue.mpg.de/kitti/?????????.???`  
4. Run `python train.py` to start training


# Configuration 

http://tensorvision.readthedocs.io/en/master/user/configuration.html