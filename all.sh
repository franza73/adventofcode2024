for i in {1..5};
do
    echo "-- day$i --"
    flake8 ./day$i.py
    pylint ./day$i.py
    ./day$i.py
done
