
# Automação de tarefas de análise de rede (por exemplo, varreduras de vulnerabilidade, coleta de logs).

import nmap

# Função para realizar a varredura de vulnerabilidade

def scan_network(target_ip):
    nm = nmap.PortScanner()

    print(f"Iniciando varredura para o IP: {target_ip}")
    nm.scan(hosts=target_ip, arguments='-sS -O')  # -sS para escanear portas e -O para tentar detectar o sistema operacional

    print("Resultado da varredura:")
    print(f"Host: {target_ip} está {nm[target_ip].state()}")
    
    # Exibe as portas abertas
    for proto in nm[target_ip].all_protocols():
        print(f"Protocólo: {proto}")
        lport = nm[target_ip][proto].keys()
        for port in lport:
            print(f"Porta {port} - Estado: {nm[target_ip][proto][port]['state']}")

# Teste com um IP específico ou faixa de IPs

scan_network('192.168.1.1')  # Exemplo de IP para escanear

