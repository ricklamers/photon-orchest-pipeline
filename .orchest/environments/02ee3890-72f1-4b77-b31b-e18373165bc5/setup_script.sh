#!/bin/bash

# Install any dependencies you have in this shell script.

# E.g. pip install tensorflow
sudo mkdir /photon
sudo chown -R $NB_USER /photon
git clone https://github.com/s0md3v/Photon.git /photon
pip install -r /photon/requirements.txt