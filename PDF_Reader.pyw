# Interface gráfica
import tkinter as tk
from tkinter import ttk, filedialog, messagebox, StringVar, BooleanVar, DISABLED 
# Manipulação de pdf
import PyPDF2 as pdf
# API da Narração
from gtts import gTTS
# Salva e roda o aúdio
import os
# Deixa a janela responsiva durante a conversão PDF -> MP3
from threading import Thread

class PassouDoLimiteError(Exception):
    pass

class PDFNarrator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('400x160')
        self.resizable(False, False)
        self.title('PDF Reader')
        
        self.pag_limit = 50
        
        self.ent_text = StringVar()
        self.cbb_current_value = StringVar()
        self.cb_var = BooleanVar()
        
        self.create_widgets()
        
    def create_widgets(self):
        self.lbl = ttk.Label(text = "Idioma do PDF:")
        self.lbl.place(x=10, y=40)

        self.cbb = ttk.Combobox(self, textvariable = self.cbb_current_value)
        self.cbb['values'] = ["Português Brasileiro","Português","Inglês","Espanhol"]
        self.cbb['state'] = 'readonly'
        self.cbb.current(0)
        self.cbb.place(x=10, y=60)
        
        self.b1 = tk.Button(self, height = 1, width = 2, command = self.set_file_path)
        self.b1.place(x=10, y=9)

        self.b2 = tk.Button(self, font = ('Calibri 8'), text = "Narrar", height = 3, width = 61, command = lambda: Thread(target = self.start_func).start())
        self.b2.place(x=10, y=100)

        self.ent = tk.Entry(self, font = ('Calibri 8'), textvariable = self.ent_text, state = DISABLED)
        self.ent_text.set("Clique no botão a esquerda para selecionar o diretório do PDF.")
        self.ent.place(x=40, y=13, width = 345)
        
        self.cb = tk.Checkbutton(self, text = "Narração lenta", variable = self.cb_var, onvalue=1, offvalue=0)
        self.cb.place(x=160, y=57)
        
    def set_file_path(self):
        file_path_temp = filedialog.askopenfilename(filetypes=[("Arquivos PDF", "*.pdf")])
    
        if file_path_temp.lower().endswith('.pdf'):
            self.ent_text.set(file_path_temp)

        else:
            self.ent_text.set('Clique no botão a esquerda para selecionar o diretório do PDF.')
    
    def get_language(self):
        return(
            {
                "Português Brasileiro": ('pt-br', 'com.br'),
                "Português": ('pt', 'pt'),
                "Inglês": ('en', 'com'),
                "Espanhol": ('es', 'es')
            }
            [self.cbb_current_value.get()]
        )
        
    def start_func(self):
        try:
            pdf_obj = open(self.ent_text.get(), 'rb')
            reader = pdf.PdfReader(pdf_obj)

            if len(reader.pages) > self.pag_limit:
                raise PassouDoLimiteError

            texto_completo = ''

            self.b2.place_forget()
            self.pb = ttk.Progressbar(self, orient='horizontal', mode='determinate', length=375)
            self.pb.place(x=11, y=110)

            for pagina in range(len(reader.pages)):
                self.pb['value'] += int(100 / len(reader.pages))

                page_obj = reader.pages[pagina]
                texto_completo += page_obj.extract_text()

                self.title(f"PDF Reader - Carregando PDF ({int(self.pb['value'])}%)")
            pdf_obj.close()

            self.pb.place_forget()
            self.b2.place(x=10, y=100)

            self.title(f"PDF Reader - Inicializando narração")
            tts = gTTS(text = texto_completo, lang = self.get_language()[0], tld = self.get_language()[1], slow = self.cb_var.get())

            if self.cb_var.get():
                nome_pdf = f'{os.path.splitext(os.path.basename(self.ent_text.get()))[0]}_{self.get_language()[0]}-narracao-lenta'
            else:
                nome_pdf = f'{os.path.splitext(os.path.basename(self.ent_text.get()))[0]}_{self.get_language()[0]}'

            self.title(f"PDF Reader - Salvando arquivo")
            tts.save(f'{nome_pdf}.mp3')
            os.startfile(f'{nome_pdf}.mp3')

            self.title(f"PDF Reader -  Arquivo aberto")

        except Exception as err:
            self.title(f"PDF Reader - Erro ({type(err).__name__})")

            match type(err).__name__:
                case 'FileNotFoundError':
                    error_msg = "Selecione um PDF válido."

                case 'PassouDoLimiteError':
                    error_msg = f"Selecione um PDF com menos de {self.pag_limit} páginas."

                case _:
                    error_msg = "Tente novamente mais tarde."

            messagebox.showerror("Erro", error_msg)
        
    def run(self):
        self.mainloop()

PDFNarrator().run()
