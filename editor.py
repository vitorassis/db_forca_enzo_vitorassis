import os
import json

os.system('color 3')
print('====== Jogo da Forca - EDITOR =======')
print('Coded by Vitor Assis & Enzo Benvengo ')
print('=====================================')
print()
words = None
with open("BDWords.json",'r') as f:
    words = f.read()
if words != {}:
    words = json.loads(words)
else:
    words = {}

#for categoria in words:
#    for palavra in words[categoria]:
#        palavra.update(dict({'pontos':100}))
#        print(palavra)

palavra = input('#> Palavra: ')
while palavra != '':
    categoria = input('#> Categoria: ')
    dica = input('#> Dica: ')
    pontos = int(input('#> Pontos: '))

    if categoria not in list(words.keys()):
        words[categoria] = []

    words[categoria].append({"palavra":palavra, "dica": dica, 'pontos': pontos})

    palavra = input('#> Palavra: ')

with open("BDWords.json",'w') as f:
    f.write(json.dumps(words, indent=4, sort_keys=True))

os.system('git commit -a')
os.system('git push')
