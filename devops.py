import os
import sys
from datetime import datetime

#DEV, STAGE E PROD

ENV = os.getenv("ENV", "dev").lower()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DEVOPS_DIR = os.path.join(BASE_DIR, "devops_files")

if ENV == "prod":
    LOG_FILE = "/var/log/devops-pipeline.log"
elif ENV == "stage":
    LOG_FILE = os.path.join(BASE_DIR, "devops_stage.log")
else:  
    LOG_FILE = os.path.join(BASE_DIR, "devops_dev.log")


def log_mensagem(mensagem):
    """
    Registra logs no console e em arquivo.
    Em STAGE e PROD, falha de log é erro crítico.
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    linha = f"{timestamp} - [{ENV.upper()}] {mensagem}"

    print(linha)

    try:
        with open(LOG_FILE, "a") as arquivo_log:
            arquivo_log.write(linha + "\n")
    except Exception as erro:
        print(
            f"{timestamp} - [{ENV.upper()}] "
            f"FALHA AO ESCREVER LOG: {erro}"
        )

        if ENV in ("stage", "prod"):
            sys.exit(1)


def garantir_diretorio():
    """
    Garante que o diretório base existe
    """
    if not os.path.exists(DEVOPS_DIR):
        os.makedirs(DEVOPS_DIR)
        log_mensagem(f"Diretório criado: {DEVOPS_DIR}")
    else:
        log_mensagem(f"Diretório já existe: {DEVOPS_DIR}")


def contar_arquivos_txt():
    """
    Conta arquivos .txt no diretório DevOps
    """
    if not os.path.exists(DEVOPS_DIR):
        log_mensagem("Diretório não existe para contagem de arquivos.")
        return 0

    arquivos_txt = [
        f for f in os.listdir(DEVOPS_DIR)
        if f.endswith(".txt")
    ]

    total = len(arquivos_txt)
    log_mensagem(f"Total de arquivos .txt encontrados: {total}")
    return total


def limpar_arquivos_temp():
    """
    Remove arquivos temporários conhecidos
    """
    arquivos_temp = ["tmp_file1.txt", "tmp_file2.log"]
    log_mensagem("Iniciando limpeza de arquivos temporários...")

    for arquivo in arquivos_temp:
        caminho = os.path.join(DEVOPS_DIR, arquivo)

        if os.path.exists(caminho):
            os.remove(caminho)
            log_mensagem(f"Arquivo removido: {arquivo}")
        else:
            log_mensagem(f"Arquivo {arquivo} não encontrado, pulando...")


def main():
    log_mensagem("Iniciando tarefas DevOps (healthcheck runtime)...")

    try:
        garantir_diretorio()
        limpar_arquivos_temp()

        total_txt = contar_arquivos_txt()
        log_mensagem(f"Contagem final de arquivos .txt: {total_txt}")

        log_mensagem("Healthcheck concluído com sucesso!")
        print("HEALTHCHECK_OK")

    except Exception as erro:
        log_mensagem(f"Erro inesperado: {erro}")
        print("HEALTHCHECK_FAIL")
        sys.exit(1)


if __name__ == "__main__":
    main()
