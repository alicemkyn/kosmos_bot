from PIL import Image, ImageDraw, ImageFont
from datetime import datetime

def ss_add_date(image_name, month_picker, tckn):
    image = Image.open(image_name)
    draw = ImageDraw.Draw(image)
    font = ImageFont.load_default(size=90)
    current_time = 'TC NO: ' + tckn + '\nDeneme Saati: ' + datetime.now().strftime('%H:%M') + '\n' + month_picker + '_Icin Randevu Bulunamadi.'+'\n'
    width, height = image.size
    text_x = width / 2
    text_y = height / 2
    
    text_color = (0,0,0)
    
    draw.text((text_x, text_y), current_time, font=font, fill=text_color)
    image.save(image_name)

def ss_found(image_name):
    image = Image.open(image_name)
    draw = ImageDraw.Draw(image)
    font = ImageFont.load_default(size=100)
    current_time = 'Deneme Saati:\n' + datetime.now().strftime('%H:%M')
    width, height = image.size
    text_x = width / 2
    text_y = height / 2
    text_color = (0, 0, 0)
    draw.text((text_x, text_y), current_time, font=font, fill=text_color)
    image.save(image_name)

if __name__ == '__main__':
    pass