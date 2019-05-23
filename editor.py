import os
import json

os.system('color 3')
print('====== Jogo da Forca - EDITOR =======')
print('Coded by Vitor Assis & Enzo Benvengo ')
print('=====================================')
print()
with open("BDWords.json",'r') as f:
    words = f.read()
if words != {}:
    words = json.loads(words)
else:
    words = {}

palavra = input('#> Palavra: ')
while palavra != '':
    categoria = input('#> Categoria: ')
    dica = input('#> Dica: ')

    if categoria not in list(words.keys()):
        words[categoria] = []

    words[categoria].append({"palavra":palavra, "dica": dica})

    palavra = input('#> Palavra: ')

with open("BDWords.json",'w') as f:
    f.write(json.dumps(words, indent=4, sort_keys=True))

os.system('git commit -a')
os.system('git push')