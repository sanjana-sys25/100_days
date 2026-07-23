import qrcode

# 1. Initialize the QRCode object with custom settings
qr = qrcode.QRCode(
    version=1,  # Controls the size of the QR Code (1 = 21x21 grid, up to 40)
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # High error correction (~30% damage recovery)
    box_size=8, # Size of each individual square pixel in the QR code
    border=4,    # Width of the outer white border (minimum is 4)
)

# 2. Add the data/URL you want to embed
data_to_encode = "https://github.com/sanjana-sys25"
qr.add_data(data_to_encode)

# 3. Compile the structure
qr.make(fit=True)

# 4. Generate the image with custom colors
img = qr.make_image(fill_color="green", back_color="white")

# 5. Save the image to your disk
img.save("custom_github_qr.png")

print("QR Code generated successfully!")