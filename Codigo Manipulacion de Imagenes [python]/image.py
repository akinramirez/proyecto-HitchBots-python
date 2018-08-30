from PIL import Image
from PIL import ImageFilter

try:
  img = Image.open("images/parrot.jpg")
  # print(img.mode)
  # print(img.getpixel((100,200)))
  # img = img.convert("L") #Nos regresa una nueva imagen 
  # img = img.rotate(40,expand=True)
  # img = img.transpose( Image.ROTATE_270 )
  # print(img.size)
  # print(img.width)
  # print(img.height)
  
  # img = img.resize( (img.width/2,img.height/2) )
  # img.save("images/news/parrot.jpg")

  # box = (150, 100, 400, 300)
  # img = img.crop(box)

  # img = img.filter( ImageFilter.BLUR )

  copy = img.resize( (100,100))
  img.paste(copy, (100,100) )
  img.save("images/news/parrot.jpg")

  img.show()
except IOError:
  print("No es posible abrir la imagen!")
