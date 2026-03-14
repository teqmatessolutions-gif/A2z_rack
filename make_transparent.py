from PIL import Image

def make_transparent(input_path, output_path, bg_color="white", tolerance=30):
    img = Image.open(input_path).convert("RGBA")
    datas = img.getdata()
    
    newData = []
    for item in datas:
        # Check if color is close to white
        if bg_color == "white":
            if item[0] > 255 - tolerance and item[1] > 255 - tolerance and item[2] > 255 - tolerance:
                newData.append((255, 255, 255, 0)) # transparent
            else:
                newData.append(item)
        elif bg_color == "black":
            if item[0] < tolerance and item[1] < tolerance and item[2] < tolerance:
                newData.append((0, 0, 0, 0)) # transparent
            else:
                newData.append(item)
    
    img.putdata(newData)
    img.save(output_path, "PNG")
    print(f"Saved transparent image to {output_path}")

try:
    make_transparent("d:\\perfumes\\a2z-racks\\logo-white.jpg", "d:\\perfumes\\a2z-racks\\logo-transparent.png", "white", 40)
except Exception as e:
    print(f"Error: {e}")
