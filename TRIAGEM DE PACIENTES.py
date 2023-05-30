import time
# importando biblioteca do mysql.connector
import mysql.connector

# atribuindo os dados de coneccao com o banco de dados remoto
mydb = mysql.connector.connect(
    host="pretriagem.mysql.database.azure.com",
    user="oseias",
    password="Saieso84@",
    database="mydb"
)

# instanciando cursor (ele que vai pemitir executar os codigo SQL)
cursor = mydb.cursor()

# Aqui instanciei as variaveis previamente, caso o programa nao chegar a perguntar elas ja estao prontas para popular o banco
prioritario: str
naoprioritario: str
casodengue: str = "Sem Informação"
casocovid: str = "Sem Informação"

articular: str = "Sem Informação"
olhos: str = "Sem Informação"
vom: str = "Sem Informação"
perda: str = "Sem Informação"
cabeca: str = "Sem Informação"
manchas: str = "Sem Informação"
cal: str = "Sem Informação"
tos: str = "Sem Informação"
gar: str = "Sem Informação"
cab: str = "Sem Informação"
cong: str = "Sem Informação"
perd: str = "Sem Informação"

nome = input("DIGITE O SEU NOME: ")
idade = int(input("DIGITE A SUA IDADE: "))

if idade >= 65:
    # definindo variaveis de atendimento prioritario
    prioritario = "SIM"
    naoprioritario = "NÃO"

    print("O PACIENTE " + nome +
          " POSSUI ATENDIMENTO PRIORITÁRIO,POR FAVOR SE DIRIJA A SALA 01")
else:
    # definindo variaveis de atendimento prioritario
    prioritario = "NÃO"
    naoprioritario = "SIM"

    print("O PACIENTE " + nome +
          " NÃO POSSUI ATENDIMENTO PRIORITÁRIO, POR FAVOR RESPONDA ALGUMAS PERGUNTAS, COM SIM OU NÃO! [s/n]:")

    s = int(0)
    n = 0
    print()
    articular = input("DOR NO CORPO OU ARTICULAÇÕES: ")
    if articular == "s":
        s = s + 1
        articular = "SIM"
    else:
        articular = "NÃO"

    olhos = input("DOR ATRÁS DOS OLHOS: ")
    if olhos == "s":
        s = s + 1
        olhos = "SIM"
    else:
        olhos = "NÃO"

    vom = input("VÔMITO OU DIARRÉIA: ")
    if vom == "s":
        s = s + 1
        vom = "SIM"
    else:
        vom = "NÃO"

    perda = input("PERDA NO OLFATO OU PALADAR: ")
    if perda == "s":
        s = s + 1
        perda = "SIM"
    else:
        perda = "NÃO"

    cabeca = input("DOR DE CABEÇA: ")
    if cabeca == "s":
        s = s + 1
        cabeca = "SIM"
    else:
        cabeca = "NÃO"

    manchas = input("MANCHAS VERMELHAS NO CORPO: ")
    if manchas == "s":
        s = s + 1
        manchas = "SIM"
    else:
        manchas = "NÃO"

    if s >= 4:
        # atribuindo variavel em caso de dengue
        casodengue = "SIM"
        casocovid = "NÃO"
        print("DIRIJA-SE PARA A SALA 02, POSSÍVEL CASO DE DENGUE!!")
    else:
        s = 0
        print("RESPONDA MAIS ALGUMAS PERGUNTAS PARA UM MELHOR DIAGNÓSTICO!")

        cal = input("TÊM CALAFRIOS: ")
        if cal == "s":
            s = s + 1
            cal = "SIM"
        else:
            cal = "NÃO"

        tos = input("TÊM TOSSE: ")
        if tos == "s":
            s = s + 1
            tos = "SIM"
        else:
            tos = "NÃO"

        gar = input("TÊM DOR NA GARGANTA: ")
        if gar == "s":
            s = s + 1
            gar = "SIM"
        else:
            gar = "NÃO"

        cab = input("TÊM DOR DE CABEÇA: ")
        if cab == "s":
            s = s + 1
            cab = "SIM"
        else:
            cab = "NÃO"

        cong = input("TÊM GONGESTÃO NASAL: ")
        if cong == "s":
            s = s + 1
            cong = "SIM"
        else:
            cong = "NÃO"

        perd = input("PERDA NO OLFATO OU PALADAR: ")
        if perd == "s":
            s = s + 1
            perd = "SIM"
        else:
            perd = "NÃO"

        if s >= 4:
            # atribuindo variavel em caso de covid
            casodengue = "NÃO"
            casocovid = "SIM"
            print("DIRIJA-SE A SALA 03, POSSÍVEL CASO DE COVID-19!!")
        else:
            print("DIRIJA-SE A SALA 04 PARA UMA CONSULTA DETALHADA!!")

sql = "INSERT INTO consultas (nome, idade, atendimento_prioritario, atendimento_nao_prioritario, dor_no_corpo_ou_articulaçoes, dor_atras_dos_olhos, vomito_ou_diarreia, perda_no_olfato_ou_paladar, dor_de_cabeça, manchas_vermelhas_no_corpo, possivel_caso_de_dengue, tem_calafrios, tem_tosse, tem_dor_na_garganta, tem_congestao_nasal, possivel_caso_covid_19) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
val = (
nome, idade, prioritario, naoprioritario, articular, olhos, vom, perda, cabeca, manchas, casodengue, cal, tos, gar,
cong, casocovid)
cursor.execute(sql, val)

mydb.commit()
mydb.close()

time.sleep(2940)
