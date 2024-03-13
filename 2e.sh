
arquiteto=$(uname -m)
nucleos=$(lscpu | grep CPU)
ram=$(free)
user=$(whoami)
boot=$(uptime -s)
MAC=$(ip link)
echo "Arquitetura do sistema operacional $arquiteto: "
echo "Número de núcleos físicos do processador $nucleos: "
echo "Memória RAM $ram: "
echo "Nome do usuário $user: "
echo "Instante do último boot $boot: "
echo "MAC da placa de rede $MAC: "
