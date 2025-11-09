from typing import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pandas as pd

def wordCloud(df, column):
    """
    Crea una word cloud a partir de una columna de un dataframe
    """
    texto = " ".join(df[column].astype(str))
    # Crear nube de palabras
    nube = WordCloud(width=800, height=400, background_color='white').generate(texto)

    # Mostrarla
    plt.imshow(nube, interpolation='bilinear')
    plt.axis('off')
    plt.show()



df = pd.read_csv("../vgsales%20(1).csv")
wordCloud(df, "Name")

texto = " ".join(df["Name"].astype(str))

palabras = texto.rstrip().split(" ")
ranking = Counter(" ".join(palabras).split()).most_common(20)
#print(ranking)
i=1
for rank in ranking:
    print (f"#{i}  {rank[0]} ---> {rank[1]}\n")
    i=i+1
"""
#1  The ---> 1752

#2  of ---> 1710

#3  the ---> 978

#4  2 ---> 844

#5  no ---> 724

#6  3 ---> 399

#7  World ---> 386

#8  & ---> 353

#9  2: ---> 323

#10  Pro ---> 314

#11  Game ---> 300

#12  Super ---> 289

#13  to ---> 274

#14  and ---> 257

#15  - ---> 248

#16  Star ---> 235

#17  Soccer ---> 221

#18  Dragon ---> 214

#19  II ---> 206

#20  NBA ---> 193


"""
##NOTA: Quita palabras vacías por defecto, por eso no se muestran varias en la Word Cloud
wordCloud(df, "Publisher")

texto = " ".join(df["Publisher"].astype(str))

palabras = texto.rstrip().split(" ")
ranking = Counter(" ".join(palabras).split()).most_common(20)
#print(ranking)
i=1
for rank in ranking:
    print (f"#{i}  {rank[0]} ---> {rank[1]}\n")
    i=i+1

"""
#1  Entertainment ---> 2479

#2  Games ---> 1975

#3  Interactive ---> 1621

#4  Arts ---> 1354

#5  Electronic ---> 1353

#6  Activision ---> 1005

#7  Digital ---> 940

#8  Ubisoft ---> 935

#9  Namco ---> 932

#10  Bandai ---> 932

#11  Konami ---> 832

#12  THQ ---> 715

#13  Sony ---> 710

#14  Nintendo ---> 703

#15  Computer ---> 701

#16  Sega ---> 639

#17  Studios ---> 436

#18  Take-Two ---> 413

#19  Capcom ---> 381

#20  Atari ---> 363
"""
