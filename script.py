import sys
from functions import obtener_avatar_kaggle, create_kaggle_profile_card
import time

def main(user):
    # Obtenemos el avatar del usuario de Kaggle
    avatar = obtener_avatar_kaggle(user)
    print(f"Avatar obtenido")

    # Creamos la tarjeta de perfil de Kaggle para el usuario
    profile_card = create_kaggle_profile_card(user)
    print("Tarjeta de perfil de Kaggle creada con éxito.")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Este script requiere un nombre de usuario de Kaggle como argumento.")
        sys.exit(1)
    user = sys.argv[1]
    main(user)