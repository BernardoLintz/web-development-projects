import logging
import schedule
import time
from Python_Script.script_varredura_de_portas import scan_network  # Certifique-se de que o caminho está correto!

# Configuração do logging
logging.basicConfig(
    filename='analise_rede.log', 
    level=logging.INFO, 
    format='%(asctime)s - %(message)s'
)

def job():
    try:
        logging.info("Iniciando análise de rede...")
        scan_network('192.168.1.1')  # Exemplo de IP a ser escaneado
        logging.info("Análise de rede concluída com sucesso.")
    except Exception as e:
        logging.error(f"Erro ao executar a análise de rede: {e}")

# Agendando para rodar a cada 10 minutos
schedule.every(10).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)