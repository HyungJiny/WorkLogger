#!/bin/bash

CWD="/home/dnlab/Github/WorkLogger"

if [ -z ${CWD} ]
then
    echo "CWD is not setted!"
    exit 0
fi

cd ${CWD}
source ./bin/activate
cd ./src/classscanner
python3 class_scanner.py

