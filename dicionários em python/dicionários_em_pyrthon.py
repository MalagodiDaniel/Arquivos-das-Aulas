contatos = { 
     "daniel@gmail.com" : {"nome": "Daniel", "telefone": "993445868"},
    "talita@gmail.com": {"nome": "Talita", "telefone": "88559669"},
}

contatos ["daniel@gmail.com"] ["telefone"]

print(contatos)



 
copia = contatos.copy()

copia["daniel@gmail.com"] = {"nome": "Dani"}
 
##print(copia)## 

resultado = "talita@gmail.com" in contatos
#print(resultado)

resultados = "idade" in contatos ["daniel@gmail.com"]
#print(resultados)

del contatos ["daniel@gmail.com"]["telefone"]
print(contatos)