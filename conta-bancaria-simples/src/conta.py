class Conta:

    def __init__(self, numero: int, saldo: float, limite=100):
        self.numero = numero
        self.limite = limite
        self.saldo = saldo + limite
        self.extrato = []

    def getNumero(self):
        return self.numero

    def getSaldo(self):
        return self.saldo

    def getLimite(self):
        return self.limite

    def sacar(self, valor: float):
        if valor < 0:
            print("Desculpe! Não é possível sacar um valor negativo.")
            return False
        elif valor > self.saldo:
            print("Desculpe! O valor do saque é maior que o saldo da sua conta.")
            return False
        elif valor > self.saldo - self.limite:
            self.limite = self.saldo - valor
            self.saldo = valor
            self.extrato.append(-valor)
            print("Saque no valor de R$", valor, "realizado com sucesso!")
            return True
        elif valor == self.saldo:
            self.saldo -= valor
            self.extrato.append(-valor)
            print("Sacando todo o dinheiro da conta!")
            return True
        elif valor < self.saldo:
            self.saldo -= valor
            self.extrato.append(-valor)
            print("Saque no valor de R$", valor, "realizado com sucesso!")
            return True

    def depositar(self, valor: float):
        if valor <= 0:
            print("Não é possível realizar o depósito desse valor.")
            return False
        else:
            valor_saldo = valor - self.limite
            if valor_saldo > 0:
                self.limite = 100
                print("Limite restaurado!")
            self.saldo += valor
            self.extrato.append(+valor)
            print("Depósito no valor de R$", valor, "realizado com sucesso!")
            return True

    def transferir(self, destino, valor: float):
        if destino == 0:
            print("Digite o número de uma conta existente.")
        elif valor < 0:
            print("Desculpe! O valor mínimo de transferência é 0.")
            return False
        elif valor > self.saldo:
            print("Não é possível realizar a transferência. O saldo da conta é insuficiente. Por favor, realize um depósito.")
            return False
        else:
            self.saldo -= valor
            saldo_menos_limte = self.saldo - self.limite - valor
            self.limite = self.limite - saldo_menos_limte
            self.extrato.append(-valor)
            destino.depositar(valor)
            print("Transferência no valor de: R$", valor, "realizada com sucesso!")
            return True

    def verExtrato(self):
        print("Extrato Bancário - Lista de Operações Finaceiras.")
        return self.extrato