class Servidor:

    def __init__(self, nome, temperatura):
        self.nome = nome
        self._temperatura = temperatura

    @property
    def temperatura(self):
        return self._temperatura
    
    @temperatura.setter
    def temperatura(self, valor):

        if valor < 0:
            print(f"[ERRO] Temperatura inválida {self.nome}")

        elif valor > 100:
            print(f"[ALERTA CRÍTICO] {self.nome} ultrapassou limite!")
            self._temperatura = valor

        else:
            self._temperatura = valor

    def status(self):

        if self._temperatura < 50:
            return "Normal"
        
        elif self._temperatura < 80:
            return "Alta"
        
        else: 
            return "Perigo"