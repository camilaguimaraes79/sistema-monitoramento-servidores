# 🖥️ Sistema de Monitoramento de Temperaturas de Servidores

Sistema desenvolvido em Python para monitorar a temperatura de servidores e classificar seu status automaticamente.

## 📋 Funcionalidades

- ✅ Cadastro de servidores
- ✅ Listagem de servidores com temperatura e status
- ✅ Atualização de temperatura em tempo real
- ✅ Classificação automática de status:
  - 🟢 Normal — abaixo de 60°
  - 🟡 Alta — entre 60° e 89°
  - 🔴 Perigo — acima de 90°
- ✅ Validação de temperaturas inválidas

## 📁 Estrutura do Projeto

sistema de monitoramento de servidores/
├── models/
│   └── servidor.py
├── services/
│   └── monitor.py
└── main.py

##  Como rodar o projeto

cd "sistema de monitoramento de servidores"
python main.py

## Tecnologias utilizadas

- Python 3.14
- Orientação a Objetos (POO)
