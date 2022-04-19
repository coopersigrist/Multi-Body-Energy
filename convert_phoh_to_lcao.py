import numpy as np
from tqdm import tqdm

PHOH_STRUCTURE = 'HCCHCHCHOCHCH'
NAME_PREFIX = 'phoh_'
N_PHOH = 3
N_ATOMS = 13

def make_line(symbol, x, y, z):
    """
    Creates a line in the format of the LCAO dataset. For example:
        C 0 -1 -1.2\n

    Parameters:
        symbol (str): The symbol representing the element.
        x (np.float64): The x atomic coordinate.
        y (np.float64): The y atomic coordinate.
        z (np.float64): The z atomic coordinate.

    Returns:
        A string representing a line in the LCAO dataset for an element.
    """
    return f"{symbol} {x} {y} {z}\n"

def convert_format(x_filename, y_filename, out_filename):
    """
    Converts a PHOH dataset to LCAO format.

    Parameters:
        x_filename (str): Filename of training data in the format of PHOH dataset. Note: the data should be shape Nx39x3.
        y_filename (str): Filename of the label data in the format of PHOH dataset. Note: the data should be shape Nx1.
        out_filename (str): Filename of the converted dataset into LCAO format.
    """
    data = np.load(x_filename)
    labels = np.load(y_filename)

    f = open(out_filename, 'w')

    # Iterate for each sample
    for i, x in enumerate(tqdm(data)):
        lines = []

        # Name is in the format of phoh_00000001
        f.write(NAME_PREFIX + str(i+1).zfill(8))
        f.write('\n')

        # For each atomic coordinate in the sample
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

