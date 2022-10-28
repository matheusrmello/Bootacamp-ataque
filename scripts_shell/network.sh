#!/bin/bash

#endereco de rede
ifconfig | grep "broadcast" | cut -d "n" -f 2 | cut -d " " -f 2 | cut -d "." -f 1,2,3 > rede
#endereco de rede para variavel
REDE=$(cat rede)

#verificando rede
for ip in $(seq 254)
do 
    ping -c 1 $REDE.$ip | grep "64" | cut -d " " -f 4 | cut -d ":" -f 1 >> resultado &
done

#scan de portas
nmap -p 22,80,443,53 -iL resultado

rm resultado