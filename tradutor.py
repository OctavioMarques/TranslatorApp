from tkinter import Tk, Label, Button, Text, Scrollbar, END
from deep_translator import GoogleTranslator

# Função para traduzir texto
def traduzir():
    try:
        texto_original = texto_entrada.get("1.0", END)
        tradutor = GoogleTranslator(source='auto', target='pt')
        texto_traduzido = tradutor.translate(texto_original)
        texto_saida.delete("1.0", END)
        texto_saida.insert(END, texto_traduzido)
    except Exception as e:
        texto_saida.delete("1.0", END)
        texto_saida.insert(END, "Erro: " + str(e))

# Configurar a interface gráfica (Tkinter)
app = Tk()
app.title("Tradutor Simples")
app.geometry("500x400")

# Título
label_titulo = Label(app, text="Tradutor de Inglês para Português", font=("Arial", 16))
label_titulo.pack(pady=10)

# Caixa de texto para entrada
texto_entrada = Text(app, height=10, width=60)
texto_entrada.pack()

# Botão para traduzir
botao_traduzir = Button(app, text="Traduzir", command=traduzir)
botao_traduzir.pack(pady=10)

# Caixa de texto para saída
texto_saida = Text(app, height=10, width=60)
texto_saida.pack()

# Scrollbar
scroll = Scrollbar(app, command=texto_saida.yview)
scroll.pack(side="right", fill="y")
texto_saida.config(yscrollcommand=scroll.set)

app.mainloop()
