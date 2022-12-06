# MQTT

O presente projeto é destinado a disciplina de Sistemas Distribuídos da Universidade Federal do Maranhão, com o propósito de implementar o MQTT. 

### Definições rápidas

MQTT is an OASIS standard messaging protocol for the Internet of Things (IoT). It is designed as an extremely lightweight publish/subscribe messaging transport that is ideal for connecting remote devices with a small code footprint and minimal network bandwidth.  [mqtt.org](https://mqtt.org/)

MQTT (originally an initialism of MQ Telemetry Transport[a]) is a lightweight, publish-subscribe, machine to machine network protocol for Message queue/Message queuing service. It is designed for connections with remote locations that have devices with resource constraints or limited network bandwidth. It must run over a transport protocol that provides ordered, lossless, bi-directional connections—typically, TCP/IP. [Wikipedia](https://en.wikipedia.org/wiki/MQTT)

## 🚀 Começando

Essas instruções permitirão que você obtenha uma cópia do projeto em operação na sua máquina local para fins de desenvolvimento e teste.

```
- git clone https://github.com/vinisantosn/Projeto-MQTT.git

- outra opção é baixar o repositório e replicar em sua máquina.

```

## ⚙️ Executando os testes

Atenção antes de prosseguir com os testes você deve instalar a biblioteca paho-mqtt podendo ser através do comando 'pip install paho-mqtt' ou consultando a documentação. 

```
Abaixo segue o relato de como foi feito os testes pelo autor

- No primeiro terminal do Visual Studio Code foi executado o seguinte comando '> python .\mqtt-pub.py ' 
- Segundo terminal executou-se '> python .\mqtt-sub-1-topic.py'
- Terceiro terminal executou-se '> python .\mqtt-sub-2-topics.py'
  

```

Vejamos:

![alt text](https://github.com/vinisantosn/Projeto-MQTT/blod/master/gifs/simulation.gif)

## 🛠️ Construído com

As ferramentas e tecnologias utilizadas na criação do projeto. 

* [Python](https://www.python.org/) - Linguagem de programação utilizada. 

* [Paho-MQTT](https://pypi.org/project/paho-mqtt/) - Biblioteca utilizada. 


## Expressões de gratidão

* Agradeço a professora da disciplina supracitada que proporciona a prática de projetos, que em minha opnião fomenta mais conhecimento e auxilia no portifólio profissional. 
