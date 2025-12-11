from PIL import Image

def redimensionar(imagem_origem, imagem_destino):
    # Abre a imagem
    img = Image.open(imagem_origem)

    # Redimensiona para 800x600
    img_redimensionada = img.resize((800, 600))

    # Salva com novo nome
    img_redimensionada.save(imagem_destino)
    print(f"Imagem salva como {imagem_destino}")

# Coloque o nome do arquivo aqui:
redimensionar("images/menu_background_800x600.png", "images/menu_background_800x600.png")
