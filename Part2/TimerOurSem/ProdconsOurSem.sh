#!/bin/bash

#gcc -pthread Semimplem.c -o ProdconsOurSem  ....
cd ../srcOurSem
THREADS=(1 2 4 8 ) 
echo "thread,i,time"
for thread in "${THREADS[@]}"; do
	for i in {1..5}; do
		/usr/bin/time -f "$thread,$i,%E" ./ProdconsOurSem $thread  $thread 8192 2>&1
	done
done
