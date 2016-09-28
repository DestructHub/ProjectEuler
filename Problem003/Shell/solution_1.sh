#!/bin/bash

prime () {
  num=$1

  counter=2
  while [  $counter -lt $num  ]; do
    if !(($num % $counter)); then num=$(($num/$counter)); fi

    let counter=counter+1
  done

  echo $num
}

prime 600851475143
