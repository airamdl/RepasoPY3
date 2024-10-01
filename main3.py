#Usando una lista
user_pass = ["airam", "1234"]

user = user_pass[0]
passw = user_pass[1]

print(f"Usuario: {user}, Contraseña: {passw}")


# diccionario
d1 = {
  "Name": "Airam",
  "Password": "1227"
}
print(d1)

#Al llenarse, las contraseñas deben pasarse a un formato Hash (por ejemplo, SHA-512).
user_pass2 = ["airam", "1234"]

hash_passw= hash(user_pass2[1])
user_pass2[1] = hash_passw
print(user_pass2)