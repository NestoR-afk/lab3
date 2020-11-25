from math import sin, pi

width = 400
height = 400
all_values = []
t = 0
STEP = 0.005
x_min = float('inf')
y_min = float('inf')

while t <= 2 * pi:
    x = round(sin(5 * t + pi / 2), 2)
    if x < x_min:
        x_min = x
    y = round(sin(6 * t), 2)
    if y < y_min:
        y_min = y
    all_values.append((x, y))
    t += STEP
all_values.reverse()

with open('test.bmp', 'wb') as f:
    f.write(b'BM')
    f.write((78).to_bytes(4, byteorder='little'))
    f.write((0).to_bytes(2, byteorder='little'))
    f.write((0).to_bytes(2, byteorder='little'))
    f.write((62).to_bytes(4, byteorder='little'))

    f.write((40).to_bytes(4, byteorder='little'))
    f.write(width.to_bytes(4, byteorder='little'))
    f.write(height.to_bytes(4, byteorder='little'))
    f.write((1).to_bytes(2, byteorder='little'))
    f.write((24).to_bytes(2, byteorder='little'))
    f.write((0).to_bytes(4, byteorder='little'))
    f.write((0).to_bytes(4, byteorder='little'))
    f.write((0).to_bytes(4, byteorder='little'))
    f.write((0).to_bytes(4, byteorder='little'))
    f.write((0).to_bytes(4, byteorder='little'))
    f.write((0).to_bytes(4, byteorder='little'))

    f.write(b'\x00\x00\x00\xFF')
    f.write(b'\xFF\xFF\xFF\xFF')

    y_of_pixel = y_min
    for y_counter in range(400):
        x_of_pixel = x_min
        for x_counter in range(400):
            if (x_of_pixel, y_of_pixel) in all_values:
                f.write(b'\x00\x00\x00')
            else:
                f.write(b'\xFF\xFF\xFF')
            x_of_pixel = round(x_of_pixel + STEP, 3)
        y_of_pixel = round(y_of_pixel + STEP, 3)
