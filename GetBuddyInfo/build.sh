#!/bin/bash
#
# Script to clean and build application.
#
rm -r build dist
python setup.py py2app --no-strip
