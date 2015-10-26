

def hex_to_RGB(hex):
    return [int(hex[i:i+2], 16) for i in range(1,6,2)]

def RGB_to_hex(RGB):
    RGB = [int(x) for x in RGB]
    return "#"+"".join(["0{0:x}".format(v) if v < 16 else "{0:x}".format(v) for v in RGB])

def color_dict(gradient):
    return {"hex":[RGB_to_hex(RGB) for RGB in gradient],
            "r":[RGB[0] for RGB in gradient],
            "g":[RGB[1] for RGB in gradient],
            "b":[RGB[2] for RGB in gradient]}

def linear_gradient(start_hex, finish_hex="#FFFFFF", n=10):
    s = hex_to_RGB(start_hex)
    f = hex_to_RGB(finish_hex)
    RGB_list = [s]
    for t in range(1, n):
        curr_vector = [
                int(s[j] + (float(t)/(n-1))*(f[j]-s[j])) for j in range(3) ]
        RGB_list.append(curr_vector)
    return color_dict(RGB_list)


