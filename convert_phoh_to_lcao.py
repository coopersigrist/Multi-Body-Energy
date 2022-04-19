import numpy as np
from tqdm import tqdm

PHOH_STRUCTURE = 'HCCHCHCHOCHCH'
NAME_PREFIX = 'phoh_'
N_PHOH = 3
N_ATOMS = 13

def make_line(symbol, x, y, z):
    return f"{symbol} {x} {y} {z}\n"

def convert_format(x_filename, y_filename, out_filename):
    data = np.load(x_filename)
    labels = np.load(y_filename)

    f = open(out_filename, 'w')

    for i, x in enumerate(tqdm(data)):
        lines = []

        f.write(NAME_PREFIX + str(i+1).zfill(8))
        f.write('\n')

        for j, atom_coord in enumerate(x):
            x = atom_coord[0]
            y = atom_coord[1]
            z = atom_coord[2]
            symbol = PHOH_STRUCTURE[j%N_ATOMS]
            lines.append(make_line(symbol, x, y, z))

        f.writelines(lines)
        f.write(str(labels[i]))
        f.write('\n\n')
    f.close()



if(__name__ == '__main__'):
    convert_format('abs_pos_phoh.npy', 'y_phoh.npy', 'converted.txt')

