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

> ## Kernel Linux 

O kernel usado é o Linux na sua versão 4.14, seguida pela 4.19 e 5.4. A versão mais recente do kernel Linux disponível é a 5.12, mas ainda não foi amplamente adotada no Android. [Android Developers 2023] <br> 

> ## Android Runtime

O Android Runtime (ART) é o ambiente de execução de aplicativos usado pelo sistema operacional Android. Ele é responsável por executar o código dos aplicativos em um dispositivo Android <br>

> ## Bibliotecas
As bibliotecas são organizadas em diferentes camadas de acordo com sua finalidade e nível de abstração. As camadas de bibliotecas mais baixas são compostas de bibliotecas nativas, que são escritas em linguagens de programação de baixo nível, como C e C++, e são usadas para acessar recursos do sistema operacional e do hardware, como o sistema de arquivos, a câmera ou o GPS. As bibliotecas de nível mais alto são compostas de código Java, que são usadas para fornecer funcionalidades de alto nível, como a interface do usuário, a lógica de negócios e a comunicação com a rede. <br>

> ## Framework de Aplicação
O Framework de Aplicação é projetado para facilitar o desenvolvimento de aplicativos Android, fornecendo uma estrutura de desenvolvimento consistente e reutilizável. Ele fornece uma variedade de componentes que os desenvolvedores podem usar para criar aplicativos, incluindo Activity, Service, Broadcast Receiver e Content Provider. <br>

> ## Aplicações 
As aplicações são desenvolvidas por terceiros, incluindo empresas, desenvolvedores independentes e organizações governamentais, e são distribuídas através da Google Play Store ou outras lojas de aplicativos. As aplicações podem ser gratuitas ou pagas, e muitas delas oferecem recursos adicionais através de compras dentro do aplicativo.


## Introdução as Threads
Uma thread é a menor unidade de processamento que pode ser agendada pelo sistema operacional para executar uma tarefa em um programa. Em outras palavras, uma thread é uma sequência de instruções de código que pode ser executada simultaneamente com outras sequências de instruções de código em um mesmo programa. <br>
Cada thread possui um registro de pilha de execução próprio, que contém informações sobre as instruções que devem ser executadas e o estado atual do processo. As threads são comumente usadas em programas que precisam executar tarefas em paralelo, ou seja, que precisam executar várias tarefas simultaneamente para aumentar a eficiência do programa ou melhorar a experiência do usuário. <br>
Segue em anexo um código realizado em Python mostrando como é uma thread em execução 
```
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
<br>
<div align="center">
<img src="https://user-images.githubusercontent.com/96505484/231562564-fb429be1-5430-45d3-af25-24663a677b54.png" width="700px" />
</div> 










