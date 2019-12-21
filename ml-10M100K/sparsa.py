import pandas as pd
import numpy as np
from scipy.sparse import csr_matrix

def read_csv(csv):
    x = pd.read_csv(csv, sep = ',', encoding = 'utf-8')
    y = x.iloc[:,-1]
    x = x.iloc[:,0:3]
    X = np.array(x)
    Y = np.array(y)
    return X, Y

def read_normal_csv(csv):
    x = pd.read_csv(csv, sep = '\:\:', encoding = 'latin-1', engine='python')
    x = x.iloc[:,:]
    X = np.array(x)
    return X

def main():
    name_1 = input('ingrese el nombre de ratings: ')
    X = read_normal_csv(name_1)
    Xt = np.transpose(X)
    Sparsa_ = csr_matrix((Xt[2], (Xt[0].astype(int), Xt[1].astype(int))), dtype=np.int8).toarray()
    name_2 = input('ingrese el nombre de movies: ')
    movies = read_normal_csv(name_2)
    answer = []
    movie_pos = 0
    for i in range(len(Sparsa_)):
        if movie_pos < len(movies) and movies[movie_pos][0] == i:
            answer.append([movies[movie_pos][1], movies[movie_pos][2], Sparsa_[i]])
            movie_pos += 1
        else:
            answer.append([-1, -1, Sparsa_[i]])
    print(answer)

if __name__ == "__main__":
    main()
