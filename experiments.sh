#!/bin/bash


cd  Part2/Timer


echo " PhiloTestAndTEstAndSet"
./philosophesOurSem.sh

echo " ProdConsTestAndTestAndSEt"

./prodconsOurSem.sh

echo "lececrivTestAndTEstAndSet"

./lececrivOurSem.sh

echo " PhiloTestAndSet"
./philosophesOurSemTestAndSet.sh

echo " ProdConsTestAndSEt"

./prodconsOurSemTestAndSet.sh

echo "lececrivTestAndSet"

./lececrivOurSemTestAndSet.sh

echo "TestAndSet"

cd ../TestAndSet

./testandset.sh

echo "TestAndTestAndSet"

cd ../TestAndTestAndSet

./TestAndTestAndSet.sh

