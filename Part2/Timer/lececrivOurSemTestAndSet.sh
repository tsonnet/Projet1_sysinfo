#!/bin/bash

#gcc -pthread Semimplem.c -o lececrivOurSem  ....

cd ../src
THREADS=(1 2 4 8 16 32 64) 
echo "thread,i,time"
for thread in "${THREADS[@]}"; do
	for i in {1..5}; do
		/usr/bin/time -f "$thread,$i,%E" ./lececriv3 $thread  $thread 2560 640 2>&1
	done
done
