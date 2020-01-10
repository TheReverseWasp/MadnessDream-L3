import numpy as np
import json

class Sparse_matrix:
    def __init__(self):
        self.sparse_dic = {}

    def prepare_dic(self, movie_dic):
        for id in movie_dic:
            self.sparse_dic[id] = []

    def read_ratings(self, ratings, ini, fin):
        line = ''
        while ini > 0:
            line = ratings.readline()
            ini, fin = ini - 1, fin - 1
        line = ratings.readline()
        while ini < fin and line:
            elem = line.split(',')
            self.sparse_dic[int(elem[1])].append([int(elem[0]), float(elem[2])])
            ini += 1
            line = ratings.readline()
        if ini == fin:
            return False, self.sparse_dic
        return True, self.sparse_dic

def read_movies(movies):
    line = movies.readline()
    line = movies.readline()
    answer_dic = {}
    while line:
        list_line = line.split(',')
        answer_dic[int(list_line[0])] = 'Pelicula: ' + list_line[1] + ', Genero:' + list_line[2]
        line = movies.readline()
    return answer_dic

#search in all jsons all the user ratings by id of movie
def read_json_by_pos(pos, to_search):
    answer = []
    ini = 0
    while ini < pos:
        with open(str(ini) + '.json', 'r') as js:
            temp_dic = json.load(js)
            for elem in temp_dic[str(to_search)]:
                answer.append(elem)
        ini += 1
    return answer

def main():
    read_and_generate = input('read and generate? y/n ')
    movies = open('movies.csv', 'r')
    movie_dic = read_movies(movies)
    pos = 0
    if read_and_generate == 'y':
        step = int(input('step? '))
        ini, fin = 1, step
        #could be improved with line cache ref: https://stackoverflow.com/questions/2444538/go-to-a-specific-line-in-python
        ratings = open('ratings.csv', 'r')
        Sparse_matrix_runner = Sparse_matrix()
        Sparse_matrix_runner.prepare_dic(movie_dic)
        continue_answer, dic_answer = Sparse_matrix_runner.read_ratings(ratings, ini, fin)
        with open(str(pos) + '.json', 'w') as fp:
            json.dump(dic_answer, fp)
        ratings.close()
        pos += 1
        ini += step
        fin += step
        while continue_answer == False:
            ratings = open('ratings.csv', 'r')
            Sparse_matrix_runner = Sparse_matrix()
            Sparse_matrix_runner.prepare_dic(movie_dic)
            continue_answer, dic_answer = Sparse_matrix_runner.read_ratings(ratings, ini, fin)
            with open(str(pos) + '.json', 'w') as fp:
                json.dump(dic_answer, fp)
            ratings.close()
            pos += 1
            ini += step
            fin += step
        #now pos is the number of jsons
        #notice that I don't need to read all elements, only the (1) element that I need
    else:
        pos = int(input('pos totales? 1 + el ultimo '))
    print(movie_dic)
    while True:
        print('elemento? ')
        id_movie = int(input())
        print(movie_dic[id_movie], ' ==> ', read_json_by_pos(pos, id_movie))

if __name__ == '__main__':
    main()
