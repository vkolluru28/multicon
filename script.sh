#!/bin/bash
echo "DAD PC 1 TOP"
echo "----------------------------------------------------"
sshpass -p swethakvs ssh swetha@192.168.1.5 "top -b -n 1" 
