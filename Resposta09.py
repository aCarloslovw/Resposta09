import time
import random

# Simulando as lâmpadas
class Lampada:
    def __init__(self, id):
        self.id = id
        self.ligada = False
        self.quente = False

# Criando as lâmpadas
lampadas = [Lampada("A"), Lampada("B"), Lampada("C")]

# Função para ligar e desligar interruptores
def ligar_interruptor(lampada):
    lampada.ligada = True
    lampada.quente = True  # Fica quente quando ligada

def desligar_interruptor(lampada):
    lampada.ligada = False
    lampada.quente = False  # Esfria quando desligada

# Simulando a lógica de descobrir as lâmpadas
def descobrir_lampadas():
    # Ligar o interruptor A
    ligar_interruptor(lampadas[0])
    print("Interruptor A ligado.")
    time.sleep(5)  # Simula o tempo que a lâmpada fica ligada

    # Desligar o interruptor A
    desligar_interruptor(lampadas[0])
    print("Interruptor A desligado.")

    # Ligar o interruptor B
    ligar_interruptor(lampadas[1])
    print("Interruptor B ligado.")

    # Simulando a ida à sala das lâmpadas
    print("Indo à sala das lâmpadas...")
    time.sleep(2)  # Tempo de espera para simular a ida

    # Verificando o estado das lâmpadas
    for lampada in lampadas:
        if lampada.ligada:
            print(f"Lâmpada {lampada.id} está ligada.")
        elif lampada.quente:
            print(f"Lâmpada {lampada.id} está desligada e quente.")
        else:
            print(f"Lâmpada {lampada.id} está desligada e fria.")

# Executar a função
descobrir_lampadas()
