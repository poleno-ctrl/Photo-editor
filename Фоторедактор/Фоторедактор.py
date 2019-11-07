from PIL import Image
from random import randint as ran



def list_():
    global way
    print('''Вот список фильтров которые вы можете использовать:
    1. Тонирование
    2. Изнанка
    3. Черно-белый
    4. Два цвета
    5. Шумы
    6. Цветовой слайсер
    7. Отзеркаливание
    8. Рябь''')
    menu()
def choosing():
    global way
    enter=input().lower()
    if enter=='список':
        list_()
        menu()
    else:
        if enter=='1':
            print('Поместите файл с фотографией в папку Загруженные фотографии и введите название файла с расширением')
            tonirovka()
            save()
        elif enter=='2':
            print('Поместите файл с фотографией в папку Загруженные фотографии и введите название файла с расширением')
            obratka()
            save()
        elif enter=='3':
            print('Поместите файл с фотографией в папку Загруженные фотографии и введите название файла с расширением')
            old()
            save()
        elif enter=='4':
            print('Поместите файл с фотографией в папку Загруженные фотографии и введите название файла с расширением')
            two_colors()
            save()
        elif enter=='5':
            print('Поместите файл с фотографией в папку Загруженные фотографии и введите название файла с расширением')
            noise()
            save()
        elif enter=='6':
            print('Поместите файл с фотографией в папку Загруженные фотографии и введите название файла с расширением')
            four_colors()
            save()
        elif enter=='7':
            print('Поместите файл с фотографией в папку Загруженные фотографии и введите название файла с расширением')
            mirror()
            save()
        elif enter=='8':
            print('Поместите файл с фотографией в папку Загруженные фотографии и введите название файла с расширением')
            ripple()
            save()
        else:
            print('Я не знаю такой команды')
            print('Попробуй использовать знакомые мне команды')
            menu()



def tonirovka():
    global img, way
    way=input()
    way='Загруженные фотографии/'+way
    print('Введите цвет в который вы хотите затонировать вашу фотографию (зеленый, красный, синий)') 
    color=input().lower()
    if color!='зеленый':
        if color!='красный':
            if color!='синий':
                print('Введено недопустимое значение')
                menu()
    print('Введите мощность тонировки от 0 до 255')
    power=int(input())
    if power>255 or power<0:
        print('Некорректное значение')
        menu()
    img = Image.open(way)
    img = img.convert(mode="RGBA")
    pixels = img.load()
    i = 0
    while i < img.width:
        j = 0
        while j < img.height:
            r, g, b, a = pixels[i, j]
            if color=='красный':
                r = r + power
                if r>255:
                    r=255
            elif color=='зеленый':    
                g=g+power
                if g>255:
                    g=255
            elif color=='синий':
                b=b+power
                if b>255:
                    b=255
            else:
                print('Вы ввели непонятное значение')
                menu()
            pixels[i, j] = (r, g, b, a)
            j = j + 1
        i = i + 1
    img.show()



def obratka():
    global img, way
    way=input()
    way='Загруженные фотографии/'+way
    img = Image.open(way)
    img = img.convert(mode="RGBA")
    pixels = img.load()
    i = 0
    while i < img.width:
        j = 0
        while j < img.height:
            r, g, b, a = pixels[i, j]
            r=255-r
            g=255-g
            b=255-b
            pixels[i, j] = (r, g, b, a)
            j+=1
        i = i + 1
    img.show()


    
def old():
    global img, way
    way=input()
    way='Загруженные фотографии/'+way
    img = Image.open(way)
    img = img.convert(mode="RGBA")
    pixels = img.load()
    i = 0
    while i < img.width:
        j = 0
        while j < img.height:
            r, g, b, a = pixels[i, j]
            a1=(r+g+b+a)//3
            r=a1
            g=a1
            b=a1
            a=a
            pixels[i, j] = r, g, b, a
            j = j + 1
        i = i + 1

    img.show()


    
def two_colors():
    global img, way
    way=input()
    way='Загруженные фотографии/'+way
    print('Выберите цвет в который частично будет закрашено фото (зеленый, синий, красный, черный)')
    color_2=input().lower()
    if color_2!='зеленый':
        if color_2!='красный':
            if color_2!='синий':
                if color_2!='черный':
                    print('Неправильное значение')
                    menu()
    img = Image.open(way)
    img = img.convert(mode="RGBA")
    pixels = img.load()
    i = 0
    y=0
    x=0
    while i <img.width:
        j=0
        while j < img.height:
            r, g, b, a =pixels[i, j]
            x+=1
            y= y+r+g+b
            pixels[i, j]= r, g, b, a
            j+=1
        i+=1
    y=y//3//x
    i=0
    while i < img.width:
        j = 0
        while j < img.height:
            r, g, b, a = pixels[i, j]
            if color_2=='зеленый':
                if (r+g+b)//3<y:
                    r=0
                    g=255
                    b=0
                    a=a
                else:
                    r=255
                    g=255
                    b=255
                    a=a
            elif color_2=='синий':
                if (r+g+b)//3<y:
                    r=0
                    g=0
                    b=255
                    a=a
                else:
                    r=255
                    g=255
                    b=255
                    a=a
            elif color_2=='красный':
                if (r+g+b)//3<y:
                    r=255
                    g=0
                    b=0
                    a=a
                else:
                    r=255
                    g=255
                    b=255
                    a=a
            elif color_2=='черный':
                if (r+g+b)//3<y:
                    r=0
                    g=0
                    b=0
                    a=a
                else:
                    r=255
                    g=255
                    b=255
                    a=a
            pixels[i, j] = (r, g, b, a)
            j = j + 1
        i = i + 1
    img.show()


    
def noise():
    global img, way
    way=input()
    way='Загруженные фотографии/'+way
    print('Оцените мощность шумов от 0 до 100')
    power=int(input())
    if power<0 or power>100:
        print('Вы ввели недопустимое значение')
        menu()
    img = Image.open(way)
    img = img.convert(mode="RGBA")
    pixels = img.load()
    i = 0
    while i < img.width:
        j = 0
        while j < img.height:
            r, g, b, a = pixels[i, j]
            c=ran(0,round(power*2.55))
            r+=c%255
            g+=c%255
            b+=c%255
            a+=c%255
            pixels[i, j] = (r, g, b, a)
            j = j + 1
        i = i + 1
    img.show()


    
def four_colors():
    global img, way
    way=input()
    way='Загруженные фотографии/'+way
    img = Image.open(way)
    img = img.convert(mode="RGBA")
    pixels = img.load()
    i = 0
    while i < img.width//2:
        j = 0
        while j < img.height//2:
            r, g, b, a = pixels[i, j]
            r+=50%255
            g+=100%255
            b+=150%255
            a+=200%255
            pixels[i, j] = (r, g, b, a)
            j = j + 1
        i = i + 1

    i=img.width//2
    while i < img.width:
        j = 0
        while j < img.height//2:
            r, g, b, a = pixels[i, j]
            r+=100%255
            g+=50%255
            b+=200%255
            a+=150%255
            pixels[i, j] = (r, g, b, a)
            j = j + 1
        i = i + 1
    i=0
    while i < img.width//2:
        j = img.height//2
        while j < img.height:
            r, g, b, a = pixels[i, j]
            r+=200%255
            g+=150%255
            b+=100%255
            a+=50%255
            pixels[i, j] = (r, g, b, a)
            j = j + 1
        i = i + 1
    i=img.width//2
    while i < img.width:
        j = img.height//2
        while j < img.height:
            r, g, b, a = pixels[i, j]
            r+=50%255
            g+=200%255
            b+=100%255
            a+=150%255
            pixels[i, j] = (r, g, b, a)
            j = j + 1
        i = i + 1
    img.show()


    
def mirror():
    global img, way
    way=input()
    way='Загруженные фотографии/'+way
    print('Ты хочешь отзеркалить фотографию справа налево или слева направо? Справа налево-введите "Лево", если слева направо то введите "Право"')
    side=input().lower()
    if side!='право':
        if side!='лево':
            print('Неподходящее значение')
            menu()
    img = Image.open(way)
    img = img.convert(mode="RGBA")
    pixels = img.load()
    if side=='лево':        
        i = 0
        while i < img.width//2:
            j = 0
            while j < img.height:
                r, g, b, a = pixels[i, j]
                pixels[img.width-i-1, j] = (r, g, b, a)
                j = j + 1
            i = i + 1
    elif side=='право':
        i = img.width//2
        while i < img.width:
            j = 0
            while j < img.height:
                r, g, b, a = pixels[i, j]
                pixels[img.width-i-1, j] = (r, g, b, a)
                j = j + 1
            i = i + 1
    img.show()


    
def ripple():
    global img, way
    way=input()
    way='Загруженные фотографии/'+way
    img = Image.open(way)
    img = img.convert(mode="RGBA")
    pixels = img.load()
    print('Введите мощность ряби от 1 до 15')
    c=int(input())
    if c<1 or c>15:
        print('Значение должно быть от 1 до 15')
        menu()
    i = 0
    a1=0
    while i < img.width:
        j = 0
        while j < img.height:
            r, g, b, a = pixels[i, j]
            if j%2==0:
                a1+=1
                if a1%2==1:
                    r+=50
                    if r>255:
                        r=255
                    if i+c>=img.width:
                        pixels[i, j] = (r, g, b, a)
                    else:
                        pixels[i+c, j] = (r, g, b, a)
                else:
                    b+=50
                    if b>255:
                        b=255
                    if i-c<img.width:
                        pixels[i, j] = (r, g, b, a)
                    else:
                        pixels[i+c, j] = (r, g, b, a)
                    pixels[i-c, j] = (r, g, b, a)
            pixels[i, j] = (r, g, b, a)
            j = j + 1
        i = i + 1
    img.show()



def save():
    global way
    print('Введите название файла с расширением куда хотите сохранить отредактированную фотографию')
    print('Фотография будет сохранена в папку Отредактированные фотографии')
    way_2=input()
    img.save('Отредактированные фотографии/'+way_2, format='PNG')
    menu()


    
def menu():
    global way
    print('Если хотите использовать фильтр, то просто введите его номер')
    print('Если хотите увидеть список фильтров напишите "Список"')
    choosing()
    
    
    



print('Привет! Это форедактор')
print('У тебя будет несколько фильтров на выбор')
print('Тебе потребуется указать название файла с фотографией и его расширение')
print('Также вам надо будет указать название файла куда захотите сохранить отредактированную фотографию')
list_()
