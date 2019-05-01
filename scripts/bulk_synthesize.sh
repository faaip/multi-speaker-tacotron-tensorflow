#!/usr/bin/env bash
echo "start!"
LOAD_PATH=${1?Error: no load path given!}
FILE_NAME=${2?Error: no txt file given!}

echo $LOAD_PATH
# while read p;do
# 	echo "$p"
# done <$FILE_NAME
