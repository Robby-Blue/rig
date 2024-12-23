# normal RGBA hex codes dont seem to be supported
# everywhere, like in the svg latex package. instead
# the color need to be given in RGB with an added
# 'opacity' field ranging from 0.0 to 1.0 

def hex_to_rgba_alpha_str(hex_int):
    red = (hex_int >> 24) & 0xFF
    green = (hex_int >> 16) & 0xFF
    blue = (hex_int >> 8) & 0xFF
    alpha = hex_int & 0xFF

    rgb_string = f"#{red:02X}{green:02X}{blue:02X}"

    alpha_float = alpha / 255.0

    return rgb_string, alpha_float

def hex_to_tuple(hex_int):
    red = (hex_int >> 24) & 0xFF
    green = (hex_int >> 16) & 0xFF
    blue = (hex_int >> 8) & 0xFF
    alpha = hex_int & 0xFF

    return (red, green, blue, alpha)