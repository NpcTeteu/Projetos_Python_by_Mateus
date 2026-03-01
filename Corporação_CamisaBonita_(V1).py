class roupa:
    
    def __init__ (self,cor):
        self.cor = cor
        self.tamanhos = ["P","M","G"]
        self.tecidos = ["Algodão","Poliester"]
        self.tecido_escolhido = None
        self.tamanho_escolhido = None

    def resolução(self):

        print("O melhor jeito é o seu!\n")
        print(f"Cor: {self.cor}")
        print(f"Tamanho: {self.tamanho_escolhido}")
        print(f"Tecido: {self.tecido_escolhido}\n")
        print(f"O preço total é ....")

    def escolha_tamanho(self):

        print("Qual será o tamanho da sua camiseta?")

        for i,tamanho in enumerate (self.tamanhos, start = 1):
            print(f"[{i}] {tamanho}")
        
        while True:
            try:

                num = int(input("Digite o número respectivo ao tamanho: "))

                if 1 <= num <= len(self.tamanhos):
                    self.tamanho_escolhido = self.tamanhos[num - 1]
                    break

                else:
                    print("Não existe essa opção!")

            except ValueError:
                print("Digite apenas números!")

    def escolha_tecido(self):

        print("Qual será o tecido escolhido? : ")

        for o,tecido in enumerate (self.tecidos, start = 1):
            print(f"[{o}] {tecido}")

        while True:
            try:

                N = int(input("Digite o número respectivo ao tecido: "))

                if 1 <= N <= len(self.tecidos):
                    self.tecido_escolhido = self.tecidos[N -1]
                    break

                else:
                    print("Não existe essa opção!")

            except ValueError:
                print("Digite apenas números!")


camiseta1 = roupa("Azul")
camiseta1.escolha_tamanho()
camiseta1.escolha_tecido()
camiseta1.resolução()



    
    
