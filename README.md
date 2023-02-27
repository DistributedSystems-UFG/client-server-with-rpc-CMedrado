# client-server-with-rpc-CMedrado
 
[Video](https://youtu.be/QDLTQ9XMxhY) 
 
As diferenças entre construir a aplicação diretamente sobre sockets e com o uso de suporte de RPC

Quando escrevemos uma aplicação que usa sockets, precisamos lidar diretamente com a comunicação entre cliente e servidor, definindo os formatos de mensagens, estabelecendo conexões, gerenciando erros e assim por diante. É como se precisássemos "inventar a roda" toda vez que quiséssemos criar uma aplicação que se comunica através da rede.

Já no caso do uso de RPC (Remote Procedure Call, ou Chamada de Procedimento Remoto), podemos pensar em uma "caixa preta" que cuida da comunicação entre cliente e servidor para nós. Nesse modelo, podemos simplesmente chamar uma função no cliente e esperar que ela seja executada no servidor, sem precisar nos preocupar com detalhes como estabelecimento de conexão, envio e recebimento de mensagens, entre outros.

O uso de RPC pode trazer algumas vantagens em relação à construção direta sobre sockets, como maior abstração, simplicidade de código e, em alguns casos, melhor desempenho. Por outro lado, pode haver uma certa perda de controle sobre a comunicação, já que muitos detalhes ficam "escondidos" pela abstração do RPC.

Resumindo, o uso de RPC pode ser uma forma mais simples e abstrata de lidar com a comunicação entre cliente e servidor, mas pode não ser a melhor opção em todos os casos, dependendo das necessidades específicas da aplicação.
