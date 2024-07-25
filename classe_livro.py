class Livro:
  def __init__(self, titulo, autor, categoria, ano_publicacao, ativo ):
    self.titulo = titulo
    self.autor = autor
    self.categoria = categoria
    self.ano_piblicacao = ano_publicacao
    self.ativo = ativo
    return
#Exemplo de retorno
  def lista_livro(self):
    print(f'Titulo: {self.titulo}')
    print(f'Autor: {self.autor}')
    print(f'Categoria: {self.categoria}')
    print(f'Ano de publicacao: {self.ano_publicacao}')
    print(f'Ativo: {self.ativo}')

    return self
#Exemplo de retorno
  def detalhes(self):
     return (f'Titulo: {self.titulo} - Autor: {self.autor} - Categoria: {self.categoria} - Ano de Publicação: {self.ano_piblicacao} - Ativo:{self.ativo}')
  
 

  livro_1 = ('Capitães da Areia','Jorge Amado','Fiction','1937','False')
  
  (livro_1.lista_livro())