from pathlib import Path
URL_PREVISAO = "https://api.weatherapi.com/v1/forecast.json"
import requests
from datetime import datetime
import locale
locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')

arquivo = Path("SaveApiKey.txt")

if arquivo.exists():
    CHAVEAPI = arquivo.read_text().strip()
    print("Chave API foi encontrada!")

else:
    print("Para que possemos consultar o tempo e previsão do tempo,\n" \
    "é necessário uma chave API, para isso, acesse o site https://www.weatherapi.com/\n" \
    "e crie uma conta gratuita para obter a sua chave API.")
    CHAVEAPI = input("Digite sua chave API: ").strip()
    arquivo.write_text(CHAVEAPI)

sair = ""
def previsao_atual(cidade):

    parametros = {
        "key": CHAVEAPI,
        "q": cidade,
        "lang": "pt"
    }

    resposta = requests.get(URL_PREVISAO, params=parametros)
    dados = resposta.json()

    atual = dados["current"]

    print("\nCidade:", dados["location"]["name"])
    print("Temperatura:", atual["temp_c"], "°C")
    print("Condição:", atual["condition"]["text"])
def previsao_futuro(cidade,dias):
    #Define os parametros para enviar para a API
    paramentros = {
        "key": CHAVEAPI,
        "q": cidade,
        "lang": "pt",
        "days": dias+1
    }
    #Manda a requisição para a API e obtém os dados
    resposta = requests.get(URL_PREVISAO, params=paramentros)
    dados = resposta.json()
    dia = dados["forecast"]["forecastday"][dias]
    
    #Tratramento de exibição dos dados
    
    #Exibe o nome da cidade
    print("\nCidade:", dados["location"]["name"])
    
    #Coleta a data do dia da previsão e converte para o formato datetime
    data = datetime.strptime(dia["date"], "%Y-%m-%d")

    #Exibe a data formatada para o padrão brasileiro ex (25/12/2024)
    data_br = data.strftime("%d/%m/%Y")
    print("Data:", data_br)

    #Exibe os dias da semana formatados para o padrão brasileiro ex (Quarta-feira)
    dia_semana = data.strftime("%A")      # nome do dia
    print("Dia:", dia_semana.capitalize())

    #Exibe a temperatura média e a condição do dia da previsão
    print("Temperatura média:", dia["day"]["avgtemp_c"], "°C")
    print("Previsão:", dia["day"]["condition"]["text"])

    match Opcao:
        case "1":
            cidade = input("Digite o nome da cidade para obter a previsão do tempo atual: ")
            previsao_atual(cidade)
            
        case "2":
            cidade = input("Digite o nome da cidade para obter a previsão do tempo para os próximos dias: ")
            dia = int(input("Digite o dia para obter a previsão do tempo: "))
            if dia > 2 or dia < 0:
                print("Lamento mas a Aplicação só tem previsão para os próximos 3 dias," \
                "por favor escolha um número entre 0 e 2.")
                
            previsao_futuro(cidade,dia)
        
while sair not in ["s","n"]:

    Opcao = input("\nQual das opções abaixo você deseja utilizar?\n" \
    "1 - Previsão do tempo atual\n" \
    "2 - Previsão do tempo para os próximos dias\n" \
    "3 - Sair\n" \
    "Digite o número da opção desejada: ")

    opcoes = ["1","2","3"]
    if Opcao not in opcoes:
        print("Opção inválida. Por favor, escolha 1, 2 ou 3.")
        continue
    
    match Opcao:
        case "1":
            cidade = input("Digite o nome da cidade para obter a previsão do tempo atual: ")
            previsao_atual(cidade)
            

        case "2":
            Opcao = ""
            cidade = input("Digite o nome da cidade para obter a previsão do tempo para os próximos dias: ")
            diaescolhido = int(input("Digite o dia para obter a previsão do tempo: "))
            
            while diaescolhido not in [0,1,2]:
                diaescolhido = int(input("Escolha 0, 1 ou 2: "))
            previsao_futuro(cidade,diaescolhido)

        case "3":
            print("ATE LOGO!")
            sair = "s"
            
        
    
   