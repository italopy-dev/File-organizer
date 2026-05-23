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

for a in arquivos:
    extensao = os.path.splitext(a)[1]

    if extensao in documentos:
        if not os.path.exists(f"{pasta}/documentos"):
            os.mkdir(f"{pasta}/documentos")
            shutil.move(f"{pasta}/{a}", f"{pasta}/documentos")

        else:
            shutil.move(f"{pasta}/{a}", f"{pasta}/documentos")

    elif extensao in compactados:
        if not os.path.exists(f"{pasta}/compactados"):
            os.mkdir(f"{pasta}/compactados")
            shutil.move(f"{pasta}/{a}", f"{pasta}/compactados")

        else:
            shutil.move(f"{pasta}/{a}", f"{pasta}/compactados")

    elif extensao in audios:
        if not os.path.exists(f"{pasta}/audios"):
            os.mkdir(f"{pasta}/audios")
            shutil.move(f"{pasta}/{a}", f"{pasta}/audios")

        else:
            shutil.move(f"{pasta}/{a}", f"{pasta}/audios")

    elif extensao in planilhas:
        if not os.path.exists(f"{pasta}/planilhas"):
            os.mkdir(f"{pasta}/planilhas")
            shutil.move(f"{pasta}/{a}", f"{pasta}/planilhas")

        else:
            shutil.move(f"{pasta}/{a}", f"{pasta}/planilhas")

    elif extensao in imagens:
        if not os.path.exists(f"{pasta}/imagens"):
            os.mkdir(f"{pasta}/imagens")
            shutil.move(f"{pasta}/{a}", f"{pasta}/imagens")

        else:
            shutil.move(f"{pasta}/{a}", f"{pasta}/imagens")

    elif extensao in videos:
        if not os.path.exists(f"{pasta}/videos"):
            os.mkdir(f"{pasta}/videos")
            shutil.move(f"{pasta}/{a}", f"{pasta}/videos")

        else:
            shutil.move(f"{pasta}/{a}", f"{pasta}/videos")

    elif extensao in apresentacoes:
        if not os.path.exists(f"{pasta}/apresentacoes"):
            os.mkdir(f"{pasta}/apresentacoes")
            shutil.move(f"{pasta}/{a}", f"{pasta}/apresentacoes")

        else:
            shutil.move(f"{pasta}/{a}", f"{pasta}/apresentacoes")

    elif extensao in executaveis:
        if not os.path.exists(f"{pasta}/executaveis"):
            os.mkdir(f"{pasta}/executaveis")
            shutil.move(f"{pasta}/{a}", f"{pasta}/executaveis")

    elif extensao in ebooks:
        if not os.path.exists(f"{pasta}/ebooks"):
            os.mkdir(f"{pasta}/ebooks")
            shutil.move(f"{pasta}/{a}", f"{pasta}/ebooks")

        else:
            shutil.move(f"{pasta}/{a}", f"{pasta}/ebooks")

    elif extensao in jogos:
        if not os.path.exists(f"{pasta}/jogos"):
            os.mkdir(f"{pasta}/jogos")
            shutil.move(f"{pasta}/{a}", f"{pasta}/jogos")

        else:
            shutil.move(f"{pasta}/{a}", f"{pasta}/jogos")

    elif extensao in design:
        if not os.path.exists(f"{pasta}/design"):
            os.mkdir(f"{pasta}/design")
            shutil.move(f"{pasta}/{a}", f"{pasta}/design")

        else:
            shutil.move(f"{pasta}/{a}", f"{pasta}/design")

    elif extensao in codigos:
        if not os.path.exists(f"{pasta}/codigos"):
            os.mkdir(f"{pasta}/codigos")
            shutil.move(f"{pasta}/{a}", f"{pasta}/codigos")

        else:
            shutil.move(f"{pasta}/{a}", f"{pasta}/codigos")


    




            

    