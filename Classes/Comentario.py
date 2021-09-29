from Classes.Usuario import Usuario


class Comentario(object):

    # Atributos
    __comentario_id = 0
    __comentario = ""
    __comentario_user = Usuario()

    def __init__(self):
        print("__init__ Comentario")
        # Desenvolver a classe Comentário

    # Getters

    @property
    def Comentario_id(self):
        return self.__comentario_id

    @property
    def Comentario(self):
        return self.__comentario

    @property
    def Comentario_user(self):
        return self.__comentario_user

    # Setters

    @Comentario_user.setter
    def Comentario_user(self, usuario):
        if isinstance(usuario, Usuario):
            self.__comentario_user = usuario
        else:
            print("Valor esperado inválido.")

    @Comentario.setter
    def Comentario(self, comentario_parm):
        if isinstance(comentario_parm, str):
            self.__comentario = comentario_parm
        else:
            print("Valor esperado inválido.")

