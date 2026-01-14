import os
import logging

log_file = "devops_log.txt"
logging.basicConfig(filename=log_file, level=logging.DEBUG, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def limpar_arquivos_temp():
    logging.info("Iniciando a tarefa DevOps: Limpando arquivos temporários...")
    arquivos = ["tmp_file1.txt", "tmp_file2.log"]
    
    for arquivo in arquivos:
        if os.path.exists(arquivo):
            os.remove(arquivo)
            logging.info(f"Arquivo {arquivo} removido.")
        else:
            logging.warning(f"Arquivo {arquivo} não encontrado.")
    
    logging.info("Tarefa de limpeza concluída.")

def contar_arquivos_txt():
    caminho = "./devops"
    arquivos_txt = [f for f in os.listdir(caminho) if f.endswith('.txt')]
    
    if arquivos_txt:
        logging.info(f"Arquivos .txt encontrados: {', '.join(arquivos_txt)}")
    else:
        logging.info("Nenhum arquivo .txt encontrado.")
    
    return len(arquivos_txt)

def main():
    logging.info("Iniciando o script DevOps...")
    
    limpar_arquivos_temp()
    
    total_txt = contar_arquivos_txt()
    
    logging.info(f"Total de arquivos .txt encontrados: {total_txt}")
    logging.info("Execução do script concluída.")
    
if __name__ == "__main__":
    main()
