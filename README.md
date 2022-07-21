# easyX: a simple Python library for saving complex data structure

This library enables you to save a Python dictionary with a complex structure to a single file. We have tested this library to save files in size 150 GB — i.e., you need a computer with 155 GB memory. 

The procedure is simple. The library tries to save homogeneous tensors by using the regular algorithm that is used for [Hierarchical Data Format 5 (HDF5)](https://en.wikipedia.org/wiki/Hierarchical_Data_Format). We will store them in a group called "raw." If the dictionary has other complex structures — such as another dictionary or nonhomogeneous tensors — the library will first dump the bytes of data from memory and encode it in a [base64](https://en.wikipedia.org/wiki/Base64) format. The encoded data will be stored as a vector in a group called "binary." This library is originally developed for the [easy fMRI project](https://easyfmri.learningbymachine.com/) — a toolbox for analyzing [task-based fMRI](https://en.wikipedia.org/wiki/Functional_magnetic_resonance_imaging) datasets.

## How to install?
You only need to copy the `easyX.py` to your project. You can use `git` for downloading this library, as well:
```bash
git clone https://gitlab.com/myousefnezhad/easyx.git
```

## Requirements
We have tested this library on Python 3.7 and Python 3.8. You need to install the libraries from the `requirements.txt` file:
```bash
pip install -r requirements.txt
```
This file includes `numpy`, `pickle`, `codecs`, `h5py`.


## How to use it?
You first copy `easyX.py` to your main project folder. Then, you will save all variables in the form of a dictionary in Python. As an example, we have created a sample data:
```python
data = {"a": np.array([[1, 2, 5, 8], [2., 4, 1, 6]]),
		 "b": [[1], [2, 4]],
		 "c": [[1, 20], [7, 4]],
		 "d": "Hi There",
		 "e": ["A", "B"],
		 "f": [["a", "b"], ["c", "d"]],
		 "h": np.random.rand(100, 1000)
		}
```
Here, we have the dictionary `data` that includes different shapes of variables.

### Saving a dictionary into a file
You can use following commands for saving a dictionary in a file:
```python
# Import easyX Library
from easyX import easyX
# Create an object from easyX class
ezx = easyX()
# Change this one with the PATH you need to save your data
fname = "/tmp/a.ezx"  
# Here, `data` is the example dictionary, you may replace it with yours
ezx.save(data, fname=fname) 
```

### Loading a data file into a dictionary
You can use following commands for loading a data file into a dictionary:
```python
# Import easyX Library
from easyX import easyX
# Create an object from easyX class
ezx = easyX()
# Change this one with the PATH you need to save your data
fname = "/tmp/a.ezx"  
# Data will be recovered in the `data` dictionary
data = ezx.load(fname=fname) 
```

### Loading the data structures (keys) from a data file into a dictionary
You can use following commands for loading the data structures (keys) from a data file into a dictionary:
```python
# Import easyX Library
from easyX import easyX
# Create an object from easyX class
ezx = easyX()
# Change this one with the PATH you need to save your data
fname = "/tmp/a.ezx"
# Keys will be recovered in the `keys` dictionary
keys = ezx.load_keys(fname=fname) 
```

For support and feedback, please contact us: [info@learningbymachine.com](mailto:info@learningbymachine.com).


