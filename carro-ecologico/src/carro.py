class Carro:

    def __init__(self):
        self.Combustivel = 0
        self.Passageiros = 0
        self.Quilometragem = 0

    def getPassageiros(self):
        return self.Passageiros

    def getCombustivel(self):
        return self.Combustivel

    def getQuilometragem(self):
        return self.Quilometragem

    def embarcar(self):
        if self.Passageiros == 2:
            return False
        else:
            self.Passageiros += 1
            return True

    def desembarcar(self):
        if self.Passageiros == 0:
            return False
        else:
            self.Passageiros -= 1
            return True

    def dirigir(self, distancia):
        if self.Passageiros > 0:
            if self.Combustivel > 0:
                if distancia > self.Combustivel:
                    print("A distância percorrida foi de: ", self.Combustivel, "! Abasteça o veículo.")
            self.Combustivel = self.Combustivel - distancia
            self.Quilometragem += distancia
            return True
        return False

    def abastecer(self, quantidade):
        if quantidade < 0:
            return False
        elif quantidade > 100:
            combustivel_residual = quantidade - 100
            self.Combustivel += quantidade - combustivel_residual
            return True
        elif quantidade < 100:
            self.Combustivel += quantidade
            return True
        return False
