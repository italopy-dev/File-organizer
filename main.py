import os
import shutil
from settings import documentos, compactados, audios, planilhas, imagens, videos, apresentacoes, executaveis, ebooks, jogos, design, codigos

pasta = input("Digite a pasta que quer organizar(o caminho completo)")
arquivos = os.listdir(pasta)

def mover(nome):
    if not os.path.exists(f"{pasta}/{nome}"):
        os.mkdir(f"{pasta}/{nome}")
        shutil.move(f"{pasta}/{a}", f"{pasta}/{nome}")
    else:
        shutil.move(f"{pasta}/{a}", f"{pasta}/{nome}")

for a in arquivos:
    extensao = os.path.splitext(a)[1]

    if extensao in documentos:
        mover("documentos")

    elif extensao in compactados:
        mover("compactados")

    elif extensao in audios:
        mover("áudios")

    elif extensao in planilhas:
        mover("planilhas")

    elif extensao in imagens:
        mover("imagens")

    elif extensao in videos:
        mover("videos")

    elif extensao in apresentacoes:
        mover("apresentações")

    elif extensao in executaveis:
        mover("executáveis")

    elif extensao in ebooks:
        mover("ebooks")

    elif extensao in jogos:
        mover("jogos")

    elif extensao in design:
        mover("designs")

    elif extensao in codigos:
        mover("códigos")

    
