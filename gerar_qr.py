import qrcode

# Insira o link aqui
link = "https://asturiasmc.com.br/"

# Gera o QR Code
qr = qrcode.QRCode(
    version=1,  # tamanho do QR (1 é o menor)
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(link)
qr.make(fit=True)

# Cria a imagem do QR Code
img = qr.make_image(fill_color="black", back_color="white")

# Salva a imagem
img.save("qrcode.png")

print("✅ QR Code gerado e salvo como 'qrcode.png'")
