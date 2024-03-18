#!/bin/bash
# Move files with 'i' in the name to the corresponding dayi folder
for ((i=1; i<=9; i++)); do
    echo $i
	echo ./day$i/
	mv *$i* ./day$i/
done