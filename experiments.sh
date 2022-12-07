#!/bin/bash


cd  Part2/Timer


echo " PhiloTestAndTEstAndSet"
./philosophesOurSem.sh

echo " ProdConsTestAndTestAndSEt"

#./prodconsOurSem.sh

echo "lececrivTestAndTEstAndSet"

#./lececrivOurSem.sh

echo " PhiloTestAndSet"
./philosophesOurSemTestAndSet.sh

echo " ProdConsTestAndSEt"

#./prodconsOurSemTestAndSet.sh

echo "lececrivTestAndSet"

#./lececrivOurSemTestAndSet.sh
cd ../TestAndSet
echo "testAnd Set"
#./testandset.sh

cd ../TestAndTestAndSet
echo "testAndTestAndSet"

#./TestAndTestAndSet.sh