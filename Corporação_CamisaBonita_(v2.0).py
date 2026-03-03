class Roupa: 
    
    def __init__(self):
        self.tamanhos = ["PP", "P", "M", "G", "GG", "XG", "XGG"]
        self.tecidos = ["Algodão", "Poliester", "Linho", "Seda", "Elastano"]
        self.cores = ["Vermelho Cereja/Carmim", "Azul Royal/Cobalto", "Lavanda", "Rosa Choque", "Verde Limão", "Preto", "Branco"]
        self.total = 0.0
        self.quantidade = None
        self.cor_escolhida = None
        self.tecido_escolhido = None
        self.tamanho_escolhido = None

    def resolucao(self):

        print("\n--- Resumo do Pedido ---")
        print("O melhor jeito é o seu!")
        print(f"Cor: {self.cor_escolhida}")
        print(f"Tamanho: {self.tamanho_escolhido}")
        print(f"Tecido: {self.tecido_escolhido}")
        print(f"O preço total é R$ {self.total:.2f}")

    def escolha_tamanho(self):

        print("\nQual será o tamanho da sua camiseta?")
        for i, tamanho in enumerate(self.tamanhos, start=1):
            print(f"[{i}] {tamanho}")
        
        while True:
            try:
                num = int(input("Digite o número respectivo ao tamanho: "))
                if 1 <= num <= len(self.tamanhos):
                    self.tamanho_escolhido = self.tamanhos[num - 1]
                    break
                print("Não existe essa opção!")
            except ValueError:
                print("Erro: Digite apenas números inteiros!")

    def escolha_tecido(self):

        print("\nQual será o tecido escolhido?")
        for i, tecido in enumerate(self.tecidos, start=1):
            print(f"[{i}] {tecido}")

        while True:
            try:
                n = int(input("Digite o número respectivo ao tecido: "))
                if 1 <= n <= len(self.tecidos):
                    self.tecido_escolhido = self.tecidos[n - 1]
                    break
                print("Não existe essa opção!")
            except ValueError:
                print("Erro: Digite apenas números inteiros!")

    def escolha_cor(self):

        print("\nQual cor será a camiseta?")
        for i, cor in enumerate(self.cores, start=1):
            print(f"[{i}] {cor}")

        while True:

            try:
                num = int(input("Digite o número respectivo à cor: "))
                if 1 <= num <= len(self.cores):
                    self.cor_escolhida = self.cores[num - 1]
                    break
                print("Não existe essa opção!")       
            except ValueError:
                print("Erro: Digite apenas números!")

    def quantidade_total(self):

        self.quantidade = int(input("Qual o número de camisetas você vai querer? "))

        while True:

            if isinstance(self.quantidade, (int)):
                break
            else:
                print("Digite apenas números!")

         
             
    def valor_total(self):

        if self.tecido_escolhido == "Algodão":
            self.total = 60.00 * self.quantidade
        elif self.tecido_escolhido == "Poliester":
            self.total = 50.00 * self.quantidade
        elif self.tecido_escolhido == "Linho":
            self.total = 70.00 * self.quantidade
        elif self.tecido_escolhido == "Seda":
            self.total = 75.00 * self.quantidade
        else: 
            self.total = 55.00 * self.quantidade


camiseta1 = Roupa()
camiseta1.escolha_tamanho()
camiseta1.escolha_tecido()
camiseta1.escolha_cor()
camiseta1.quantidade_total()
camiseta1.valor_total()
camiseta1.resolucao()
