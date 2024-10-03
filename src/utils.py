# normal RGBA hex codes dont seem to be supported
# everywhere, like in the svg latex package. instead
# the color need to be given in RGB with an added
# 'opacity' field ranging from 0.0 to 1.0 

def hex_rgba_to_rgba_alpha(hex_str):
    # add some system to allow colors like 'green'
    # maybe allow users to map names to hex values first
    # or just print a warning and pass it on with opacity of 1
    
    if hex_str[0] == "#":
        hex_str = hex_str[1:]

    if len(hex_str) == 6:
        return "#"+hex_str, 1
    if len(hex_str) == 8:
        return "#"+hex_str[:6], int(hex_str[7:8], 16) / 255
    
    # 'orange' doesnt get this far
    # probably try to hex parse it and if
    # it fails error too
    # or trust users to be smart and figure it our
    # themselves
    raise ValueError(f"Bad color {hex_str}")

def rgba_alpha_to_hex(rgb_str, opacity):
    return "#" + rgb_str + "{:02X}".format(int(opacity*255))