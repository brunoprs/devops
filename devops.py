import datetime
import os


def gerar_log():
    data_atual = datetime.datetime.now()
    log_mensagem = f"Execução realizada em: {data_atual.strftime('%Y-%m-%d %H:%M:%S')}\n"
    

    with open("log.txt", "a") as log_file:
        log_file.write(log_mensagem)
    print(f"Log gerado em: {data_atual.strftime('%Y-%m-%d %H:%M:%S')}")


def tarefa_devops():
    print("Iniciando a tarefa DevOps: Limpando arquivos temporários...")
    arquivos_para_limpar = ["tmp_file1.txt", "tmp_file2.log"]  
    for arquivo in arquivos_para_limpar:
        if os.path.exists(arquivo):
            os.remove(arquivo)
            print(f"Arquivo {arquivo} removido com sucesso.")
        else:
            print(f"Arquivo {arquivo} não encontrado.")


def main():
    gerar_log()   
    tarefa_devops()  

if __name__ == "__main__":
    main()
