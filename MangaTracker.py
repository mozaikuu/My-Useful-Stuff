import glob

G_O_A_T = 'g:/Manga/downloads/Done/G.O.A.T/*'
Other = 'g:/Manga/downloads/Done/Other/*'
Rotten = 'g:/Manga/downloads/Done/Rotten/*'
MangaKakalot = 'g:/Manga/downloads/MangaKakalot/*'
Downloaded = 'g:/Manga/downloads/Downloaded/*'

files = glob.glob(G_O_A_T)
files += glob.glob(Other)
files += glob.glob(Rotten)
files += glob.glob(MangaKakalot)


files = [file.replace('g:/Manga/downloads/Done/G.O.A.T/', '') for file in files]
files = [file.replace('g:/Manga/downloads/Done/Other/', '') for file in files]
files = [file.replace('g:/Manga/downloads/Done/Rotten/', '') for file in files]
files = [file.replace('g:/Manga/downloads/MangaKakalot/', '') for file in files]
files = [file.replace('g:/Manga/downloads/Downloaded/', '') for file in files]


files = [file.lower() for file in files]


# print(files)


my_input = input("what are you searching for?: ").lower()


found = False

for file in files:
  if my_input in file:
    print("FOUND!!!")
    found = True
    break

if not found:
  print("Not found")