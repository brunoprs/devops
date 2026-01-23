import os
import sys
from datetime import datetime

APP_ENV = os.getenv("APP_ENV", "dev").lower()
ENABLE_ROLLBACK = os.getenv("ENABLE_ROLLBACK", "false").lower() == "true"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DEVOPS_DIR = os.path.join(BASE_DIR, "devops_files")

LOG_FILE = os.getenv(
    "DEVOPS_LOG_FILE",
    "/var/log/devops-pipeline.log"
)

def log_mensagem(mensagem, fatal=False):
    """
    Registra logs.
    - DEV: nunca quebra
    - STAGE/PROD: quebra se fatal
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    linha = f"{timestamp} - [{APP_ENV.upper()}] {mensagem}"

    print(linha)

    try:
        with open(LOG_FILE, "a") as arquivo_log:
            arquivo_log.write(linha + "\n")

    except Exception as erro:
        print(
            f"{timestamp} - "
            f"[{APP_ENV.upper()}] "
            f"FALHA AO ESCREVER LOG: {erro}"
        )

        if APP_ENV in ("stage", "prod") and fatal:
            print("HEALTHCHECK_FAIL")
            sys.exit(1)

        return

def garantir_diretorio():
    if not os.path.exists(DEVOPS_DIR):
        os.makedirs(DEVOPS_DIR)
        log_mensagem(f"Diretório criado: {DEVOPS_DIR}")
    else:
        log_mensagem(f"Diretório já existe: {DEVOPS_DIR}")


def contar_arquivos_txt():
    arquivos_txt = [
        arquivo
        for arquivo in os.listdir(DEVOPS_DIR)
        if arquivo.endswith(".txt")
    ]

    total = len(arquivos_txt)
    log_mensagem(f"Total de arquivos .txt encontrados: {total}")

    return total


def limpar_arquivos_temp():
    arquivos_temp = ["tmp_file1.txt", "tmp_file2.log"]

    log_mensagem("Iniciando limpeza de arquivos temporários...")

    for arquivo in arquivos_temp:
        caminho = os.path.join(DEVOPS_DIR, arquivo)

        if os.path.exists(caminho):
            os.remove(caminho)
            log_mensagem(f"Arquivo removido: {arquivo}")
        else:
            log_mensagem(
                f"Arquivo {arquivo} não encontrado, pulando..."
            )

def main():
    log_mensagem("Iniciando tarefas DevOps (healthcheck runtime)...")

    try:
        garantir_diretorio()
        limpar_arquivos_temp()

        total_txt = contar_arquivos_txt()
        log_mensagem(
            f"Contagem final de arquivos .txt: {total_txt}"
        )

        log_mensagem("Healthcheck concluído com sucesso!")
        print("HEALTHCHECK_OK")

    except Exception as erro:
        log_mensagem(
            f"Erro inesperado: {erro}",
            fatal=True
        )


if __name__ == "__main__":
    main()
