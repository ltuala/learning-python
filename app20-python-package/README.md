# What is this project
Publish a python package that generate PDF invoices.
![Python Package](14.png)
## How to run
1. cd to root folder, run the following command to create a source distribution
```
python setup.py sdist
```
2. Install `twine`, for upload process
```
python -m pip install twine
```
3. Run the following command to upload to PyPi
```
twine upload dist/*
```