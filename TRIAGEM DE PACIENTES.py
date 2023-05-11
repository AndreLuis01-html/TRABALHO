import time
nome =input("DIGITE O SEU NOME :")
idade =int(input("DIGITE A SUA IDADE:"))
if idade >=65:
    print("O PACIENTE " + nome + " POSSUI ATENDIMENTO PRIORITÁRIO,POR FAVOR SE DIRIJA A SALA 01")
else:
    print("O PACIENTE " + nome + " NÃO POSSUI ATENDIMENTO PRIORITÁRIO, POR FAVOR RESPONDA ALGUMAS PERGUNTAS,COM SIM OU NÃO!!:")
    s=int(0)
    n=0
    print()
    articular=input("DOR NO CORPO OU ARTICULAÇÕES:")
    if articular == "s":
        s=s+1
    olhos=input ("DOR ATRÁS DOS OLHOS:")
    if olhos == "s":
        s=s+1
    vom=input("VÔMITO OU DIARRÉIA:")
    if vom == "s":
        s=s+1
    perda = input("PERDA NO OLFATO OU PALADAR:")
    if perda == "s":
        s=s+1
    cabeca = input("DOR DE CABEÇA:")
    if cabeca == "s":
        s=s+1
    manchas =input("MANCHAS VERMELHAS NO CORPO:")
    if manchas == "s":
        s=s+1
    if s>=4 :
        print("DIRIJA-SE PARA A SALA 02, POSSÍVEL CASO DE DENGUE!!")
    else:
        s=0
        print("RESPONDA MAIS ALGUMAS PERGUNTAS PARA UM MELHOR DIAGNÓSTICO!")
        cal=input("TÊM CALAFRIOS:")
        if cal == "s":
            s=s+1
        tos=input("TÊM TOSSE:")
        if tos == "s":
            s=s+1
        gar=input("TÊM DOR NA GARGANTA:")
        if gar == "s":
            s=s+1
        cab=input("TÊM DOR DE CABEÇA:")
        if cab == "s":
            s=s+1
        cong= input("TÊM GONGESTÃO NASAL:")
        if cong == "s":
            s=s+1
        perd = input("PERDA NO OLFATO OU PALADAR:")
        if perd == "s":
            s = s + 1
            if s >= 4:
                print("DIRIJA-SE A SALA 03, POSSÍVEL CASO DE COVID-19!!")
            else:
                print("DIRIJA-SE A SALA 04 PARA UMA CONSULTA DETALHADA!!")

    time.sleep(2940)




