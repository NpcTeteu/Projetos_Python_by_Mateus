Name_A = input("Como você se chama?\n")
Hobs_A = input("Qual é o seu hobbie principal?\n")
Temp_A = input("Você se considera uma pessoa de qual temperamento?\n")
Gost_A = input("Para você, oque não pode faltar em alguém para ser seu namorado(a)?\n")
print("---")
Name_B = input("Como você se chama?\n")
Hobs_B = input("Qual é o seu hobbie principal?\n")
Temp_B = input("Você se considera uma pessoa de qual temperamento?\n")
Gost_B = input("Para você, oque não pode faltar em alguém para ser seu namorado(a)?\n")
print("---")
User_A = (f"Gosto de {Hobs_A}, e eu sou {Temp_A}")
User_B = (f"Gosto de {Hobs_B}, e eu sou {Temp_B}")

print(f"{Name_A} encontrou o(a) {Name_B}")
print(f"{Name_A} e {Name_B} começaram a conversar")
print(f"{Name_A} perguntou sobre {Name_B} e ela(e) disse:")
print(f"{User_B}")
print(f"{Name_A} percebeu ")
print(f"E {Name_B} fez o mesmo com {Name_A}")
print(f"{Name_A} disse:")
print(f"{User_A}")
print(f"E eles(a) ficaram por mais algum tempo")
print(f"Então {Name_B} avisou que tinha que ir embora")
print(f"Coincidentemente {Name_A} teve que sair também")

Deci_A = input(f"{Name_A}, você gostou da(o) {Name_B}? [S] ou [N]").upper
Deci_B = input(f"{Name_B}, você gostou da(o) {Name_B}? [S] ou [N]").upper

if Deci_A == "S" and Deci_B == "S":
    print(f"Mas olha só, parece que {Name_A} e {Name_B} gostaram um do outro")
else:
    print(f"Que pena, pelo jeito {Name_A} e {Name_B} não deram muito certo, mas ainda tem 1.999.999.999 de novas posiibilidades")
