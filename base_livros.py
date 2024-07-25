import pandas as pd
#Importando um arquivo csv

#df = pd.read_csv('tabela_livros.csv')
#print(df)

class Livro:
   def __init__(self, titulo, autor, categoria, ano_publicacao, ativo ):#Atributos da classe
        self.titulo = titulo#Intanciando as variaveis
        self.autor = autor
        self.categoria = categoria
        self.ano_piblicacao = ano_publicacao
        self.ativo = ativo
       

livro0 = Livro("livro0","Julio","Programação",2012,"Sim")
livro1 = Livro("livro1","Julio","Programação",2012,"Sim")
livro2 = Livro("livro2","Julio","Programação",2012,"Sim")
lista_de_livros = [livro0,livro1,livro2]

for livro in lista_de_livros:
    print(livro.titulo)






