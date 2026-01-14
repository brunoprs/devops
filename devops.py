import os
import time

def create_temp_file(file_name):
    with open(file_name, 'w') as file:
        file.write(f"This is a temporary file created by DevOps process. Created at {time.ctime()}.\n")

def cleanup_temp_files():
    files_to_cleanup = ['tmp_file1.txt', 'tmp_file2.log', 'tmp_file3.txt']
    
    for file in files_to_cleanup:
        if os.path.exists(file):
            os.remove(file)
            print(f"Arquivo {file} removido com sucesso.")
        else:
            print(f"Arquivo {file} não encontrado.")

def devops_task():
    print(f"Log gerado em: {time.ctime()}")
    
    print("Iniciando a tarefa DevOps: Limpando arquivos temporários...")
    cleanup_temp_files()

    print("Criando novos arquivos temporários...")
    create_temp_file('tmp_file1.txt')
    create_temp_file('tmp_file2.log')
    create_temp_file('tmp_file3.txt')  

if __name__ == "__main__":
    devops_task()
