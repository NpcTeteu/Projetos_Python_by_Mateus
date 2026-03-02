class roupa:
    
    def __init__ (self):
        self.tamanhos = ["P","M","G"]
        self.tecidos = ["Algodão","Poliester"]
        self.cores = ["Vermelho Cereja/Carmim", "Azul Royal/Cobalto", "Lavanda"]
        self.total = None
        self.cor_escolhida = None
        self.tecido_escolhido = None
        self.tamanho_escolhido = None

    def resolução(self):

        print("O melhor jeito é o seu!\n")
        print(f"Cor: {self.cor_escolhida}")
        print(f"Tamanho: {self.tamanho_escolhido}")
        print(f"Tecido: {self.tecido_escolhido}\n")
        print("O preço total é {:.2f}".format(self.total))

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

        print("Qual será o tecido escolhido? ")
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


    def escolha_cor(self):

        print("Qual cor será a camiseta? ")
        for p,cor in enumerate (self.cores, start=1):
            print(f"[{p}] {cor}")

        while True:

            try:
                Num = int(input("Digite o número respectivo a cor: "))
                if 1 <= Num <= len(self.cores):
                    self.cor_escolhida = self.tecidos[Num -1]
                    break
                else:
                    print("Não existe essa opção!")       
            except ValueError:
                print("Digite apenas números")

    def valor_total (self):

        if self.tecido_escolhido == "Algodão":
            self.total = 60.00
        
        else:
            self.total = 50.00

camiseta1 = roupa()
camiseta1.escolha_tamanho()
camiseta1.escolha_tecido()
camiseta1.escolha_cor()
camiseta1.valor_total()
camiseta1.resolução()



    
    
