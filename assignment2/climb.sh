#!/bin/bash

if [ $# -gt 0 ]; then

  number_of_steps=$1;

  for (( i = 0; i < number_of_steps; i++ )); do
      cd ..
  done
  echo "Climbed up ${number_of_steps} steps"

else
  cd ..
  echo "Climbed up 1 step"

fi