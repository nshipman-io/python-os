#!/bin/bash

dir=$1

if [ -d "$dir" ]; then
	cd "$dir" || exit
	for website in *.HTM; do
		base=$(basename "$website" .HTM)
		echo mv "$website" "$base".html
	done
fi


