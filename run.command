#!/bin/bash
#
# call python on macos/linux

export KMP_DUPLICATE_LIB_OK=TRUE

cd `dirname "$0"`

python $1
