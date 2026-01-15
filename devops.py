import os
import datetime
import sys


def log_mensagem(mensagem):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"{timestamp} - {mensagem}")


# Diretório base do projeto (onde o script está)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Diretório para arquivos DevOps (criado automaticamente)
DEVOPS_DIR = os.path.join(BASE_DIR, "devops_files")


def garantir_diretorio():
    if not os.path.exists(DEVOPS_DIR):
        os.makedirs(DEVOPS_DIR)
        log_mensagem(f"Diretório criado: {DEVOPS_DIR}")
    else:
        log_mensagem(f"Diretório já existe: {DEVOPS_DIR}")


def contar_arquivos_txt():
    arquivos_txt = [f for f in os.listdir(DEVOPS_DIR) if f.endswith('.txt')]
    log_mensagem(f"Total de arquivos .txt encontrados: {len(arquivos_txt)}")
    return len(arquivos_txt)


def limpar_arquivos_temp():
    arquivos_temp = ['tmp_file1.txt', 'tmp_file2.log']

    log_mensagem("Iniciando limpeza de arquivos temporários...")

    for arquivo in arquivos_temp:
        caminho_arquivo = os.path.join(DEVOPS_DIR, arquivo)
        if os.path.exists(caminho_arquivo):
            os.remove(caminho_arquivo)
            log_mensagem(f"Arquivo removido: {arquivo}")
        else:
            log_mensagem(f"Arquivo {arquivo} não encontrado, pulando...")


def main():
    log_mensagem("Iniciando tarefas DevOps...")

    try:
        garantir_diretorio()

        limpar_arquivos_temp()

        total_txt = contar_arquivos_txt()
        log_mensagem(f"Contagem final de arquivos .txt: {total_txt}")

        log_mensagem("Tarefas DevOps concluídas com sucesso!")

    except Exception as e:
        log_mensagem(f"Erro inesperado: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
