# qr_code_generator

As indicated by his name, qr_code_generator is a simple program in python who generate a qr cod.

## Installation

You need those modules :

```bash
pip install qrcode
pip install Pillow
``` 

## Usage

```python
import qrcode

qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=100, border=2) # the version and the size/appearance

qr.add_data("https://afram.xyz") #add a link into your qr code
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white") #customize the apparence of your qr code
img.save("portfolio_code.png") # save the qr code as a png file
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## language
<img alt="Python" src="https://img.shields.io/badge/python%20-%2314354C.svg?&style=for-the-badge&logo=python&logoColor=white"/>