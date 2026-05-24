import os
import shutil

pasta = input("Digite a pasta que quer organizar(o caminho completo)")
arquivos = os.listdir(pasta)

documentos = [".txt", ".pdf", ".doc", ".docx", ".rtf"]
compactados = [".zip", ".rar", ".7z", ".tar"]
audios = [".mp3", ".wav", ".ogg", ".flac", ".m4a"]
planilhas = [".xls", ".xlsx", ".csv"]
imagens = [".png", ".jpg", ".jpeg", ".gif", ".webp", ".bmp", ".svg"]
videos = [".mp4", ".mkv", ".avi", ".mov", ".webm"]
apresentacoes = [".ppt", ".pptx", ".pps", ".ppsx", ".odp"]
executaveis = [".exe", ".msi", ".bat"]
ebooks = [".epub", ".mobi", ".azw3"]
jogos = [".iso", ".rom", ".sav"]
design = [".psd", ".ai"]
codigos = [".py", ".java", ".html", ".css", ".js", ".cpp"]

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

            


    




            

    