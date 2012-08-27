#!/usr/bin/env python

import os, glob

from subprocess import call

output_dir = '../../postman_lib'

for file in glob.glob("*.ui"):
    # call pyside-uic input_file -o output_file
    output_file = 'Ui_' + file.split('.')[0] + '.py'
    call(['pyside-uic', file, '-o', os.path.join(output_dir, output_file)])
