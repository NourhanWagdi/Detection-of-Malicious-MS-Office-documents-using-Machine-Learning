#!/bin/bash

for file in /home/remnux/Pictures/doc_samples/clean/*
do
     olevba -j  "$file" | grep -e "keyword" -e "sample" >> CleanOutput 
    
done
