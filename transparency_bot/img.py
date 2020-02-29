from PIL import Image
from io import BytesIO


def white_to_transparent(raw_image):
    img = Image.open(BytesIO(raw_image))
    img = img.convert("RGBA")
    resized = img.resize(calc_dimensions(*img.size))

    datas = resized.getdata()
    newData = []
    for item in datas:
        if item[0] == 255 and item[1] == 255 and item[2] == 255:
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)

    bytes = BytesIO()
    resized.putdata(newData)
    resized.save(bytes, "PNG")
    return bytes


def calc_dimensions(width, height):
    if all(x <= 512 for x in (width, height)):
        return (width, height)

    larger = max(width, height)
    factor = larger / 512
    new_width = int(width // factor)
    new_height = int(height // factor)
    return (new_width, new_height)
