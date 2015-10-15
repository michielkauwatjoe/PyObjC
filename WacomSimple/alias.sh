#!/bin/bash
#
# Script to clean and build application.
#
python setup.py py2app -A # Compile with aliased dependencies
killall WacomSimple # Kills running application.
./dist/WacomSimple.app/Contents/MacOS/WacomSimple # Calls application binary from the command line.
