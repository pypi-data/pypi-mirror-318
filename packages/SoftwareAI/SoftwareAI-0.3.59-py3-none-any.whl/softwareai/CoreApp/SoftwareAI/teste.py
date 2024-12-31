import os
import json
from datetime import datetime

# Definindo o nome da aplicação (substitua por sua variável `nameassistant`)
nameassistant = "MyAssistant"

# Gerando o caminho do arquivo JSON
date = datetime.now().strftime('%Y-%m-%d')
output_path_json = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        f'../Destilation/{nameassistant}/Json/DestilationAgent{date}'
    )
)

# Garantir que o diretório exista
os.makedirs(output_path_json, exist_ok=True)

# Nome completo do arquivo JSON
output_path_json2 = os.path.join(output_path_json, f"DestilationDateTime_{date.replace('-', '_').replace(':', '_')}.json")

# Dados a serem adicionados
input_data = "novo input"
output_data = "novo output"
new_entry = {"input": input_data, "output": output_data}

# Verificando se o arquivo já existe e lendo os dados
if os.path.exists(output_path_json2):
    with open(output_path_json2, 'r', encoding='utf-8') as json_file:
        try:
            datasetjson2 = json.load(json_file)  # Carregar o JSON existente
            if not isinstance(datasetjson2, list):
                datasetjson2 = []  # Se não for uma lista, inicializar como lista
        except json.JSONDecodeError:
            datasetjson2 = []  # Inicializar lista se o arquivo estiver vazio ou corrompido
else:
    datasetjson2 = []  # Inicializar lista se o arquivo não existir

# Adicionar a nova entrada
datasetjson2.append(new_entry)

# Escrever de volta no arquivo
with open(output_path_json2, 'w', encoding='utf-8') as json_file:
    json.dump(datasetjson2, json_file, indent=4, ensure_ascii=False)

print(f"Dados salvos em: {output_path_json2}")
