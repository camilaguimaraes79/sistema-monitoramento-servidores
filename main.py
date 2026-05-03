from models.servidor import Servidor
from services.monitor import MonitorServidores

monitor = MonitorServidores()

s1 = Servidor("Servidor web", 45)
s2 = Servidor("Servidor Banco", 52)
s3 = Servidor("Servidor API", 39)

monitor.adicionar_servidor(s1)
monitor.adicionar_servidor(s2)
monitor.adicionar_servidor(s3)

monitor.listar_servidores()

print("\nAtualizando temperaturas...\n")

monitor.atualizar_temperatura("Servidor web", 70)
monitor.atualizar_temperatura("Servidor Banco", 95)
monitor.atualizar_temperatura("Servidor API", -10)

monitor.listar_servidores()



