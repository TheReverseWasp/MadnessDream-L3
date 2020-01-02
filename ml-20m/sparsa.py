import pandas as pd
import numpy as np
from scipy.sparse import dok_matrix

chunksz = 3000000

def read_csv(csv):
    x = pd.read_csv(csv, sep = ',', encoding = 'utf-8')
    y = x.iloc[:,-1]
    x = x.iloc[:,0:3]
    X = np.array(x)
    Y = np.array(y)
    return X, Y

def read_normal_csv(csv, pag):
    counter = pag * chunksz
    dfn = pd.read_csv(csv, sep = ',', encoding = 'latin-1', dtype = np.float, skiprows = counter, nrows = chunksz, engine='python')
    X = np.array(dfn)
    print(X)
    return X

def read_text_csv(csv):
    dfn = pd.read_csv(csv, sep = ',', encoding = 'latin-1', skiprows = 0, nrows = 5000000, engine='python')
    X = np.array(dfn)
    print(X)
    return X


def main():
    name_1 = input('ingrese el nombre de ratings: ')
    name_2 = input('ingrese el nombre de movies: ')
    movies = read_text_csv(name_2)
    Sparse_matrix = dok_matrix((21000000,131263), dtype = np.float32)
    answer = []
    for i in range(0, 7):
        Xarray = read_normal_csv(name_1, i)
        Xtarray = np.transpose(Xarray)
        for col in range(0, len(Xtarray[0])):
            Sparse_matrix[int(Xtarray[1][col]), int(Xtarray[0][col])] = Xtarray[2][col]
        print(i)
    print(Sparse_matrix)
if __name__ == "__main__":
    main()
