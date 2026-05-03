class MonitorServidores:
    
    def __init__(self):
        self.servidores =[]

    def adicionar_servidor(self, servidor):
            self.servidores.append(servidor)

    def listar_servidores(self):
        print("\n--- MONITORAMENTO ---")

        for servidor in self.servidores:
            
            print(
                f"{servidor.nome} | "
                f"Temp: {servidor.temperatura}º | "
                f"Status: {servidor.status()}"
            )

    def atualizar_temperatura(self, nome, nova_temp):
        
        for servidor in self.servidores:
            
            if servidor.nome == nome:
                servidor.temperatura = nova_temp
                return
            
        print("servidor não encontrado")



