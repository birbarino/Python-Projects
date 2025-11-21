#!/bin/bash

conda init && conda activate udacity
# Get eth0 IP address
HOST_ETH0_IP=`ip addr | grep eth0 | grep inet | awk '{print $2}' | cut -d"/" -f1`
# Run jupyter notebook for the IP address
jupyter notebook --no-browser --ip $HOST_ETH0_IP
