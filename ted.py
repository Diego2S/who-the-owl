from PIL import Image

def redimensionar(imagem_origem, imagem_destino):
    # Abre a imagem
    img = Image.open(imagem_origem)

    # Redimensiona para 800x600
    img_redimensionada = img.resize((120, 120))

    # Salva com novo nome
    img_redimensionada.save(imagem_destino)
    print(f"Imagem salva como {imagem_destino}")

# Coloque o nome do arquivo aqui:
redimensionar("images/bomb.png", "images/bomb2.png")
