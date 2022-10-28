#!/bin/bash

echo "Este script ira buscar informacoes sobre o sistema operacional[s/n]"
read RESPOSTA
if [ $RESPOSTA != "s" ]
    then
        echo "Execucao interrompida"
        exit
else
    echo "Buscando dados sobre o sistema"
    echo "------------------------------"
    echo "Data e hora:"
    date
    echo "Uso do disco:"
    df
    echo "Usuarios logados:"
    w
fi