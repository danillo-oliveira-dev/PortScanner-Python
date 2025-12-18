import socket
import sys
from datetime import datetime

# Banner informativo para interface de linha de comando (CLI)
print("-" * 50)
print("ALVO: Scanner de Portas Simples (TCP)")
print("-" * 50)

# Input do alvo
target_input = input("Digite o IP ou Host para escanear: ")

try:
    # Resolução de DNS: Converte hostname (ex: google.com) para IPv4
    target = socket.gethostbyname(target_input)
    print(f"\nAlvo identificado: {target}")
    print(f"Iniciando varredura em: {datetime.now()}")
    print("-" * 50)

except socket.gaierror:
    print("\n[!] Erro: Não foi possível resolver o hostname.")
    sys.exit()

# Lista de portas comuns para enumeração rápida (Reconnaissance)
# Inclui serviços padrões como FTP, SSH, DNS, HTTP, HTTPS, MySQL, RDP, etc.
common_ports = [21, 22, 23, 25, 53, 80, 110, 135, 139, 443, 445, 3306, 3389, 8080]

try:
    for port in common_ports:
        # Configuração do Socket:
        # AF_INET = IPv4 | SOCK_STREAM = Protocolo TCP
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Timeout definido para 0.5s para agilizar a varredura em portas filtradas/fechadas
        s.settimeout(0.5)
        
        # connect_ex retorna 0 em caso de sucesso (Handshake TCP completado)
        result = s.connect_ex((target, port))
        
        if result == 0:
            print(f"[+] Porta {port}: ABERTA")
            
        # Fechamento do socket para liberar recursos do sistema
        s.close()

except KeyboardInterrupt:
    print("\n\n[!] Operação cancelada pelo usuário.")
    sys.exit()

except socket.error:
    print("\n[!] Erro de conexão com o servidor.")
    sys.exit()

print("-" * 50)
print("Varredura finalizada.")