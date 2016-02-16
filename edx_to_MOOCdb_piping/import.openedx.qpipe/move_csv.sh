#!/bin/bash/expect


source_name = $1
dest_name=$2

mkdir $dest_name
cp -r $source_name/ $dest_name/