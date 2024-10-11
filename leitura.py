import pyrebase  # Para conectar ao Firebase
import time  # Para pausas entre as leituras

# Configurações do Firebase
firebaseConfig = {
    "apiKey": "AIzaSyBAf9c-9w4mO51tpNpv0LU8VNmgFPw6rLc",
    "authDomain": "dados-sinais-vitais.firebaseapp.com",
    "databaseURL": "https://dados-sinais-vitais-default-rtdb.firebaseio.com",
    "projectId": "dados-sinais-vitais",
    "storageBucket": "dados-sinais-vitais.appspot.com",
    "messagingSenderId": "806366736652",
    "appId": "1:806366736652:web:7c834a58f31457eeac9929"
}

# Inicializa o Firebase
firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()

# Função para ler dados do arquivo .txt
def ler_dados_arquivo(arquivo):
    with open(arquivo, 'r') as file:
        dados = file.readlines()
        if len(dados) >= 3:  # Verifica se há pelo menos 3 linhas no arquivo
            temperatura = dados[0].strip()  # Primeira linha: temperatura
            spo2 = dados[1].strip()  # Segunda linha: SpO2
            bpm = dados[2].strip()  # Terceira linha: BPM
            return temperatura, spo2, bpm
        else:
            return None, None, None

# Loop para ler dados do arquivo e enviar para o Firebase
while True:
    temperatura, spo2, bpm = ler_dados_arquivo('dados.txt')  # Substitua 'dados.txt' pelo nome do seu arquivo

    if temperatura and spo2 and bpm:
        # Exibe no terminal para depuração
        print(f'Temperatura: {temperatura}, SpO2: {spo2}, BPM: {bpm}')
        
        # Envia os dados para o Firebase
        data = {
            "temperatura": temperatura,
            "spo2": spo2,
            "bpm": bpm
        }
        # Envia os dados para o Firebase em um caminho específico
        db.child("dados/sinais_vitais").push(data)  # Envia os dados para o caminho 'dados/sinais_vitais' no Firebase
                
    else:
        print("Arquivo não contém dados suficientes ou está vazio.")

    time.sleep(5)  # Intervalo entre leituras
