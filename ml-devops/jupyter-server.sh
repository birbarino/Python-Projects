#!/bin/bash

# Get eth0 IP address
HOST_ETH0_IP=`ip addr | grep eth0 | grep inet | awk '{print $2}' | cut -d"/" -f1`
# Run jupyter notebook for the IP address
jupyter lab --NotebookApp.token=$JUPYTER_TOKEN --no-browser --ip $HOST_ETH0_IP
