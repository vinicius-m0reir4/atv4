from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

class UsuarioComum(Pessoa):
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade)
        self.matricula = matricula
        self.livros_emprestados = []

    def emprestar_livro(self, livro):
        if len(self.livros_emprestados) < 3 and livro.esta_disponivel():
            self.livros_emprestados.append(livro)
            livro.alterar_disponibilidade(False)

    def devolver_livro(self, livro):
        if livro in self.livros_emprestados:
            self.livros_emprestados.remove(livro)
            livro.alterar_disponibilidade(True)

class Administrador(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)

    def cadastrar_livro(self, titulo, autor, ano):
        return Livro(titulo, autor, ano)

class ItemBiblioteca(ABC):
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True

    @abstractmethod
    def esta_disponivel(self):
        pass

    @abstractmethod
    def alterar_disponibilidade(self, status):
        pass

class Livro(ItemBiblioteca):
    def __init__(self, titulo, autor, ano):
        super().__init__(titulo, autor)
        self.ano = ano

    def esta_disponivel(self):
        return self.disponivel

    def alterar_disponibilidade(self, status):
        self.disponivel = status

class Biblioteca:
    def __init__(self):
        self.livros = []
        self.usuarios = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def cadastrar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def listar_livros_disponiveis(self):
        return [livro for livro in self.livros if livro.esta_disponivel()]

    def listar_usuarios_com_livros(self):
        return [usuario for usuario in self.usuarios if usuario.livros_emprestados]

biblioteca = Biblioteca()
administrador = Administrador("Ana", 35)
livro1 = administrador.cadastrar_livro("Livro A", "Autor A", 2000)
livro2 = administrador.cadastrar_livro("Livro B", "Autor B", 2010)
biblioteca.adicionar_livro(livro1)
biblioteca.adicionar_livro(livro2)
usuario = UsuarioComum("João", 25, "12345")
biblioteca.cadastrar_usuario(usuario)
usuario.emprestar_livro(livro1)
usuario.devolver_livro(livro1)

print([livro.titulo for livro in biblioteca.listar_livros_disponiveis()])
print([(usuario.nome, [livro.titulo for livro in usuario.livros_emprestados]) for usuario in biblioteca.listar_usuarios_com_livros()])
