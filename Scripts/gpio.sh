#!/bin/bash
for i in {1 2 3 4 5 6 7 8 9  10}
do
gpio mode 0 out
gpio -g  mode 27 out
gpio write 0 1
gpio -g  write 27 0
sleep 1s
gpio write 0 0
gpio -g write 27 1
sleep 1s
done
gpio -g write 27 0
