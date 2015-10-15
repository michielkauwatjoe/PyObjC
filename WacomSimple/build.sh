#!/bin/bash
#
# Script to clean and build application.
#
rm -r build dist # Removes build files and compiled application.
python setup.py py2app --no-strip # Compiles again.
killall WacomSimple # Kills running application.
./dist/WacomSimple.app/Contents/MacOS/WacomSimple # Calls application binary from the command line.
