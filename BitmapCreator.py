from math import sin, pi

y_offset = -1
t = 0
all_values = []
STEP = 0.005
while t <= 2 * pi:
    x = round(sin(5 * t + pi / 2), 2)
    y = round(sin(6 * t), 2)
    all_values.append((x, y))
    t += STEP
all_values.reverse()

with open('test.bmp', 'w+b') as f:
    f.write(b'BM')
    f.write((78).to_bytes(4, byteorder='little'))
    f.write((0).to_bytes(2, byteorder='little'))
    f.write((0).to_bytes(2, byteorder='little'))
    f.write((62).to_bytes(4, byteorder='little'))

    f.write((40).to_bytes(4, byteorder='little'))
    f.write((400).to_bytes(4, byteorder='little'))
    f.write((400).to_bytes(4, byteorder='little'))
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

    for y_counter in range(400):
        x_offset = -1
        for x_counter in range(400):
            if (x_offset, y_offset) in all_values:
                f.write(b'\x00\x00\x00')
            else:
                f.write(b'\xFF\xFF\xFF')
            x_offset = round(x_offset + STEP, 3)
        y_offset = round(y_offset + STEP, 3)
