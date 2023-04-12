import threading
import time

def minha_funcao():
    # código da thread
    print("Iniciando a thread...")
    # faça algo aqui...
    time.sleep(10)  # faz a thread esperar por 10 segundos
    print("Finalizando a thread...")

# cria uma nova thread
thread = threading.Thread(target=minha_funcao)

# inicia a thread
thread.start()

# espera até que a thread termine antes de continuar com o código principal
thread.join()

# o programa agora pode continuar com outras tarefas
print("A thread foi finalizada.")
