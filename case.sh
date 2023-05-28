#!/bin/bash
x=$1
case $x in
"car" )
  echo "rent is 100" ;;
 "bus" )
  echo "rent is 50" ;;
"bike" )
  echo "rent is 20" ;;
* )
  echo "unknown" ;;
esac