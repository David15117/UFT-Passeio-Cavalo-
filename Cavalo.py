#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import print_function #função print para 3+ funçao print
import copy
import random #numero randonicos
import time #importação time

NUM_GENERATIONS = int(input("Quantidade de Geração?"))#quantidade de geração
POPULATION_SIZE = int(input("Tamanho da População? ")) #numero de individuo da população
TABLE_SIZE = int(input("Tamanho do jogo? ")) #tamanho da tabela


def createTable(rows=TABLE_SIZE, columns=TABLE_SIZE, zeroes=True): #criar as tabelas em forma de vetores
    if zeroes: #se zeroes== true
        return [[0 for i in range(columns)] for j in range(rows)]#valores da geração
    else:
        return [[random.randint(0, 10) for i in range(columns)] for j in range(rows)]#criar tabela pridoridade randomica


class Game():
    def __init__(self):
        self.priority_table = createTable(zeroes=False)#chama a criação da tabela de prioridade
        self.setDefault()

    def setDefault(self):
        self.moves = 0 #armazena quantidade de movimento realizados ate momento
        self.path = [] # o caminho do individuo pelo tabuleiro
        self.table = createTable()# cria um tabuleiro de prioridades
        self.position = (0, 0) #posição iniciar
        self.table[0][0] = 1 # todas posição visitadas no tabuleiro

    def nextMoves(self):# gera os possiveis caminhos
        moves = []
        knight_moves = [(2, -1), (2, 1), (-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2)]
        x, y = self.position
        for (dx, dy) in knight_moves:
            if x + dx < 0 or y + dy < 0:
                continue
            try:
                if self.table[x + dx][y + dy] == 0:
                    moves.append((x + dx, y + dy))
            except IndexError:
                continue

        return moves

    def getBestMove(self, moves):#analisa qual tem maior prioridade no codigo ou seja qual indivui possui
								 #maior vlaor de moveis
        bestValue = float('-inf')
        bestMove = self.position
        for (x, y) in moves:
            if self.priority_table[x][y] > bestValue:
                bestValue = self.priority_table[x][y]
                bestMove = (x, y)

        return bestMove

    def moveTo(self, position):#movimenta a tabela
        x, y = position
        self.path.append(position)
        self.position = position
        self.moves += 1
        self.table[x][y] = self.moves + 1

    def play(self):#e executado até o indíviduo não obter nenhum movimento possível em sua lista de nextMoves,
					#parando de incrementar moves
        self.setDefault()
        while self.nextMoves():
            moves = self.nextMoves()
            bestMove = self.getBestMove(moves)
            self.moveTo(bestMove)

    def mutation(self):
        x = random.randint(0, TABLE_SIZE - 1)
        y = random.randint(0, TABLE_SIZE - 1)
        self.priority_table[x][y] = random.randint(0, 10)
        self.play()

    def printTable(self):
        for i in range(0, TABLE_SIZE):
            for j in range(0, TABLE_SIZE):
                print(repr(self.table[i][j]).rjust(3), end=' ')
            print()

    def printPriorityTable(self):
        for i in range(0, TABLE_SIZE):
            for j in range(0, TABLE_SIZE):
                print(repr(self.priority_table[i][j]).rjust(3), end=' ')
            print()

    def __add__(self, other):#divida tabela em dois  e junta
        g = copy.deepcopy(self)
        for i in range(0, int(TABLE_SIZE / 2)):
            for j in range(0, TABLE_SIZE):
                g.priority_table[i][j] = other.priority_table[i][j]

        g.play()
        return g


class Population():
    def __init__(self):
        self.games = []
        self.bestGames = []
        self.worstGames = []

        for i in range(POPULATION_SIZE):
            g = Game()
            self.games.append(g)

    def play(self):
        for game in self.games:
            game.play()

        self.bestGames.append(self.getBestGame())
        self.worstGames.append(self.getWorstGame())

        print("({0}, {1})".format(self.bestGames[-1].moves, self.worstGames[-1].moves))

    def getBestGame(self): #armazena melhor game
        bestGame = self.games[0]
        for game in self.games:
            if game.moves > bestGame.moves:
                bestGame = game

        return bestGame

    def getWorstGame(self): #armazena pior game
        worstGame = self.games[0]
        for game in self.games:
            if game.moves < worstGame.moves:
                worstGame = game

        return worstGame

    def cross(self):
        pass

    def nextGeneration(self):
        new_generation = []
        for i in range(POPULATION_SIZE):
            i = random.randint(0, POPULATION_SIZE - 1)
            j = random.randint(0, POPULATION_SIZE - 1)

            new_generation.append(self.games[i] + self.games[j])
            new_generation.append(self.games[j] + self.games[i])

            new_generation[-1].mutation()

        self.games = new_generation
        self.games[0] = self.bestGames[-1]


if __name__ == '__main__':
    start = time.time()

    p = Population()

    for i in range(NUM_GENERATIONS):
        p.play()
        p.nextGeneration()

    x = [i for i in range(NUM_GENERATIONS)]
    y = []
    z = []

    for game in p.bestGames:
        y.append(game.moves)

    for game in p.worstGames:
        z.append(game.moves)

    end = time.time()
    print(end - start)
print('\nGerações')
print(x)
print('\nMelhor Jogo')
print(y)
print('\nPior Jogo')
print(z)

bestGame = p.bestGames[-1]
print("\nTabela Prioritária")
bestGame.printPriorityTable()
print("\nTabela Resultante")
bestGame.printTable()