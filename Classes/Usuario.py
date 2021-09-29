class Usuario(object):

    # Atributos
    __usuario_id = 0
    __usuario_nome = ""
    __usuario_sobrenome = ""
    __usuario_email = ""

    def __init__(self):
        print("__init__ Usuario")

    # Getters

    @property
    def Usuario_id(self):
        return self.__usuario_id

    @property
    def Usuario_nome(self):
        return self.__usuario_nome

    @property
    def Usuario_sobrenome(self):
        return self.__usuario_sobrenome

    @property
    def Usuario_email(self):
        return self.__usuario_email

    # Setters

    @Usuario_nome.setter
    def Usuario_nome(self, nome):
        if isinstance(nome, str):
            self.__usuario_nome = nome
        else:
            print("Valor esperado ínvalido.")

    @Usuario_sobrenome.setter
    def Usuario_sobrenome(self, sobrenome):
        if isinstance(sobrenome, str):
            self.__usuario_sobrenome = sobrenome
        else:
            print("Valor esperado ínvalido.")

    @Usuario_email.setter
    def Usuario_email(self, email):
        if isinstance(email, str):
            self.__usuario_email = email
        else:
            print("Valor esperado ínvalido.")

