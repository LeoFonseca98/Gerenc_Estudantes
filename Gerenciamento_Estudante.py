import textwrap

class Curso:
    def __init__(self, nome):
        self.nome = nome
        self.estudantes = []

    def listar_estudantes_curso(self):
        if self.estudantes:
            print(f"Estudantes matriculados no curso de {self.nome}")
            for estudante in self.estudantes:
                print(f"- {estudante.nome} (Matrícula: {estudante.matricula})")
        else:
            print(f"Não há estudantes matriculados no curso de {self.nome}")


class Estudante:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        self.cursos = []
    
    def realizar_matricula(self, curso):
        if curso not in self.cursos:
            self.cursos.append(curso)
            curso.estudantes.append(self)
            print(f"Estudante {self.nome} foi matriculado no curso {curso.nome}.")

    def listar_cursos(self):
        if self.cursos:
            print(f"Cursos do estudante: {self.nome}")
            for curso in self.cursos:
                print(f"- {curso.nome}")
        else:
            print(f"O(A) estudante {self.nome} não está matriculado em nenhum curso!")


cursos = {}
estudantes = {}

def realizar_matricula():
    matricula = input("Informe a matricula: ")

    if matricula not in estudantes:
        print("Estudante não encontrado!")
        return

    listar_cursos()
    nome_curso = input("Informe o nome do curso: ")
    if nome_curso not in cursos:
        print(f"O curso {nome_curso} não está disponível!")
        return

    estudante = estudantes[matricula]
    curso = cursos[nome_curso]
    estudante.realizar_matricula(curso)

def listar_cursos():
    if cursos:
        for nome_curso, curso in cursos.items():
            print(f"Nome do Curso: {nome_curso}")
    else:
        print("Nenhum curso disponível.")
    
def cursos_estudante():
    matricula = input("Informe a matricula: ")
    print("Cursos do estudante")

    listar_cursos()

    if matricula not in estudantes:
        print("Estudante não encontrado!")
        return
    
    estudante = estudantes[matricula]
    estudante.listar_cursos()  

def criar_curso():
    nome = input("Informe o nome do curso: ")
    if nome in cursos:
        print(f"O curso {nome} já existe!")
    else:
        curso = Curso(nome)
        cursos[nome] = curso
        print(f"Curso {nome} foi criado com sucesso!")

def criar_estudante():
    nome = input("Informe o nome do Estudante: ")
    matricula = input("Informe a matrícula do estudante: ")

    if matricula in estudantes:
        print("O estudante já está cadastrado!")
    else: 
        estudante = Estudante(nome, matricula)
        estudantes[matricula] = estudante
        print(f"O estudante {nome} foi criado com sucesso!")

def listar_estudantes_curso():
    if cursos:
        for nome_curso, curso in cursos.items():
            curso.listar_estudantes_curso()
            print("=" * 40)
    else:
        print("Nenhum curso disponível.")


def menu():
    menu = """\n 
=============== MENU ===============
[RM]\t Realizar Matrícula
[LC]\t Listar Cursos
[CDE]\t Cursos do Estudante
[CC]\t Criar Curso
[CE]\t Criar Estudante
[LE]\t Listar Estudantes
[S]\t Sair
=> """
    
    return input(textwrap.dedent(menu))

def main():
    while True:
        opcao = menu()
    
        if opcao == "RM":
            realizar_matricula()

        elif opcao == "LC":
            listar_cursos()

        elif opcao == "CDE":
            cursos_estudante()

        elif opcao == "CC":
            criar_curso()
        
        elif opcao == "CE":
            criar_estudante()
        
        elif opcao == "LE":
            listar_estudantes_curso()

        elif opcao == "S":
            break

main()
