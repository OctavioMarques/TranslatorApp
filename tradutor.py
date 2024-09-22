from tkinter import Tk, Label, Button, Text, Scrollbar, filedialog, messagebox, END
from deep_translator import GoogleTranslator

# Função para traduzir texto simples
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

# Função para carregar o arquivo .srt
def carregar_ficheiro():
    file_path = filedialog.askopenfilename(filetypes=[("SRT files", "*.srt")])
    if file_path:
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                conteudo_ficheiro = file.read()
                texto_entrada.delete("1.0", END)
                texto_entrada.insert(END, conteudo_ficheiro)
                global srt_file_path
                srt_file_path = file_path
        except Exception as e:
            messagebox.showerror("Erro", f"Não foi possível abrir o ficheiro: {str(e)}")

# Função para traduzir o conteúdo do ficheiro .srt
def traduzir_ficheiro():
    try:
        tradutor = GoogleTranslator(source='auto', target='pt')
        linhas = texto_entrada.get("1.0", END).splitlines()

        linhas_traduzidas = []
        for linha in linhas:
            if '-->' in linha or linha.strip().isdigit() or not linha.strip():
                linhas_traduzidas.append(linha)  # Manter linhas de tempo e vazias
            else:
                linhas_traduzidas.append(tradutor.translate(linha))

        texto_saida.delete("1.0", END)
        texto_saida.insert(END, '\n'.join(linhas_traduzidas))
    except Exception as e:
        texto_saida.delete("1.0", END)
        texto_saida.insert(END, "Erro: " + str(e))

# Função para salvar o ficheiro traduzido
def salvar_ficheiro():
    file_path = filedialog.asksaveasfilename(defaultextension=".srt", filetypes=[("SRT files", "*.srt")])
    if file_path:
        try:
            with open(file_path, 'w', encoding='utf-8') as file:
                conteudo_traduzido = texto_saida.get("1.0", END)
                file.write(conteudo_traduzido)
            messagebox.showinfo("Sucesso", "Ficheiro traduzido salvo com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", f"Não foi possível salvar o ficheiro: {str(e)}")

# Interface gráfica com Tkinter
app = Tk()
app.title("Tradutor de Texto e Ficheiros .srt")
app.geometry("600x500")

# Título
label_titulo = Label(app, text="Tradutor de Inglês para Português", font=("Arial", 16))
label_titulo.pack(pady=10)

# Caixa de texto para entrada
texto_entrada = Text(app, height=10, width=60)
texto_entrada.pack()

# Botão para traduzir texto simples
botao_traduzir = Button(app, text="Traduzir Texto", command=traduzir)
botao_traduzir.pack(pady=5)

# Botão para carregar o ficheiro .srt
botao_carregar_ficheiro = Button(app, text="Carregar Ficheiro .srt", command=carregar_ficheiro)
botao_carregar_ficheiro.pack(pady=5)

# Botão para traduzir o ficheiro .srt
botao_traduzir_ficheiro = Button(app, text="Traduzir Ficheiro .srt", command=traduzir_ficheiro)
botao_traduzir_ficheiro.pack(pady=5)

# Botão para salvar o ficheiro traduzido
botao_salvar_ficheiro = Button(app, text="Salvar Ficheiro Traduzido", command=salvar_ficheiro)
botao_salvar_ficheiro.pack(pady=5)

# Caixa de texto para saída
texto_saida = Text(app, height=10, width=60)
texto_saida.pack()

# Scrollbar
scroll = Scrollbar(app, command=texto_saida.yview)
scroll.pack(side="right", fill="y")
texto_saida.config(yscrollcommand=scroll.set)

app.mainloop()
