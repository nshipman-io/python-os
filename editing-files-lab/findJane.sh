#!/bin/bash

files=$(grep 'jane ' ~/data/list.txt | cut -d ' ' -f 3)

for file in $files; do
	if [ -e /home/student-03-57ebbbe148fd/$file ]; then
		echo /home/student-03-57ebbbe148fd$file >> oldFiles.txt
	fi
done
