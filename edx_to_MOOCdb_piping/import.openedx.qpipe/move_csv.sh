# !/bin/bash/expect

name=$1

mkdir '/tmp/'$name
cp -r /home/sebboyer/port/data_copy/$name/moocdb_csv /tmp/$name