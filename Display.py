import os
import time
from PIL import Image, ImageTk
import tkinter as tk
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

# Autentica com a API do Google Drive
gauth = GoogleAuth()
gauth.RedirectURI = 'http://localhost:8090/'  # Define o URI de redirecionamento
gauth.LocalWebserverAuth()  # Abrirá uma página da web para autenticação

# Cria uma instância do GoogleDrive usando a autenticação
drive = GoogleDrive(gauth)

# ID do diretório no Google Drive contendo suas imagens
DRIVE_DIRECTORY_ID = "### adicione aqui seu ID diretório " # Tirei o anterior para não entrarem no meu drive xD

# Função para baixar as imagens do Google Drive
def download_images_from_drive(directory_id):
    images = drive.ListFile({'q': f"'{directory_id}' in parents and trashed=false"}).GetList()
    image_files = []
    for image in images:
        if image['mimeType'] in ['image/jpeg', 'image/png']:
            image.GetContentFile(image['title'])
            image_files.append(image['title'])
    return image_files

# Cria uma janela Tkinter
window = tk.Tk()
window.title("Apresentação de Slides de Imagens")

# Define a janela como fullscreen
window.attributes("-fullscreen", True)

# Variável para rastrear o índice da imagem atual
current_image_index = 0

# Função para exibir a próxima imagem
def show_next_image():
    global current_image_index
    if current_image_index < len(image_files):
        image_path = image_files[current_image_index]
        try:
            image = Image.open(image_path)
            image = image.resize((window.winfo_screenwidth(), window.winfo_screenheight()))  # Redimensiona a imagem para caber na tela cheia
            image_tk = ImageTk.PhotoImage(image)
            label.config(image=image_tk)
            label.image = image_tk  # Mantém uma referência para evitar a coleta de lixo
            current_image_index += 1
            window.after(5000, show_next_image)  # Agenda a próxima imagem após 5 segundos
        except Exception as e:
            print(f"Erro ao exibir a imagem {image_path}: {e}")

            # Se ocorrer um erro, continue para a próxima imagem
            current_image_index += 1
            show_next_image()
    else:
        # Se todas as imagens foram exibidas, reinicie do início
        current_image_index = 0
        download_images_from_drive(DRIVE_DIRECTORY_ID)
        show_next_image()

# Baixa as imagens do Google Drive
image_files = download_images_from_drive(DRIVE_DIRECTORY_ID)

# Cria uma etiqueta para exibir as imagens
label = tk.Label(window)
label.pack(fill="both", expand=True)

# Inicia a apresentação de slides
show_next_image()

# Função para encerrar a apresentação de slides com a tecla "Esc"
def end_slideshow(event):
    if event.keysym == "Escape":
        window.destroy()

# Vincula evento de pressionamento da tecla "Esc" para encerrar a apresentação de slides
window.bind("<Key>", end_slideshow)

# Executa o loop de eventos do Tkinter
window.mainloop()
