# 🖼️ Apresentação de Slides com Google Drive + Tkinter

Este projeto é um **script em Python** que cria uma **apresentação de slides fullscreen** com imagens armazenadas em um diretório do seu **Google Drive**, utilizando a biblioteca **Tkinter** para interface gráfica e **PyDrive** para integração com o Google Cloud.

---

## 🚀 Funcionalidades

* ✅ Autenticação via navegador com sua conta do Google.
* ✅ Download automático de imagens (`.jpg` ou `.png`) a partir de uma pasta no Google Drive.
* ✅ Exibição fullscreen com redimensionamento automático das imagens.
* ✅ Transição automática a cada 5 segundos.
* ✅ Encerramento da apresentação com a tecla `Esc`.

---

## 📂 Estrutura e Funcionamento

* **GoogleAuth**: Abre uma página local para autenticação com o Google (em `localhost:8090`).
* **GoogleDrive API**: Acessa os arquivos de imagem dentro de um diretório específico no Drive.
* **Tkinter**: Cria uma janela fullscreen para a apresentação.
* **Pillow (PIL)**: Lida com o redimensionamento e exibição das imagens.

---

## 🛠️ Como Usar

### 1. Instale as dependências

```bash
pip install pydrive pillow
```

### 2. Configure seu projeto no Google

1. Vá até o [Google Cloud Console](https://console.developers.google.com/)
2. Crie um novo projeto e ative a **Google Drive API**
3. Gere o arquivo `client_secrets.json` e coloque na mesma pasta do script

### 3. Adicione o ID da pasta do Google Drive

Substitua no script:

```python
DRIVE_DIRECTORY_ID = "### adicione aqui seu ID diretório "
```

> 🔒 Mesmo com o ID da pasta, a **autenticação local via navegador** é obrigatória por segurança.

---

## 💾 Executando o Script

Depois de tudo configurado, execute:

```bash
python nome_do_arquivo.py
```

Uma janela fullscreen será aberta e iniciará o slideshow.

---

## ⛔ Encerrando a Apresentação

Pressione `Esc` a qualquer momento para encerrar.

---

## 📌 Observações

* O script roda **localmente**, não é uma aplicação web.
* A cada ciclo completo, ele baixa as imagens do Drive novamente — isso garante atualizações mas pode ser otimizado.

---

## 💡 Melhorias Futuras

* [ ] Cache local para evitar redownloads desnecessários
* [ ] Controles manuais (próxima, anterior, pausa)
* [ ] Interface gráfica para escolher pasta do Drive dinamicamente

---

## 🧐 Requisitos

* Python 3.6+
* Conta Google com pasta de imagens no Drive
* Conexão com a internet
* `client_secrets.json` configurado corretamente

---

## 📄 Licença

Uso pessoal e educacional. Faça o que quiser com o código, mas não culpe o autor se quebrar alguma coisa. 😄
