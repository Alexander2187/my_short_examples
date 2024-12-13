from PIL import Image


def merge(picture):
    """
    Данный скрипт предназначен для наглядной демонстрации
        особенностей нашего зрения на примере перемещения цветовых каналов
        в выбранном Вами изображении.
    Позволяет рассмотреть особенности восприятия в разных интерпретациях одного и того-же изображения.
    Пояснение:
        В каждой строке будет находиться четыре картинки:
            три из них -> (красный канал, зелёный канал, синий канал) представленные в одном и том-же цвете
                и одна картинка -> каждый канал которой, один и тот-же цвет, что сделает её черно-белой.
        Последняя строка:
            каналы R, G, B и исходное изображение.
    """

    """
    Новое изображение из исходного стоится так: 

    [RGB] ---->     [R__][G__][B__][RRR]
                    [_R_][_G_][_B_][GGG]
                    [__R][__G][__B][BBB]
                    [R__][_G_][__B][RGB]

    Где --> "_" канал заполненный нулевыми значениями, что соответствует 
        нулевой яркости (т.е. "черный" для любого цвета).

    Другими словами получится 16 картинок в одной.
        Разрешение увеличится в 4 раза: 
            например для 1280 x 1024 станет 5120 x 4096.
    """
    """
    Если нужно, здесь можно уменьшить разрешение изображения, 
        которое используется далее в качестве исходного.

    Пример: 
    разрешение исходного изображения --> разрешение финального изображения
    scale = 1  -->       1280 x 1024 --> 5120 x 4096
    scale = 4  -->       1280 x 1024 --> 1280 x 1024
    scale = 8  -->       1280 x 1024 --> 640 x 512
    """
    # Понижение разрешения с потерей качества для ускорения демонстрации:
    scale = 4  # Во сколько раз уменьшить, "1" без изменений.
    width = int(picture.size[0] / scale)
    height = int(picture.size[1] / scale)
    picture = picture.resize((width, height))
    #
    # Разделение исходного изображения на каналы R, G, B.
    # zero: канал заполненный нулевыми значениями, что соответствует нулевой яркости
    channels = picture.split()
    zero = channels[0].point(lambda p: p * 0)  # Не менять.
    """
    Изменяя коэффициенты lambda у каналов от 0.1 до 4 можно добиться различных эффектов.
    """
    red = channels[0].point(lambda p: p * 1)  # (0.1 - 4),    "1" без изменений.
    green = channels[1].point(lambda p: p * 1)  # (0.1 - 4),    "1" без изменений.
    blue = channels[2].point(lambda p: p * 1)  # (0.1 - 4),    "1" без изменений.

    # Сборка строки из четырёх картинок
    def m_line():
        """
        Сборка строки из четырёх картинок
        """
        img = Image.new("RGB", (w, h))
        img.paste(red_only, (0, 0))
        img.paste(green_only, (picture_mix.size[0] * 1, 0))
        img.paste(blue_only, (picture_mix.size[0] * 2, 0))
        img.paste(picture_mix, (picture_mix.size[0] * 3, 0))

        return img

    # Подготовка картинок для первой строки
    red_only = Image.merge("RGB", (red, zero, zero))
    green_only = Image.merge("RGB", (green, zero, zero))
    blue_only = Image.merge("RGB", (blue, zero, zero))
    picture_mix = Image.merge("RGB", (red, red, red))
    # Установка ширины и высоты для строк
    w = picture_mix.size[0] * 4
    h = picture_mix.size[1]
    # Первая строка
    im1 = m_line()

    # Подготовка картинок для второй строки
    red_only = Image.merge("RGB", (zero, red, zero))
    green_only = Image.merge("RGB", (zero, green, zero))
    blue_only = Image.merge("RGB", (zero, blue, zero))
    picture_mix = Image.merge("RGB", (green, green, green))
    # Вторая строка
    im2 = m_line()

    # Подготовка картинок для третьей строки
    red_only = Image.merge("RGB", (zero, zero, red))
    green_only = Image.merge("RGB", (zero, zero, green))
    blue_only = Image.merge("RGB", (zero, zero, blue))
    picture_mix = Image.merge("RGB", (blue, blue, blue))
    # Третья строка
    im3 = m_line()

    # Подготовка картинок для четвертой строки
    red_only = Image.merge("RGB", (red, zero, zero))
    green_only = Image.merge("RGB", (zero, green, zero))
    blue_only = Image.merge("RGB", (zero, zero, blue))
    picture_mix = Image.merge("RGB", (red, green, blue))
    # Четвертая строка
    im4 = m_line()

    # Установка ширины и высоты финального изображения
    w = im1.size[0]
    h = im1.size[1] * 4
    # Заготовка финального изображения
    im = Image.new("RGB", (w, h))
    # Объединение строк в столбик, заполнение финального изображения
    im.paste(im1, (0, 0))
    im.paste(im2, (0, im1.size[1]))
    im.paste(im3, (0, im1.size[1] * 2))
    im.paste(im4, (0, im1.size[1] * 3))

    return im


"""
Поместите изображение в папку с этим скриптом
Укажите имя Вашего файла с расширением, например "SomePicture.jpg"
"""
name = "Sea_1024_1280.jpg"  # Укажите имя Вашего файла с расширением, например "SomePicture.jpg"
try:
    pic = Image.open(name)
    print(pic.format, pic.size, pic.mode)
    out = merge(pic)
    out.show()
    # Если желаете сохранить результат, удалите комментарий '#' на строке ниже
    # out.save("New_" + name, "JPEG")
except FileNotFoundError as e:
    print(f"???\nИзображение '{name}' не найдено в папке с этим скриптом!")
