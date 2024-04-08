import re
import requests
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
import matplotlib.pyplot as plt
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

def obtener_avatar_kaggle(user):
    # Configura Selenium para usar Chrome
    service = Service(ChromeDriverManager().install())
    # Dont open the browser
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    # Driver
    driver = webdriver.Chrome(service=service,options=options)

    # Abre la URL objetivo
    driver.get(f'https://www.kaggle.com/{user}')

    # Usa una espera implícita si es necesario para asegurar que la página haya cargado
    driver.implicitly_wait(10)

    # Encuentra el elemento por su atributo data-testid
    elemento = driver.find_element(By.CSS_SELECTOR, 'div[data-testid="avatar-image"]')

    # Extrae el valor del atributo 'style' del elemento
    style_attr = elemento.get_attribute('style')

    # Cierra el navegador
    driver.quit()


    url_match = re.search(r'url\("([^"]+)"\)', style_attr)[1]


        # Verifica si la URL es completa o relativa
    if not url_match.startswith('http'):
            # Asume que la URL es relativa y decide no cargarla (o ajusta según sea necesario)
            image_path = "img/default-avatar.png"
            image = Image.open(image_path)
            # Guarda la imagen en el disco
            image.save('avatar.png')
    else:
            # La URL es completa, realiza una solicitud HTTP GET para obtener la imagen
            response = requests.get(url_match)
            image = Image.open(BytesIO(response.content))
            plt.axis('off')  # Oculta los ejes

            # Guarda la imagen en el disco
            image.save('avatar.png')





def create_kaggle_profile_card(user):
    # Configura Selenium para usar Chrome
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(service=service, options=options)

    # Abre la URL objetivo
    driver.get(f'https://www.kaggle.com/{user}')
    driver.implicitly_wait(10)

    # Encuentra el elemento por su atributo data-testid
    elemento = driver.find_element(By.XPATH, '/html/body/main/div[1]/div/div[5]/div[2]/div[2]/div/div/div[5]/div[1]/div[1]')
    matches = re.findall(r"(Competitions|Datasets|Notebooks|Discussions)\n([A-Za-z]+)\nMEDALS\n(?:none yet|(\d+)(?:\n(\d+)(?:\n(\d+))?)?)", elemento.text)
    driver.quit()

    datos_nuevos = {match[0]: {"Level": match[1], "Gold": 0, "Silver": 0, "Bronze": 0} for match in matches}
    for match in matches:
        category = match[0]
        medallas = [int(x) if x.isdigit() else 0 for x in match[2:]]
        if len(medallas) == 3:
            datos_nuevos[category]["Gold"], datos_nuevos[category]["Silver"], datos_nuevos[category]["Bronze"] = medallas
        elif len(medallas) == 2:
            datos_nuevos[category]["Silver"], datos_nuevos[category]["Bronze"] = medallas
        elif len(medallas) == 1:
            datos_nuevos[category]["Bronze"] = medallas[0]

    for category, details in datos_nuevos.items():
        gold, silver, bronze = details["Gold"], details["Silver"], details["Bronze"]
        if bronze == 0 and silver == 0:
            details["Bronze"], details["Silver"], details["Gold"] = gold, 0, 0
        elif bronze == 0 and silver > 0:
            details["Bronze"], details["Silver"], details["Gold"] = silver, gold, 0

    df_ajustado_final = pd.DataFrame(datos_nuevos).T

    # Preparar la imagen
    img = Image.open('img/Kaggle_template.png')  # Asegúrate de tener esta imagen en la ruta correcta
    d = ImageDraw.Draw(img)
    fnt = ImageFont.truetype('notebooks/PPTelegraf-Regular.otf', size=40)  # Asegúrate de tener esta fuente o usa una alternativa

    # Extraer y procesar datos para la imagen
    jerarquia_niveles = ['Novice', 'Contributor', 'Expert', 'Master', 'Grandmaster']
    nivel_usuario = df_ajustado_final['Level'].apply(lambda x: jerarquia_niveles.index(x)).idxmax()
    nivel_usuario = df_ajustado_final.loc[nivel_usuario, 'Level']

    total_oro = df_ajustado_final.Gold.sum()
    total_plata = df_ajustado_final.Silver.sum()
    total_bronce = df_ajustado_final.Bronze.sum()

    # Añadir texto a la imagen
    d.text((120,55), f"{user}", font=fnt, fill=(0,0,0), align='center', stroke_width=2)
    d.text((220,105), f"{nivel_usuario}", font=fnt, fill=(0,0,0), align='center')
    d.text((75,640), f"{total_oro}", font=fnt, fill=(0,0,0), align='center')
    d.text((285,640), f"{total_plata}", font=fnt, fill=(0,0,0), align='center')
    d.text((475,640), f"{total_bronce}", font=fnt, fill=(0,0,0), align='center')

    # Añadir la imagen de perfil (asegúrate de tener 'avatar.png' disponible)
    imagen_perfil = Image.open('avatar.png')
    tamaño_perfil = 316
    factor_antialias = 4
    tamaño_antialias = tamaño_perfil * factor_antialias
    imagen_perfil = imagen_perfil.resize((tamaño_antialias, tamaño_antialias), Image.Resampling.LANCZOS)

    mascara = Image.new('L', (tamaño_antialias, tamaño_antialias), 0)
    dibujar = ImageDraw.Draw(mascara)
    dibujar.ellipse((0, 0, tamaño_antialias, tamaño_antialias), fill=255)

    perfil_redondeado = Image.new('RGBA', (tamaño_antialias, tamaño_antialias), (0, 0, 0, 0))
    perfil_redondeado.paste(imagen_perfil, (0, 0), mascara)
    perfil_redondeado = perfil_redondeado.resize((tamaño_perfil, tamaño_perfil), Image.Resampling.LANCZOS)

    img.paste(perfil_redondeado, (122, 180), perfil_redondeado)

    # Guardar y mostrar la imagen
    img.save('Kaggle_card.png')
    img.show()

    return df_ajustado_final

