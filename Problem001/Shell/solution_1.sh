#!/bin/bash

for i in {0..999}; do if !(($i%3)) || !(($i%5)); then multiples[$i]=$i; fi; done
for j in ${multiples[@]}; do let total+=$j; done; echo $total
