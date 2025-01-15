import csv
def getLines(path,ip):
    file = path+ip+'.log'
    f = open(file, "r")
    lines = f.read().split("\n") # "\r\n" if needed
    return lines

path_gps = '../logs/2023-11-21/GPS/'
ipGps = '172.23.72.84' 
lines = getLines(path_gps,ipGps)
for line in lines:
    if (line != "" and 'Erro' not in line 
        and 'Not Found' not in line 
        and '0.000000000' not in line) : # add other needed checks to skip titles
            cols = line.split(";")
            num_ip = cols[0]
            try: #check if is a valid latitude
                data = cols[1][0:10]
                hora = cols[1][11:16]
                lat = float(cols[2])
                lon = float(cols[3])
                #print(str(data)+" "+str(hora)+" "+str(lat)+" "+str(lon))
            except:
                print("Erro ao processar coordendada:\n"+line)
                continue
"""        
path_gps = '../logs/2023-11-21/'
ipGps = '172.23.67.111' 
#ipGps = '172.23.67.215' 
lines = getLines(path_gps,ipGps)
for line in lines:
    if("Logging" not in line ):
            cols = line.split(';')
            data = cols[0][0:10]
            hora = cols[0][11:16]
            temperatura=cols[2]
            modelo=cols[3]
            version=cols[8]
            ip = cols[13]
            if('W' in line and 'S' in line): # Rádio da Rajant tem seu próprio GPS
                ipPar = cols[34] 
                rssi = cols[40]  
                custo = cols[43] 
                lat = cols[29]   
                lon = cols[30]   
            else:  # Coordena deve ser pega via GPS da Caterpilar ou fica zerada
                ipPar = cols[31] 
                rssi = cols[37]  
                custo = cols[40] 
                lat =  0.0   
                lon =  0.0   
          #2023-11-21 09:16:33.714 [Thread-111] INFO  c.r.b.p.PeersRssiAppPeriodico$GetRSSIPeers - ;
          # ;
          #  2; 3 ; 4      ; 5      ; 6  ; 7  ; 8     ; 9    ; 10  ; 11  ;12; 13 ; 14   ; 15        ; 16   
          # 35;LX5;73725.06;60943.23;true;true;11.24.2;170352;false;false;;172.23.67.111;172.23.66.1;0.0.0.0;
          #  17                    ;18   ;19   ; 20  ; 21   ; 22  ; 23 ; 24
          # fe80::d0:12ff:fe46:f6d6;87280;false;false;gw2385;false;1259;00:d0:12:46:f6:d6 00:d0:12:46:f6:d7 04:f0:21:8e:95:7b 84:8d:84:fe:45:2e 04:f0:21:8e:95:71 84:8d:84:fe:45:2d;30:30:3A:64:30:3A:31:32:3A:34:36:3A:66:36:3A:64:36:20:30:30:3A:64:30:3A:31:32:3A:34:36:3A:66:36:3A:64:37:20:30:34:3A:66:30:3A:32:31:3A:38:65:3A:39:35:3A:37:62:20:38:34:3A:38:64:3A:38:34:3A:66:65:3A:34:35:3A:32:65:20:30:34:3A:66:30:3A:32:31:3A:38:65:3A:39:35:3A:37:31:20:38:34:3A:38:64:3A:38:34:3A:66:65:3A:34:35:3A:32:64;
          #  25       ; 26 ;27;28;29;30;31;  30   ; 31          ;32;33 ;34  ;35   ;36;37 ;38;39;40   ;41           ;42;43
          # 1700568950;tap0;  ;  ;172.23.67.111;wlan0;172.23.67.132;  ;ADD;true;54712;17;-77;0 ;  ;77449;172.23.67.132;14;fe80::868d:84ff:fefe:d120%wlan0wds


          # Linha com GPS da própria Rajant
          #0                                                                                       ;1; 2;  3;        4;        5;
          #2023-11-21 09:17:22.707 [Thread-215] INFO  c.r.b.p.PeersRssiAppPeriodico$GetRSSIPeers - ; ;39;LX5;224205.05;178199.97;i
          #    6;   7;      8;     9;   10;   11;12;           13;         14;     15;                     16;   17;   18;   19;    20;
          # true;true;11.24.2;169176;false;false;  ;172.23.67.215;172.23.66.1;0.0.0.0;fe80::d0:12ff:feaf:f6f5;87278;false;false;gw2385;
          #    21; 22;                                                                                                                                                                                                                                                                                                                                                                                                                                                     23;
          # false;646;00:d0:12:af:f6:f5 00:d0:12:af:f6:f6 04:f0:21:8e:99:7c 84:8d:84:fe:d9:29 04:f0:21:8e:99:7d 84:8d:84:fe:d9:2b;30:30:3A:64:30:3A:31:32:3A:61:66:3A:66:36:3A:66:35:20:30:30:3A:64:30:3A:31:32:3A:61:66:3A:66:36:3A:66:36:20:30:34:3A:66:30:3A:32:31:3A:38:65:3A:39:39:3A:37:63:20:38:34:3A:38:64:3A:38:34:3A:66:65:3A:64:39:3A:32:39:20:30:34:3A:66:30:3A:32:31:3A:38:65:3A:39:39:3A:37:64:20:38:34:3A:38:64:3A:38:34:3A:66:65:3A:64:39:3A:32:62;1700568953;i
          #   24;25;26;        27;         28;                  29; 
          # tap0;  ;  ;2028.4229S;04355.5155W;1249.7;172.23.67.215;wlan3;172.23.67.135;;ADD;true;10763;20;-88;0;;87576;172.23.67.135;23;fe80::6f0:21ff:fe8e:955c%wlan3wds
#    print (cols)
"""