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
    x = pd.read_csv(csv, sep = ',', encoding = 'latin-1')
    x = x.iloc[:,:]
    X = np.array(x)
    return X

def main():
    X = read_normal_csv('ratings.csv')
    Xt = np.transpose(X)

    Sparsa_ = csr_matrix((Xt[2], (Xt[0].astype(int), Xt[1].astype(int))), dtype=np.float64).toarray()
    movies = read_csv('movies.csv')
    answer = [[movies[0][i][1], movies[0][i][2], Sparsa_[i]] for i in range(len(Sparsa_))]
    print(answer)

if __name__ == "__main__":
    main()
