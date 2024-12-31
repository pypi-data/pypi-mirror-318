from setuptools import setup, Extension, find_packages
from Cython.Build import cythonize

setup(
    ext_modules=cythonize("USBMonitorUtilsLib/usb_monitor.pyx"),
    packages=find_packages(),
)
