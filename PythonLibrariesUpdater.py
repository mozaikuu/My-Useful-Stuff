string = """
kiwisolver               1.4.5
lazy_loader              0.4
Levenshtein              0.25.1
libclang                 18.1.1
librosa                  0.10.2.post1
llvmlite                 0.43.0
Markdown                 3.6
markdown-it-py           3.0.0
MarkupSafe               2.1.5
matplotlib               3.9.0
matplotlib-inline        0.1.6
mdurl                    0.1.2
mkl                      2021.4.0
ml-dtypes                0.3.2
mpmath                   1.3.0
msgpack                  1.0.8
multidict                6.0.5
multiprocess             0.70.16
mysql-connector-python   9.0.0
namex                    0.0.8
nest-asyncio             1.6.0
networkx                 3.3
numba                    0.60.0
numpy                    1.26.3
oauthlib                 3.2.2
opencv-python            4.9.0.80
opt-einsum               3.3.0
optree                   0.11.0
outcome                  1.3.0.post0
packaging                23.2
pandas                   2.2.2
parso                    0.8.3
pillow                   10.2.0
pip                      24.1.1
platformdirs             4.1.0
polars                   1.0.0
pooch                    1.8.2
prompt-toolkit           3.0.43
proto-plus               1.24.0
protobuf                 4.25.3
psutil                   5.9.8
pure-eval                0.2.2
pyamaze                  1.0.1
pyarrow                  16.1.0
pyarrow-hotfix           0.6
pyasn1                   0.6.0
pyasn1_modules           0.4.0
pycparser                2.22
pygame-ce                2.5.0
Pygments                 2.17.2
pyparsing                3.1.2
PySocks                  1.7.1
python-dateutil          2.8.2
python-dotenv            1.0.1
python-Levenshtein       0.25.1
pytz                     2024.1
pywin32                  306
PyYAML                   6.0.1
pyzmq                    25.1.2
rapidfuzz                3.9.3
regex                    2024.5.15
requests                 2.32.3
requests-oauthlib        2.0.0
rich                     13.7.1
rsa                      4.9
safetensors              0.4.3
scikit-learn             1.5.0
scipy                    1.13.1
selenium                 4.22.0
setuptools               70.1.0
six                      1.16.0
sniffio                  1.3.1
sortedcontainers         2.4.0
soundfile                0.12.1
soxr                     0.3.7
sqlparse                 0.5.0
stack-data               0.6.3
sympy                    1.12.1
tbb                      2021.12.0
tensorboard              2.16.2
tensorboard-data-server  0.7.2
tensorflow               2.16.2
tensorflow-intel         2.16.2
termcolor                2.4.0
threadpoolctl            3.5.0
tokenizers               0.19.1
torch                    2.3.1
torchaudio               2.3.1
tornado                  6.4
tqdm                     4.66.4
traitlets                5.14.1
transformers             4.41.2
trio                     0.25.1
trio-websocket           0.11.1
typing_extensions        4.12.2
tzdata                   2024.1
uritemplate              4.1.1
urllib3                  2.2.2
wcwidth                  0.2.13
webdriver-manager        4.0.1
websocket-client         1.8.0
Werkzeug                 3.0.3
wheel                    0.43.0
wrapt                    1.16.0
wsproto                  1.2.0
xxhash                   3.4.1
yarl                     1.9.4
"""

arr = string.split("\n")
arr = list(filter(None, arr))

newarr = []

for lib in arr:
  for i in range(len(lib)):
    if lib[i] == " ":
      newarr.append(lib[:i])
      # print(lib[:i])
      break

# for lib in newarr:
#   print(lib)

import os


pipupd = "python.exe -m pip install --upgrade pip"
pyupd = ""
pyupd += f"pip install "

for lib in newarr:
  pyupd += lib + " "
  
# print(string)
os.system(pipupd)
os.system(pyupd)







# for i, lib in enumerate(arr):
#   if i % 2 == 0:
#     print(lib)
