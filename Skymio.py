from pathlib import Path
URL_PREVISAO = "https://api.weatherapi.com/v1/forecast.json"
import requests
from datetime import datetime

DIAS_SEMANA = {
    1: "Domingo",
    2: "Segunda-feira",
    3: "Terça-feira",
    4: "Quarta-feira",
    5: "Quinta-feira",
    6: "Sexta-feira",
    7: "Sábado",
}

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

def mensagem_probabilidade_chuva(chance):
    chance = int(chance)
    if chance > 65:
        return "É melhor levar um guarda-chuva."
    elif chance >= 50:
        return "Pode ser que chova."
    elif chance >= 30:
        return "Vai ter algumas nuvens no céu."
    elif chance >= 10:
        return "Não vai chover."
    else:
        return "Será um dia ensolarado e quase sem nuvens, leve um protetor solar."

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
    if "forecast" in dados and dados["forecast"]["forecastday"]:
        chance_chuva = dados["forecast"]["forecastday"][0]["day"].get("daily_chance_of_rain", 0)
        print(f"Probabilidade de chuva: {chance_chuva}% - {mensagem_probabilidade_chuva(chance_chuva)}")
def previsao_futuro(cidade, numero_dia):
    #Define os parametros para enviar para a API
    paramentros = {
        "key": CHAVEAPI,
        "q": cidade,
        "lang": "pt",
        "days": 3
    }
    #Manda a requisição para a API e obtém os dados
    resposta = requests.get(URL_PREVISAO, params=paramentros)
    dados = resposta.json()
    dia = next(
        (
            previsao
            for previsao in dados["forecast"]["forecastday"]
            if datetime.strptime(previsao["date"], "%Y-%m-%d").isoweekday() % 7 + 1
            == numero_dia
        ),
        None,
    )

    if dia is None:
        print(f"Não há previsão para {DIAS_SEMANA[numero_dia]} nos próximos 3 dias.")
        return
    
    #Tratramento de exibição dos dados
    
    #Exibe o nome da cidade
    print("\nCidade:", dados["location"]["name"])
    
    #Coleta a data do dia da previsão e converte para o formato datetime
    data = datetime.strptime(dia["date"], "%Y-%m-%d")

    #Exibe a data formatada para o padrão brasileiro ex (25/12/2024)
    data_br = data.strftime("%d/%m/%Y")
    print("Data:", data_br)

    #Exibe os dias da semana formatados para o padrão brasileiro ex (Quarta-feira)
    dia_semana = data.isoweekday() % 7 + 1
    print("Dia:", DIAS_SEMANA[dia_semana])

    #Exibe a temperatura média e a condição do dia da previsão
    print("Temperatura média:", dia["day"]["avgtemp_c"], "°C")
    print("Previsão:", dia["day"]["condition"]["text"])
    chance_chuva = dia["day"].get("daily_chance_of_rain", 0)
    print(f"Probabilidade de chuva: {chance_chuva}% - {mensagem_probabilidade_chuva(chance_chuva)}")

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
            diaescolhido = int(input(
                "Digite o número do dia da semana (1 - Domingo, 2 - Segunda, "
                "3 - Terça, 4 - Quarta, 5 - Quinta, 6 - Sexta, 7 - Sábado): "
            ))
            
            while diaescolhido not in DIAS_SEMANA:
                diaescolhido = int(input("Escolha um número entre 1 e 7: "))
            previsao_futuro(cidade,diaescolhido)

        case "3":
            print("ATE LOGO!")
            sair = "s"
            
        
    
   