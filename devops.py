import os
import datetime
import sys


def log_mensagem(mensagem):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"{timestamp} - {mensagem}")


def contar_arquivos_txt():
    caminho = './devops'  
    try:
        if not os.path.exists(caminho):
            raise FileNotFoundError(f"O diretório {caminho} não foi encontrado!")
        
        arquivos_txt = [f for f in os.listdir(caminho) if f.endswith('.txt')]
        log_mensagem(f"Total de arquivos .txt encontrados: {len(arquivos_txt)}")
        return len(arquivos_txt)
    
    except FileNotFoundError as e:
        log_mensagem(f"Erro: {e}")
       
        raise SystemExit("Execução interrompida devido a erro no código.")


def limpar_arquivos_temp():
    arquivos_temp = ['tmp_file1.txt', 'tmp_file2.log']
    caminho = './devops'
    
    log_mensagem("Iniciando limpeza de arquivos temporários...")
    
    for arquivo in arquivos_temp:
        caminho_arquivo = os.path.join(caminho, arquivo)
        if os.path.exists(caminho_arquivo):
            os.remove(caminho_arquivo)
            log_mensagem(f"Arquivo removido: {arquivo}")
        else:
            log_mensagem(f"Arquivo {arquivo} não encontrado, pulando...")

def main():
    log_mensagem("Iniciando tarefas DevOps...")
    
    try:

        limpar_arquivos_temp()
        

        total_txt = contar_arquivos_txt()
        log_mensagem(f"Contagem final de arquivos .txt: {total_txt}")
        
        log_mensagem("Tarefas DevOps concluídas com sucesso!")
    
    except SystemExit as e:
        log_mensagem(str(e))
        sys.exit(1) 

if __name__ == "__main__":
    main()
