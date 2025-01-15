import Data
from main import line


class Coordenada: 
    def __init__(self,lat=0,lon=0,alt=0):
        self.lat = lat
        self.lon = lon
        self.alt = alt

class Horario:
    def __init__(self,data,hora):
        self.data = data
        self.hora = hora        

class Par:
    def __init__(self, origem, destino, rssi, custo, horario:Horario):
        self.origem = origem
        self.destino = destino
        self.rssi = rssi
        self.custo = custo
        self.horario = horario
    #def ad():
    #   a:Horario
    #   for a in range(0,9):
    #       a.

class LogRadio:
    def __init__(self,line):
        self.horario = Horario()
        self.equipamento = Equipamento()
        self.pares = list()
        self.coordenada = Coordenada()
        self.bestRssi = 0
        self.bestCusto = 0
    def __init__(self,data,hora, ip):
        self.horario = Horario(data,hora)
        self.equipamento = Equipamento.getEquipamento(ip)

    def addPar(self,par):
        self.pares.append(par)
        if(par.custo < self.bestCusto):
            self.bestCusto = par.custo
        if(par.rssi < self.bestRssi):
            self.bestRssi = par.rssi
    def getHorario(self,line):
        return self.horario
        
equipamentos = dict()
menor = sorted()[0]

class Equipamento:
    def __init__(self,ip):
        self.tipo = ''
        self.ipRadio = ip
        self.ipGPS = ''
        self.nome = ''
        self.logRadio = list()
        equipamentos[ip]=self
    def addRssi (self, m,rssi):
        self.rssiDict[m]= rssi
    def addCusto (self, m,custo):
        self.custoDict[m]= custo 
    def getIpRadio(self):
        return self.ipRadio 
    def getEquipamento(ip):
        try:
            return equipamentos[ip]
        except:
            novoEquipamento = Equipamento(ip)
            return novoEquipamento
        
        

class MapaCalorPonto:
    def __init__(self,coordenada, melhorRssi, melhorCusto) :
       self.coordenada = coordenada 
       self.rssi  = melhorRssi
       self.custo = melhorCusto
       
class MapaCalor:
    def __init__(self, horario) :
        self.horario = Horario()
        self.mapaCalorPontoLista = list() # lista de equipamentos vistos nesse horário
    def addPonto(self, pontoMapaCalor):
        self.mapaCalorPontoLista.append(pontoMapaCalor)
    def print(self):
        print(self.mapaCalorPontoLista)

nomeMap = dict()    # Mapeamento entre nome e ip
ipMap   = dict()    # Mapeamento entre ip do rádio e ip do GPS


#ipMap["172.23.67.125"]="172.23.72.234"
#ipMap["172.23.67.124"]="172.23.72.224"
#ipMap["172.23.67.120"]="172.23.72.184"
#ipMap["172.23.67.117"]="172.23.72.154"
#ipMap["172.23.67.111"]="172.23.72.84"
#ipMap["172.23.67.116"]="172.23.72.144"
#ipMap["172.23.67.108"]="172.23.72.64"
#ipMap["172.23.67.113"]="172.23.72.114" # Não gerou o arquivo 113 no dia 20/11
#ipMap["172.23.67.115"]="172.23.72.134"
#ipMap["172.23.67.142"]="172.23.73.134"
ipMap["172.23.67.104"]="172.23.75.129"  #CM-7901   Not Found at 20/11
ipMap["172.23.67.105"]="172.23.72.24"   #CM-7902
ipMap["172.23.67.106"]="172.23.72.44"   #CM-7904
ipMap["172.23.67.107"]="172.23.74.244"  #CM-7905
ipMap["172.23.67.108"]="172.23.72.64"   #CM-7906
ipMap["172.23.67.110"]="172.23.72.74"   #CM-7907   Not Found at 20/11
ipMap["172.23.67.111"]="172.23.72.84"   #CM-7908
ipMap["172.23.67.112"]="172.23.72.104"  #CM-7910
#ipMap["172.23.67.113"]="172.23.72.114"  #CM-7911   Not Found at 20/11
ipMap["172.23.67.114"]="172.23.72.124"  #CM-7912
ipMap["172.23.67.115"]="172.23.72.134"  #CM-7913
ipMap["172.23.67.116"]="172.23.72.144"  #CM-7914
ipMap["172.23.67.117"]="172.23.72.154"  #CM-7915
ipMap["172.23.67.118"]="172.23.72.164"  #CM-7916
ipMap["172.23.67.119"]="172.23.72.174"  #CM-7917
ipMap["172.23.67.120"]="172.23.72.184"  #CM-7918
ipMap["172.23.67.121"]="172.23.72.194"  #CM-7919   Not Found at 20/11
ipMap["172.23.67.122"]="172.23.72.204"  #CM-7920
ipMap["172.23.67.123"]="172.23.72.214"  #CM-7921
ipMap["172.23.67.124"]="172.23.72.224"  #CM-7922
ipMap["172.23.67.125"]="172.23.72.234"  #CM-7923
ipMap["172.23.67.126"]="172.23.72.244"  #CM-7924   Not Found at 20/11
ipMap["172.23.67.127"]="172.23.73.14"   #CM-7925
ipMap["172.23.67.128"]="172.23.73.24"   #CM-7926
ipMap["172.23.67.130"]="172.23.73.34"   #CM-7927
ipMap["172.23.67.131"]="172.23.73.44"   #CM-7928
ipMap["172.23.67.132"]="172.23.73.54"   #CM-7929   Not Found at 20/11
ipMap["172.23.67.133"]="172.23.73.64"   #CM-7930   Not Found at 20/11
ipMap["172.23.67.135"]="172.23.73.74"   #CM-7931
ipMap["172.23.67.136"]="172.23.73.84"   #CM-7932
ipMap["172.23.67.137"]="172.23.73.94"   #CM-7933   Not Found at 20/11
ipMap["172.23.67.138"]="172.23.73.104"  #CM-7934
ipMap["172.23.67.139"]="172.23.73.114"  #CM-7935
ipMap["172.23.67.140"]="172.23.73.124"  #CM-7936
ipMap["172.23.67.142"]="172.23.73.134"  #CM-7937
ipMap["172.23.67.143"]="172.23.73.144"  #CM-7938
ipMap["172.23.67.145"]="172.23.73.154"  #CM-7939
ipMap["172.23.67.146"]="172.23.73.164"  #CM-7940
ipMap["172.23.67.147"]="172.23.73.174"  #CM-7941
ipMap["172.23.67.148"]="172.23.73.184"  #CM-7942
ipMap["172.23.67.149"]="172.23.73.194"  #CM-7943
ipMap["172.23.67.150"]="172.23.73.204"  #CM-7944   Not Found at 20/11
ipMap["172.23.67.151"]="172.23.73.214"  #CM-7945   Not Found at 20/11
ipMap["172.23.67.152"]="172.23.73.224"  #CM-7946
ipMap["172.23.67.153"]="172.23.73.234"  #CM-7947   Not Found at 20/11
ipMap["172.23.67.154"]="172.23.73.244"  #CM-7948   Not Found at 20/11
ipMap["172.23.67.155"]="172.23.74.14"   #CM-7949
ipMap["172.23.67.156"]="172.23.74.24"   #CM-7950
ipMap["172.23.67.157"]="172.23.74.34"   #CM-7951
ipMap["172.23.67.158"]="172.23.74.44"   #CM-7952
ipMap["172.23.67.159"]="172.23.74.54"   #CM-7953
ipMap["172.23.67.160"]="172.23.74.64"   #CM-7954
ipMap["172.23.67.161"]="172.23.74.74"   #CM-7955
ipMap["172.23.67.162"]="172.23.74.84"   #CM-, g
ipMap["172.23.67.163"]="172.23.74.94"   #CM-7957
ipMap["172.23.67.164"]="172.23.72.14"   #CM-7958   Not Found at 20/11
ipMap["172.23.67.165"]="172.23.72.34"   #CM-7959
ipMap["172.23.67.166"]="172.23.72.54"   #CM-7960
ipMap["172.23.67.191"]="172.23.72.94"   #CM-7961
ipMap["172.23.67.192"]="172.23.74.219"  #CM-7962   Not Found at 20/11
ipMap["172.23.67.203"]="172.23.74.204"  #CM-7963
ipMap["172.23.67.204"]="172.23.74.214"  #CM-7964
ipMap["172.23.67.205"]="172.23.74.224"  #CM-7965
ipMap["172.23.67.206"]="172.23.74.234"  #CM-7966
#ipMap["172.23.66.9"]="UMR 01 - 22H (Link)" # Não tem coordenadas
#ipMap["172.23.66.13"]="UFR 02 - Britador" # Não tem coordenadas
#ipMap["172.23.66.46"]="UFR 04 - Vila 2" # Não tem coordenadas
#ipMap["172.23.66.37"]="UMR 12 - 13T Link" # Não tem coordenadas
ipMap["172.23.66.33"]= "172.23.66.33"

nomeMap["172.23.67.71"]="TP-8502" 
nomeMap["172.23.67.84"]="MN-2408" 
nomeMap["172.23.67.85"]="Desconhecido" 
nomeMap["172.23.67.90"]="Desconhecido" 
nomeMap["172.23.67.92"]="PE-6211" 
nomeMap["172.23.67.93"]="Desconhecido" 
nomeMap["172.23.67.94"]="Desconhecido" 
nomeMap["172.23.67.102"]="CM-7902" 
nomeMap["172.23.67.129"]="Desconhecido" 
nomeMap["172.23.67.134"]="Desconhecido" 
nomeMap["172.23.67.141"]="Desconhecido" 
nomeMap["172.23.67.144"]="Desconhecido" 
nomeMap["172.23.67.193"]="PM-9903 Pires" 
nomeMap["172.23.67.194"]="Desconhecido" 
nomeMap["172.23.67.195"]="PM-9905 Pires" 
nomeMap["172.23.67.207"]="ES-6002" 
nomeMap["172.23.67.201"]="ES-5501" 
nomeMap["172.23.67.202"]="ES-5502" 
nomeMap["172.23.67.208"]="ES-6003" 
nomeMap["172.23.67.209"]="ES-6004" 
nomeMap["172.23.67.210"]="PM-9905" 
nomeMap["172.23.67.211"]="PM-9906" 
nomeMap["172.23.67.213"]="PM-9908" 
nomeMap["172.23.67.214"]="PM-9909" 
nomeMap["172.23.67.215"]="PM-9910" 
nomeMap["172.23.67.226"]="TE-1105" 
nomeMap["172.23.67.229"]="TE-1108" 
nomeMap["172.23.67.230"]="Desconhecido" 
nomeMap["172.23.67.231"]="TE-1110" 
nomeMap["172.23.67.235"]="TE-1114" 
nomeMap["172.23.67.237"]="TE-1116" 
nomeMap["172.23.67.238"]="TE-1117" 
nomeMap["172.23.67.239"]="TE-1118" 
nomeMap["172.23.67.241"]="Desconhecido" 
nomeMap["172.23.67.104"]="CM-7901"  # CM-7901  Not Found at 20/11
nomeMap["172.23.67.105"]="CM-7902"  # CM-7902
nomeMap["172.23.67.106"]="CM-7904"  # CM-7904
nomeMap["172.23.67.107"]="CM-7905"  # CM-7905
nomeMap["172.23.67.108"]="CM-7906"  # CM-7906
nomeMap["172.23.67.110"]="CM-7907"  # CM-7907  Not Found at 20/11
nomeMap["172.23.67.111"]="CM-7908"  # CM-7908
nomeMap["172.23.67.112"]="CM-7910"  # CM-7910
nomeMap["172.23.67.113"]="CM-7911"  # CM-7911  Not Found at 20/11
nomeMap["172.23.67.114"]="CM-7912"  # CM-7912
nomeMap["172.23.67.115"]="CM-7913"  # CM-7913
nomeMap["172.23.67.116"]="CM-7914"  # CM-7914
nomeMap["172.23.67.117"]="CM-7915"  # CM-7915
nomeMap["172.23.67.118"]="CM-7916"  # CM-7916
nomeMap["172.23.67.119"]="CM-7917"  # CM-7917
nomeMap["172.23.67.120"]="CM-7918"  # CM-7918
nomeMap["172.23.67.121"]="CM-7919"  # CM-7919  Not Found at 20/11
nomeMap["172.23.67.122"]="CM-7920"  # CM-7920
nomeMap["172.23.67.123"]="CM-7921"  # CM-7921
nomeMap["172.23.67.124"]="CM-7922"  # CM-7922
nomeMap["172.23.67.125"]="CM-7923"  # CM-7923
nomeMap["172.23.67.126"]="CM-7924"  # CM-7924  Not Found at 20/11
nomeMap["172.23.67.127"]="CM-7925"  # CM-7925
nomeMap["172.23.67.128"]="CM-7926"  # CM-7926
nomeMap["172.23.67.130"]="CM-7927"  # CM-7927
nomeMap["172.23.67.131"]="CM-7928"  # CM-7928
nomeMap["172.23.67.132"]="CM-7929"  # CM-7929  Not Found at 20/11
nomeMap["172.23.67.133"]="CM-7930"  # CM-7930  Not Found at 20/11
nomeMap["172.23.67.135"]="CM-7931"  # CM-7931
nomeMap["172.23.67.136"]="CM-7932"  # CM-7932
nomeMap["172.23.67.137"]="CM-7933"  # CM-7933  Not Found at 20/11
nomeMap["172.23.67.138"]="CM-7934"  # CM-7934
nomeMap["172.23.67.139"]="CM-7935"  # CM-7935
nomeMap["172.23.67.140"]="CM-7936"  # CM-7936
nomeMap["172.23.67.142"]="CM-7937"  # CM-7937
nomeMap["172.23.67.143"]="CM-7938"  # CM-7938
nomeMap["172.23.67.145"]="CM-7939"  # CM-7939
nomeMap["172.23.67.146"]="CM-7940"  # CM-7940
nomeMap["172.23.67.147"]="CM-7941"  # CM-7941
nomeMap["172.23.67.148"]="CM-7942"  # CM-7942
nomeMap["172.23.67.149"]="CM-7943"  # CM-7943
nomeMap["172.23.67.150"]="CM-7944"  # CM-7944  Not Found at 20/11
nomeMap["172.23.67.151"]="CM-7945"  # CM-7945  Not Found at 20/11
nomeMap["172.23.67.152"]="CM-7946"  # CM-7946
nomeMap["172.23.67.153"]="CM-7947"  # CM-7947  Not Found at 20/11
nomeMap["172.23.67.154"]="CM-7948"  # CM-7948  Not Found at 20/11
nomeMap["172.23.67.155"]="CM-7949"  # CM-7949
nomeMap["172.23.67.156"]="CM-7950"  # CM-7950
nomeMap["172.23.67.157"]="CM-7951"  # CM-7951
nomeMap["172.23.67.158"]="CM-7952"  # CM-7952
nomeMap["172.23.67.159"]="CM-7953"  # CM-7953
nomeMap["172.23.67.160"]="CM-7954"  # CM-7954
nomeMap["172.23.67.161"]="CM-7955"  # CM-7955
nomeMap["172.23.67.162"]="CM-7956"  # CM-7956
nomeMap["172.23.67.163"]="CM-7957"  # CM-7957
nomeMap["172.23.67.164"]="CM-7958"  # CM-7958  Not Found at 20/11
nomeMap["172.23.67.165"]="CM-7959"  # CM-7959
nomeMap["172.23.67.166"]="CM-7960"  # CM-7960
nomeMap["172.23.67.191"]="CM-7961"  # CM-7961
nomeMap["172.23.67.192"]="CM-7962"  # CM-7962  Not Found at 20/11
nomeMap["172.23.67.203"]="CM-7963"  # CM-7963
nomeMap["172.23.67.204"]="CM-7964"  # CM-7964
nomeMap["172.23.67.205"]="CM-7965"  # CM-7965  Not Found at 20/11
nomeMap["172.23.67.206"]="CM-7966"  # CM-7966
nomeMap["172.23.66.7"] = "UFR 09 - Pires Oficina"
nomeMap["172.23.66.8"] = "UMR 40 - PCOL"
nomeMap["172.23.66.9"] = "UMR 01 - 22H ( Link )"
nomeMap["172.23.66.10"]= "UMR 27 - PCOL Banco acima"
nomeMap["172.23.66.11"]= "UMR 30 -  Salum"
nomeMap["172.23.66.12"]= "UMR 31- B2 Acima rampa do ceguinho"
nomeMap["172.23.66.13"]= "UFR 02 - Britador"
nomeMap["172.23.66.14"]= "UMR 19 - ESC MINA"
nomeMap["172.23.66.15"]= "UMR 17 - 7K Prox. entrada da mina"
nomeMap["172.23.66.16"]= "UFR 06 - 13N"
nomeMap["172.23.66.17"]= "UMR 33 - Esmeril D entrada"
nomeMap["172.23.66.18"]= "UMR 16F Prox. A ES-6003"
nomeMap["172.23.66.19"]= "UMR 41 - 17 L link"
nomeMap["172.23.66.20"]= "UMR 36 - 20H Baixo"
nomeMap["172.23.66.21"]= "UMR 37 - 18N PROX ES5502"
nomeMap["172.23.66.22"]= "UMR 28 - 18D PRX 6003"
nomeMap["172.23.66.23"]= "UMR 20 - PCOL  LINK"
nomeMap["172.23.66.24"]= "UMR 35 - Vila Sub Estacão "
nomeMap["172.23.66.27"]= "UFR 07 - Sump 1080"
nomeMap["172.23.66.28"]= "UFR 08 - Pires TFI"
nomeMap["172.23.66.30"]= "UMR 39 - 18I / PCN 02"
nomeMap["172.23.66.31"]= "UMR 11 - Estrada abaixo 1080 "
nomeMap["172.23.66.32"]= "UMR 23 - Trevo 18i | Bandeira"
nomeMap["172.23.66.33"]= "UMR 32 - 8F Antigo Corpo Oeste"
nomeMap["172.23.66.37"]= "UMR 12 - 13T  LINK"
nomeMap["172.23.66.41"]= "UMR 14 - 4H Estrada sentido Batateiro"
nomeMap["172.23.66.45"]= "UMR 22 - 20H LINK Alto"
nomeMap["172.23.66.46"]= "UFR 04 - Vila 2"
nomeMap["172.23.66.47"]= "UMR 03 - Trailer telescopio  PCN"
nomeMap["172.23.66.49"]= "UMR 09 - Engenho Subida"
nomeMap["172.23.66.50"]= "UMR 04 - Trailer Telescopio Mascate"
nomeMap["172.23.66.55"]= "UMR 26- Rampa do Ceguinho"
nomeMap["172.23.66.61"]= "UMR 34 - 4H Estacionamento"
nomeMap["172.23.66.63"]= "UMR 07  -  9F"
nomeMap["172.23.66.64"]= "UMR 08 - 13T Baixo"
nomeMap["172.23.66.65"]= "UMR 24 -15K | Acima Lavador de báscula"
nomeMap["172.23.66.66"]= "UMR 29 - 23K Bandeira"
nomeMap["172.23.66.67"]= "UFR 03 - A38 Oficina LX5"
nomeMap["172.23.66.76"]= "UMR 18 - Patio de Sucata"
nomeMap["172.23.66.83"]= "UMR 10 - 10N"
nomeMap["172.23.66.199"]= "UMR  -  Esmeril Fase 3 Alto"
nomeMap["172.23.66.104"]= "UFR CPD A38"
nomeMap["172.23.66.220"]= "RadioTabletmina"
nomeMap["172.23.66.225"]= "UMR Guarita A40"
nomeMap["172.23.66.226"]= "UMR 13 - 15F Estrada"
nomeMap["172.23.66.228"]= "UMR 25 - Entrada 16D"
nomeMap["172.23.66.239"]= "UMR 38 - 18C Praça da ES-6004"
nomeMap["172.23.66.240"]= "UMR 21 - 19J"
nomeMap["172.23.66.241"]= "UFR 05 Corpo Oeste B2"
nomeMap["172.23.66.242"]= "UMR 16 - Esmeril D"
nomeMap["172.23.66.243"]= "UMR 06 - Substação 13H"
nomeMap["172.23.66.244"]= "UMR 15 - PCN1 TREVO PCOL"
nomeMap["0.0.0.0"]= "Gateway"
