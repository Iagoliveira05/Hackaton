from tkinter import *

class Tela:
    cor_fundo = "#004E86"
    cor_opcoes = "#E30613"
    cor_botao = "#02172C"
    def __init__(self):
        self.root = root
        self.configura_tela()
        self.tela_principal()

        root.mainloop()

    def configura_tela(self):
        self.root.state("zoomed")
        self.root.configure(bg=self.cor_fundo)

    def tela_principal(self):
        lb_cadastrar = Label(self.root, text="Cadastrar", font="Arial 50 bold", bg=self.cor_fundo)
        lb_cadastrar.pack(pady=20)

        lb_tipo = Label(self.root, text="Escolha o tipo de venda:", font="Arial 40 bold", bg=self.cor_fundo)
        lb_tipo.place(relx=0.05, rely=0.3)

        self.vtipo_primeiro = StringVar()
        rb_locatario = Radiobutton(self.root, text="Locatário", font="Arial 30 bold", value="L", variable=self.vtipo_primeiro, bg=self.cor_opcoes)
        rb_locatario.place(relx=0.05, rely=0.55, relwidth=0.25, relheight=0.2)

        rb_fiador = Radiobutton(self.root, text="Fiador", font="Arial 30 bold", value="F", variable=self.vtipo_primeiro, bg=self.cor_opcoes)
        rb_fiador.place(relx=0.7, rely=0.55, relwidth=0.25, relheight=0.2)

        btn_confirmar = Button(self.root, text="Confirmar", font="Arial 40 bold", bg=self.cor_botao, fg="white", command=self.decisao_tipo)
        btn_confirmar.pack(side=BOTTOM, pady=20)

    def decisao_tipo(self):
        if self.vtipo_primeiro.get() == "L":
            self.tela_locatario()

        elif self.vtipo_primeiro.get() == "F":
            self.tela_fiador()

    def tela_locatario(self):
        fr_locatario = Frame(self.root, bg=self.cor_fundo)
        fr_locatario.place(relwidth=1, relheight=1)

        lb_locatario = Label(fr_locatario, text="Locatário", font="Arial 50 bold", bg=self.cor_fundo)
        lb_locatario.pack(pady=20)

        lb_tipo = Label(fr_locatario, text="Escolha o tipo de pessoa:", font="Arial 40 bold", bg=self.cor_fundo)
        lb_tipo.place(relx=0.05, rely=0.3)

        self.vtipo_pessoa_locatorio = StringVar()
        rb_fisica = Radiobutton(fr_locatario, text="Pessoa Física", font="Arial 30 bold", value="L", variable=self.vtipo_pessoa_locatorio, bg=self.cor_opcoes)
        rb_fisica.place(relx=0.05, rely=0.55, relwidth=0.25, relheight=0.2)

        rb_juridica = Radiobutton(fr_locatario, text="Fiador", font="Arial 30 bold", value="F", variable=self.vtipo_pessoa_locatorio, bg=self.cor_opcoes)
        rb_juridica.place(relx=0.7, rely=0.55, relwidth=0.25, relheight=0.2)

        btn_confirmar = Button(fr_locatario, text="Confirmar", font="Arial 40 bold", bg=self.cor_botao, fg="white", command=self.inserir_documentos)
        btn_confirmar.pack(side=BOTTOM, pady=20)

    def tela_fiador(self):
        self.inserir_documentos()

    def inserir_documentos(self):
        pass


root = Tk()
Tela()