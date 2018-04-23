import base64

def getImageBase64(image_path):
  with open(image_path, "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read())
    image_file.close
    print(encoded_string.decode("utf-8"))

#Call the function: Provide the actual path of the image
getImageBase64("C:\Downloads\image.png")


