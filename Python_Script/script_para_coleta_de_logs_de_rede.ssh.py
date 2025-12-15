import paramiko

# Função para coletar logs via SSH

def collect_logs(hostname, username, password, log_file_path):

# Conectando via SSH

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(hostname, username=username, password=password)
        print(f"Conectado com sucesso em {hostname}")

# Comando para obter os logs (aqui exemplificando a coleta do log do sistema)

        stdin, stdout, stderr = ssh.exec_command(f'cat {log_file_path}')
        logs = stdout.read().decode()

# Salvar logs em um arquivo local

        with open('collected_logs.txt', 'w') as file:
            file.write(logs)

        print("Logs coletados com sucesso.")

    except Exception as e:
        print(f"Erro ao conectar ou coletar os logs: {e}")
    finally:
        ssh.close()

# Exemplo de uso

collect_logs('192.168.1.100', 'user', 'password', '/var/log/syslog')