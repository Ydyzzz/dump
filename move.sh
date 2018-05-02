#!/bin/bash

for file in ~/Downloads/*
do
	if [[ $file = *".pdf" || $file = *".djvu" || $file = *".epub" ]]; then
		#mv $file "~/Must Read/$file"
		mv "$file" ~/Must\ Read/

	fi
done
