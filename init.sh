#!/bin/bash

OWNER = $1
REPO = $2


#running data plane aggregate
echo "running data plane aggreagate ..."
cd data-plane

pip3 install -r requirements.txt
python3 aggregate.py

# running static analyzes on acquired data
echo "running static analyzes..."
cd ../static-analyze
pip3 install -r requirements.txt || { 
    echo "failed to install requirementes.txt" exit 1 
    }
python3 analyze.py > ../output.txt

# running the category ml to output table
echo "running machine learning categorization ..."
cd ../category-ml
pip3 install -r requirements.txt || {
     echo "failed to install req" exit 1
     }
python3 train.py >> ../output.txt

echo "showing analyzes output"

sleep(3)

cat ../output.txt