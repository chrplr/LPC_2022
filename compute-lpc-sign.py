import pandas as pd
import string

def remove_punctuation(text):
    punct = string.punctuation + chr(10)
    return text.translate(str.maketrans(punct, " " * len(punct)))


lexique = pd.read_csv('Lexique380.utf8.csv.gz')
lexique = lexique.drop_duplicates(subset='ortho', keep="first")
lexique.set_index('ortho', inplace=True)

phrases = """Le chat a renversé la gamelle de lait.
J'ai garé l'automobile devant le supermarché.
"""


for p in phrases.split('\n'):
    print(f'# {p}')
    pclean = remove_punctuation(p.lower())
    for w in pclean.split():
        cvcv = lexique.p_cvcv[w]
        print(f'{w}\t{cvcv}\t{cvcv.count("C")}')
