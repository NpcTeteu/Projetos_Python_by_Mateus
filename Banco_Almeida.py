"""
saldo = 0
deposito = int(input("Digite o valor do depósito"))
saque = int(input("Digite o valor do saque"))

"""

class Conta:

    def __init__ (self):
        self.saldo = 0
        self.tentativas_saque = 4
        self.quantidade_max_depósito = 4

    def depositar (self):

        while True:

            deposito = float(input("Digite o valor para depositar (ou digite ""3"" para voltar ao menu): "))

            if deposito <=0:
                print("Digite um valor maior do que 0!")

            if deposito >0 and deposito != 3:
                self.saldo += deposito
                self.quantidade_max_depósito -= 1
                print(f"Você depositou {deposito}")
                print(f"Você pode apenas fazer mais {self.quantidade_max_depósito} depósitos")

            if self.quantidade_max_depósito == 0:
                print("Quantidade máxima de depósitos alcançada!")
                break

            if deposito == 3:
                self.operação()


    def sacar (self):

        saque = float(input("Digite o valor do saque (ou digite ""3"" para voltar ao menu): "))
        
        while True:

            if saque < self.saldo:
                self.saldo -= saque    
                print(f"Seu saldo atual é de {self.saldo}")
                break

            if saque > self.saldo:
                saque = float(input("Digite o valor possível para o saque: "))
                self.tentativas_saque -= 1
                print(f"Você tem apenas {self.tentativas_saque} tentativa")

            if self.tentativas_saque == 0:
                print("Você esgotou as tentativas")
                break

            if saque == 3:
                self.operação()


    def operação (self):

        while True:

            print("--------------- Operações --------------")
            print("[1] Sacar")
            print("[2] Depositar")
            print("[3] Finalizar")
            print("----------------------------------------")
            escolha = int((input("Escolha uma das ações: ")))

            """-----------------------------------------------------"""

            if escolha > 3 or escolha < 0 :
                print("Você digitou uma opção que não existe, tente de novo!")

            if escolha == 1 and self.saldo <=0:
                print()
                print("Você não tem saldo nenhum!")
                print()

            if escolha == 1 and self.tentativas_saque == 0:
                print()
                print("Você esgotou seu número de tentativas")
                print()

            if escolha == 1 and self.saldo >0 and self.tentativas_saque >0:
                self.sacar()

            """-----------------------------------------------------"""
            
            if escolha == 2 and self.quantidade_max_depósito >0:
                self.depositar()

            if escolha == 2 and self.quantidade_max_depósito <=0:
                print("Você não pode mais depositar hoje!")



            if escolha == 3:
                print("Adeus!!!")
                break
       

conta1 = Conta()
conta1.operação()