# Seção de Comentários.

from Classes.Usuario import Usuario
from Classes.Comentario import Comentario

user = Usuario()

user.Usuario_nome = "Bruno"
user.Usuario_sobrenome = "Pontes"
user.Usuario_email = "Bruno@Pontes.com"

nome = user.Usuario_nome + " " + user.Usuario_sobrenome
email = user.Usuario_email

print(nome)
print(email)

print()

comentario = Comentario()

comentario.Comentario = "Este é um teste"
comentario.Comentario_user = user

coment = comentario.Comentario
usuario = comentario.Comentario_user.Usuario_nome

print("User: " + usuario)
print("Comentou: " + coment)
