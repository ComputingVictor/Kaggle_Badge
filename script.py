# Importamos las funciones específicas desde el archivo functions.py
from functions import obtener_avatar_kaggle, create_kaggle_profile_card

def main():
    # Pedimos al usuario que introduzca el nombre de usuario de Kaggle
    user = input("Por favor, introduce el nombre de usuario de Kaggle: ")


    # Obtenemos el avatar del usuario de Kaggle
    avatar = obtener_avatar_kaggle(user)
    print(f"Avatar obtenido: {avatar}")


    # Creamos la tarjeta de perfil de Kaggle para el usuario
    profile_card = create_kaggle_profile_card(user)
    print("Tarjeta de perfil de Kaggle creada con éxito.")

if __name__ == "__main__":
    main()
