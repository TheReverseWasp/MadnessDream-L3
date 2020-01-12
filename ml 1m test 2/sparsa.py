import numpy as np
import json
import time
import re

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
            elem = re.findall(r"[\w']+", line)
            self.sparse_dic[int(elem[1])].append([int(elem[0]), float(elem[2])])
            ini += 1
            line = ratings.readline()
        if ini == fin:
            return False, self.sparse_dic
        return True, self.sparse_dic

def read_movies(movies):
    line = movies.readline()
    answer_dic = {}
    while line:
        list_line = re.findall(r"[\w']+", line)
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
    movies = open('movies.dat', 'r', encoding='latin-1')
    movie_dic = read_movies(movies)
    pos = 0
    creation_file_t = 0
    read_time_loss = 0
    if read_and_generate == 'y':
        step = int(input('step? '))
        ini, fin = 0, step
        #could be improved with line cache ref: https://stackoverflow.com/questions/2444538/go-to-a-specific-line-in-python
        ratings = open('ratings.dat', 'r')
        Sparse_matrix_runner = Sparse_matrix()
        Sparse_matrix_runner.prepare_dic(movie_dic)
        start_read_time_loss = time.time()
        continue_answer, dic_answer = Sparse_matrix_runner.read_ratings(ratings, ini, fin)
        read_time_loss += time.time() - start_read_time_loss
        temp = time.time()
        with open(str(pos) + '.json', 'w') as fp:
            json.dump(dic_answer, fp)
        ratings.close()
        creation_file_t += time.time() - temp
        pos += 1
        ini += step
        fin += step
        while continue_answer == False:
            ratings = open('ratings.dat', 'r')
            Sparse_matrix_runner = Sparse_matrix()
            Sparse_matrix_runner.prepare_dic(movie_dic)
            start_read_time_loss = time.time()
            continue_answer, dic_answer = Sparse_matrix_runner.read_ratings(ratings, ini, fin)
            read_time_loss += time.time()- start_read_time_loss
            temp = time.time()
            with open(str(pos) + '.json', 'w') as fp:
                json.dump(dic_answer, fp)
            creation_file_t += time.time() - temp
            ratings.close()
            pos += 1
            ini += step
            fin += step
        #now pos is the number of jsons
        #notice that I don't need to read all elements, only the (1) element that I need
    else:
        pos = int(input('pos totales? 1 + el ultimo '))
    print(movie_dic)
    print('\n\n\n')
    print('Resultados:')
    print('Lectura del archivo perdida: ', read_time_loss)
    print('Creacion de archivos temporales: ', creation_file_t / pos)
    search_time = 0
    iterations = 0
    while True:
        print('elemento? ')
        id_movie = int(input())
        temp_search = time.time()
        print(movie_dic[id_movie], ' ==> ', read_json_by_pos(pos, id_movie))
        search_time += time.time() - temp_search
        iterations += 1
        print('\n')
        print('Resultados de busqueda: ', search_time / iterations)

if __name__ == '__main__':
    main()
