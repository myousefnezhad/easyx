# MIT License

# Copyright (c) 2022 Tony (Muhammad) Yousefnezhad

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import h5py
import pickle
import codecs
import numpy as np

class easyX:
    def _obj_to_binary(self, objdat):
        """
        This function dumps a data object to a string of Base64 string.
        :param object objdat: a binary data object

        :return: a string of Base64 encoded
        """
        return codecs.encode(pickle.dumps(objdat), "base64").decode()

    def _binary_to_obj(self, bdata):
        """
        This function decode a string of Base64 to a binary data object
        :param string bdata: A string of Base64

        :return: A binary data object
        """
        return pickle.loads(codecs.decode(str(np.array(bdata, dtype=str)).encode(), "base64"))

    def save(self, data, fname, verbose=True):
        """
        This function save a structured data (dictionary) to a single file

        :param dict data: A python dictionary includes all of our data
        :param string fname: A string includes output file address
        :param bool verbose: A binary variable to enable showing log of saving process; It is enabled by default.

        :return: A binary that is true if everything is fine.
        """
        try:
            binaryKeys = list()
            hf = h5py.File(fname, "w")
            hf.create_dataset("__easyfMRI__", data="easyX")
            # Save RAW data
            rawGroup = hf.create_group("raw")
            for k in data.keys():
                try:
                    if verbose:
                        print('\x1b[0m' + f"SAVE::RAW::{k}", end='')
                    rawGroup.create_dataset(k, data=data[k])
                    if verbose:
                        print('\x1b[32m' + " ✓" + '\x1b[0m')
                except:
                    binaryKeys.append(k)
                    print('\x1b[0m' + " [" + '\x1b[94m' + "R2B" + '\x1b[0m' + "]" + '\x1b[0m')
            # Save Binary data
            binaryGroup = hf.create_group("binary")
            for bk in binaryKeys:
                try:
                    if verbose:
                        print('\x1b[0m' + f"SAVE::BINARY::{bk}", end='')
                    binaryGroup.create_dataset(bk, data=self._obj_to_binary(data[bk]))
                    if verbose:
                        print('\x1b[32m' + " ✓" + '\x1b[0m')
                except Exception as e:
                    raise Exception(f"Cannot save data: \"{bk}\"\n" + str(e))
            hf.close()
        except:
            return False
        return True


    def load(self, fname, partial=None, verbose=True):
        """
        This function load an easyX file to a python dictionary

        :param string fname: The address of a file
        :param list partial: A list of strings, including variables that should be load from saved dictionary; It is None by default that causes loading all saved keys.
        :param bool verbose: A binary variable to enable showing log of loading process; It is enabled by default.

        :return: A python dictionary including saved data
        """
        out = dict()
        hf = h5py.File(fname, "r")
        try:
            if str(np.asanyarray(hf.get("__easyfMRI__"))) == "easyX":
                print("Signed by easyX project!")
        except:
            pass
        try:
            if len(partial) == 0:
                raise Exception
        except:
            partial = None
        # Load RAW data
        rawData = hf['raw']
        for k in rawData.keys():
            is_load = True
            if partial is not None:
                is_load = False
                try:
                    if k in partial:
                        is_load = True
                except:
                    pass
            if is_load:
                if verbose:
                    print('\x1b[0m' + f"LOAD::RAW::{k}" , end='')
                out[k] = np.asarray(rawData[k])
                if verbose:
                    print('\x1b[32m' + " ✓" + '\x1b[0m')

        # Load Binary data
        binaryData = hf['binary']
        for bk in binaryData.keys():
            is_load = True
            if partial is not None:
                is_load = False
                try:
                    if bk in partial:
                        is_load = True
                except:
                    pass
            if is_load:
                if verbose:
                    print('\x1b[0m' + f"LOAD::BINARY::{bk}", end='')
                try:
                    out[bk] = self._binary_to_obj(np.asarray(binaryData[bk]))
                    if verbose:
                        print('\x1b[32m' + " ✓" + '\x1b[0m')
                except:
                    if verbose:
                        print('\x1b[31m' + " x" + '\x1b[0m')
        return out

    def load_keys(self, fname):
        """
        This function only loads variable names from a saved easyX file.
        It is suitable for checking whether a variable name exists in a big data or not.

        :param string fname: The address of a file

        :return: A python dictionary including all saved keys; the value is None for all variables.
        """
        out = dict()
        hf = h5py.File(fname, "r")
        rawData = hf['raw']
        for k in rawData.keys():
            out[k] = None
        # Load Binary data
        binaryData = hf['binary']
        for bk in binaryData.keys():
            out[bk] = None
        return out