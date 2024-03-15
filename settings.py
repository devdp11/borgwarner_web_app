import json

def string_conexao():
#Conexao DB atraves do ficheiro Json   
    fileObject = open("settings/settings.json", "r")
    jsonContent = fileObject.read()
    aList = json.loads(jsonContent)
    #resultado da pesquisa do Json
    connection_string=aList[0]['connection_string_db_gps']
    return connection_string