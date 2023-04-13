import threading
import time

def contar_ate_n(n):
    for i in range(1, n+1):
        print(i)
        time.sleep(0.5)

if __name__ == '__main__':
    n1 = int(input('Digite um número inteiro para a primeira thread: '))
    n2 = int(input('Digite um número inteiro para a segunda thread: '))

    thread1 = threading.Thread(target=contar_ate_n, args=(n1,))
    thread2 = threading.Thread(target=contar_ate_n, args=(n2,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print('Contagem finalizada!')