#!/bin/bash
echo "Esse script para pings continuos ao alvo. Executar?[s/n]"
read RESPOSTA
if [ $RESPOSTA != "s" ]
    then
        echo "Codigo interrompido"
        exit
else
    echo "Qual endereco pingar?"
    read ENDERECO
    echo "Quantos pings realiza?"
    read VALOR
    echo "Iniciando ping........"
    sleep 2
    for n in $(seq $VALOR)
    do
        ping -c 1 $ENDERECO
    done
fi
