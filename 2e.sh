#!/bin/bash

# Informações sobre o sistema operacional
echo "Arquitetura do sistema operacional:"
uname -m

# Número de núcleos físicos do processador
echo "Número de núcleos físicos do processador:"
nproc

# Memória RAM
echo "Memória RAM (em bytes):"
free -b | awk '/Mem:/ {print $2}'

# Nome do usuário
echo "Nome do usuário:"
whoami

# Instante do último boot
echo "Instante do último boot:"
uptime -s

# MAC da placa de rede (eth0)
echo "MAC da placa de rede (eth0):"
ifconfig eth0 | awk '/ether/ {print $2}'