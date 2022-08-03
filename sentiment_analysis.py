from textblob import TextBlob
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
import seaborn as sns
import matplotlib.pyplot as plt
from google_trans_new import google_translator

#LENDO O ARQUIVO DE DADOS
df = pd.read_csv('./data_example.csv', index_col=0)

#FUNCAO TRADUZIR O CONTEUDO
def translate(text):
    translator = google_translator()
    translate_text = translator.translate(text, lang_tgt='en')
    return translate_text

#FUNCAO QUE RETORNA VALOR DA POLARIDADE DOS DADOS
def polarity(text):
    return TextBlob(text).sentiment.polarity

#FUNCAO QUE ANALISA A POLARIDADE E RETORNA POSITIVO/NEUTRO/NEGATIVO
def analise(polaridade):
    if polaridade <= -0.10:
        return 'Negativo'
    elif polaridade == 0:
        return 'Neutro'
    elif polaridade < 0 and polaridade > -0.10:
        return 'Neutro'
    else:
        return 'Positivo'

#APLICANDO FUNCOES NOS DADOS
df['content_english'] = df['content'].apply(translate)
df['polaridade'] = df['content_english'].apply(polarity)
df['analise'] = df['polaridade'].apply(analise)

print(df['content'])
print(df['content_english'])
print(df['polaridade'])
print(df['analise'])
#SALVANDO RESULTADO EM UM NOVO ARQUIVO DE DADOS
df.to_csv("analise_sentimentos.csv", index = False)

'''# CRIANDO GRAFICO PARA VISUALIZAÇÃO DA ANALISE
df_analise = pd.DataFrame(df['analise'].value_counts())
plt.figure()
ax = sns.barplot(y=df_analise['analise'], x=df_analise.index, data=df)
ax.set_xlabel('Sentimento')
ax.set_ylabel(' ')
plt.show()'''