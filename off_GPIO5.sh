#!/bin/bash
# Indicamos el pin GPIO que recibe el cambio de estado para el apagado
GPIOpin1=5
echo "$GPIOpin1" > /sys/class/gpio/export
echo "in" > /sys/class/gpio/gpio$GPIOpin1/direction
while true; do
  sleep 1
  power=$(cat /sys/class/gpio/gpio$GPIOpin1/value)
  if [ $power != 1 ]; then
    echo "out" > /sys/class/gpio/gpio$GPIOpin1/direction
    echo "0" > /sys/class/gpio/gpio$GPIOpin1/value
    sleep 3
    sudo shutdown -h now
  fi
done
