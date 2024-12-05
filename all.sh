#!/bin/bash
for i in {1..25};
do
    if [ ! -f ./day$i.py ]; then break; fi
    echo "-- day$i --"
    flake8 ./day$i.py
    pylint --score=n ./day$i.py
    ./day$i.py
done
