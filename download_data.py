"""Download data relevant to train the KittiSeg model."""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import logging
import sys
import os
import subprocess

import zipfile


from six.moves import urllib
from shutil import copy2

logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s',
                    level=logging.INFO,
                    stream=sys.stdout)

sys.path.insert(1, 'incl')

# Please set kitti_data_url to the download link for the Kitti DATA.
#
# You can obtain by going to this website:
# http://www.cvlibs.net/download.php?file=data_road.zip
#
# Replace 'http://kitti.is.tue.mpg.de/kitti/?????????.???' by the
# correct URL.
kitti_data_url = 'http://kitti.is.tue.mpg.de/kitti/?????????.???'


vgg_url = 'https://dl.dropboxusercontent.com/u/50333326/vgg16.npy'


def get_pathes():
    """
    Get location of `data_dir` and `run_dir'.

    Defaut is ./DATA and ./RUNS.
    Alternativly they can be set by the environoment variabels
    'TV_DIR_DATA' and 'TV_DIR_RUNS'.
    """

    if 'TV_DIR_DATA' in os.environ:
        data_dir = os.path.join(['hypes'], os.environ['TV_DIR_DATA'])
    else:
        data_dir = "DATA"

    if 'TV_DIR_RUNS' in os.environ:
        run_dir = os.path.join(['hypes'], os.environ['TV_DIR_DATA'])
    else:
        run_dir = "RUNS"

    return data_dir, run_dir


def download(url, dest_directory):
    filename = url.split('/')[-1]
    filepath = os.path.join(dest_directory, filename)

    logging.info("Download URL: {}".format(url))
    logging.info("Download DIR: {}".format(dest_directory))

    def _progress(count, block_size, total_size):
                prog = float(count * block_size) / float(total_size) * 100.0
                sys.stdout.write('\r>> Downloading %s %.1f%%' %
                                 (filename, prog))
                sys.stdout.flush()

    filepath, _ = urllib.request.urlretrieve(url, filepath,
                                             reporthook=_progress)
    print()


def main():
    data_dir, run_dir = get_pathes()

    vgg_weights = os.path.join(data_dir, 'vgg16.npy')

    if not os.path.exists(data_dir):
        os.makedirs(data_dir)

    # Download VGG DATA
    if not os.path.exists(vgg_weights):
        download_command = "wget {} -P {}".format(vgg_url, data_dir)
        logging.info("Downloading VGG weights.")
        download(vgg_url, data_dir)
    else:
        logging.warning("File: {} exists.".format(vgg_weights))
        logging.warning("Please delete to redownload VGG weights.")

    data_road_zip = os.path.join(data_dir, 'data_road.zip')

    # Download KITTI DATA
    if not os.path.exists(data_road_zip):
        if kitti_data_url == 'http://kitti.is.tue.mpg.de/kitti/?????????.???':
            logging.error("Data URL for Kitti Data unknown.")
            url = "http://www.cvlibs.net/download.php?file=data_road.zip"
            logging.error("Please visit: {}".format(url))
            logging.error("Request a Kitti Download link and set "
                          "'kitti_data_url' in download_data.py to"
                          "the correct URL and rerun the script.")
            exit(1)
        else:
            logging.info("Downloading Kitti Road Data.")
            download(kitti_data_url, data_dir)

    # Extract and prepare KITTI DATA
    zipfile.ZipFile(data_road_zip, 'r').extractall(data_dir)
    kitti_road_dir = os.path.join(data_dir, 'data_road/')

    train_txt = "data_scripts/train3.txt"
    val_txt = "data_scripts/val3.txt"
    copy2(train_txt, kitti_road_dir)
    copy2(val_txt, kitti_road_dir)

    logging.info("All data have been downloaded successful.")


if __name__ == '__main__':
    main()
