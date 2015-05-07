#!/bin/bash 
sudo yum -y install git gcc python-dev python-devel
sudo pip install -U numpy 
sudo pip install pyyaml nltk 
sudo pip install -e git://github.com/mdp-toolkit/mdp-toolkit#egg=MDP 
sudo pip install geopandas
sudo yum-config-manager --enable epel
sudo yum install -y spatialindex spatialindex-devel
sudo ln -sf /usr/bin/python2.7 /usr/bin/python