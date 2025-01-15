import pandas as pd
import json
import requests
import ssl
import os
import sys
import time

import requests
from urllib3 import Retry
from requests.adapters import HTTPAdapter
from urllib3.util.ssl_ import create_urllib3_context



#API_URL = "https://ourobranco.ufsj.edu.br:4200/csn-api/api/mapeamento/peer"
API_URL = "http://127.0.0.1:4011/mapeamento/peer"

IS_IN_ARRAY_FORMAT = False

HAS_HEADER = True

SAVE_TO_LOG = True

READ_ALL_FILES_FROM_DIR = True

EXPECTED_STATUS_CODE = ["200", "201"]

USE_CUSTOM_HEADERS = True

#CSV_COLUMN_NAMES = [
#    "ip",
#    "data",
#    "hora",
#    "radio",
#    "lat",
#    "lon",
#    "alt",
#    "temperatura",
#    "custo",
#    "rssi",
#    "ipv4Address",
#]
CSV_COLUMN_NAMES = [
    "data",
    "hora", 
    "lat", 
    "lon", 
    "alt", 
    "radio", 
    "custo", 
    "rssi", 
    "ipv4Address", 
    "ip", 
    "macsource", 
    "macdestination",
    "action", 
    "enabled", 
    "rate", 
    "signal_ok", 
    "age", 
    "stats", 
    "encapId", 
    "txpower",  
    "version",
    "linkLocalAddress"
]

def request(url,dados):
    context = ssl.create_default_context()
    context.options |= ssl.OP_NO_SSLv3  # Disable SSLv3
    context.options |= ssl.OP_NO_SSLv2  # Disable SSLv2
    response = requests.post(
        url,
        headers={'Content-Type': 'application/json'},
        json=dados,
#        data=json.dumps({'key': 'value'}),
        verify=False,  # Disable certificate verification (adjust as needed)
        context=context
    )

    
    context = create_urllib3_context()
    context.options |= 0x4  # Enables TLSv1.0/1.1

    session = requests.Session()
    adapter = HTTPAdapter(max_retries=Retry(3), pool_connections=1, pool_maxsize=1)
    session.mount("https://", adapter)
    url='http://127.0.0.1:4011/mapeamento/peer'
    response = session.post(url, json=dados, verify=False)
    return response


def save_to_log(log):
    if SAVE_TO_LOG:
        with open("log.txt", "a") as f:
            f.write(log)


def send_data_to_api(data):
    json_data = json.dumps(data, ensure_ascii=False)
    return requests.post(API_URL, json=json_data)


def read_csv_file(file_name, column_names=None):
    if column_names and USE_CUSTOM_HEADERS:
        df = pd.read_csv(file_name, names=column_names, skiprows=int(HAS_HEADER), index_col=False)
    else:
        df = pd.read_csv(file_name)
    df_dict = df.to_dict(orient="records")
    return df_dict


def send_object_by_object_to_api(data):
    for row in data:
        try:
            save_to_log(f"\nEnviando: {row}\n")
            if(row["radio"]=="ME4"): # API somente recebe valores inteiros por enquanto. Remover após corrigir
                row[ "radio" ] = 4  
            elif(row["radio"]=="LX5"):
                row[ "radio" ] = 5
            else:
                row[ "radio" ] = 50
            print(f"Enviando: {row}\n")
#            r = request(API_URL, row)
            #response = requests.post(API_URL, json=data, verify=False)

            session = requests.Session()
            r = session.request("POST",API_URL, json=row,verify=False)
            if str(r.status_code) not in EXPECTED_STATUS_CODE:
                raise Exception(f"Status code inválido: {r.status_code}\n {r.text}\n")
            save_to_log(f"Status code: {r.status_code}\n")
        except Exception as e:
            print(e)
            save_to_log(f"error: {e}\n")


def main(path,file_name):
    try:
        path_and_name = path + file_name
        if os.path.exists(path_and_name) is False:
            raise Exception(f"Arquivo {path_and_name} não encontrado")
        df_dict = read_csv_file(path_and_name, CSV_COLUMN_NAMES)
        if IS_IN_ARRAY_FORMAT:
            send_data_to_api(df_dict)
            return
        send_object_by_object_to_api(df_dict)
    except Exception as e:
        print(e)
        save_to_log(f"error: {e}\n")


def read_all_file_names_from_dir():
    file_names = os.listdir()
    file_names_filtered = [name for name in file_names if name.endswith(".csv")]
    return file_names_filtered


def read_file_names_from_args():
    file_names = [name for name in sys.argv[1:]]
    return file_names

def read_all_file_names_from_dir(path):
    file_names = os.listdir(path)
    file_names_filtered = [name for name in file_names if name.endswith(".csv")]
    return file_names_filtered

 


def confirm_and_load(path,file_names):
    print(f"\nArquivos a serem enviados: {file_names}\n")
    print(f"Envio para API: {API_URL}\n")
    print(f"Envio em formato de array único: {IS_IN_ARRAY_FORMAT}\n")
    continue_flag = input("Continuar (s/n)? ")
    if continue_flag.lower() != "s":
        return 0
    for file_name in file_names:
        main(path,file_name)
    return 1

def loadToApi(path):
    file_names =  read_all_file_names_from_dir(path)
    confirm_and_load(path,file_names)

if __name__ == "__main__":
    path_out ='../dados2/2023-11-22/' 
#    path_out ='../tests/' 
    loadToApi(path_out)


    print(requests.__version__)
    file_names = read_file_names_from_args()
    if READ_ALL_FILES_FROM_DIR and len(file_names) == 0:
        file_names = read_all_file_names_from_dir('./')
    result = confirm_and_load('./',file_names)
    if (result):
        print(f"Tentativa de carga de dados para a API realizada, verificar logs")
    else:
        print(f"Tentativa de carga de dados abortada")

