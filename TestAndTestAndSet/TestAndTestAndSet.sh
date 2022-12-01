#!/bin/bash


THREADS=(1 2 4 8 16 32 64) # ON met directement deux philo car bug avec 1
echo "thread,i,time"
for thread in "${THREADS[@]}"; do
	for i in {1..5}; do
		/usr/bin/time -f "$thread,$i,%E" ./testAndTestAndSet  $thread 2>&1
	done
done
