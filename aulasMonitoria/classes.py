class Carro:
    def __init__(self, marca, modelo, ano, cor):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.velocidade = 0
        self.ligado = False

    def ligar(self):
        if not self.ligado:
            self.ligado = True
            print("O carro está ligado.")
        else:
            print("O carro já está ligado.")

    def desligar(self):
        if self.ligado:
            self.ligado = False
            self.velocidade = 0
            print("O carro está desligado.")
        else:
            print("O carro já está desligado.")

    def acelerar(self, velocidade):
        if self.ligado:
            self.velocidade += velocidade
            print(f"O carro acelerou para {self.velocidade} km/h.")
        else:
            print("Não é possível acelerar, o carro está desligado.")

    def frear(self, velocidade):
        if self.ligado:
            if self.velocidade - velocidade >= 0:
                self.velocidade -= velocidade
                print(f"O carro reduziu a velocidade para {self.velocidade} km/h.")
            else:
                self.velocidade = 0
                print("O carro parou completamente.")
        else:
            print("Não é possível frear, o carro está desligado.")

# Criando um objeto da classe Carro
meu_carro = Carro("Toyota", "Corolla", 2022, "Preto")

# Testando os métodos
meu_carro.ligar()
meu_carro.acelerar(50)
meu_carro.frear(20)
meu_carro.desligar()
