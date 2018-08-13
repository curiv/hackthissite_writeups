# -*- coding: utf-8 -*-
import re

def unn():
    global sol
    sol = list()
    file = open('1.txt','r')       # открываем файл только для чтения
    for line in file:
        result = re.findall('\S+',line)
        if result.__len__() > 0:
            sol.append(result)
    print(sol,"\n")
    file.close()

def finder(word):

    def sortByAlphabet(inputStr):
        return inputStr[0]

    file = open('wordlist.txt','r')

    word_len = len(word)
    pattern = '['+word+']{'+str(word_len)+'}'

    check = []
    for i in word:
        check.append(i)
    sol = []
    k = ''
    n = 0
    for line in file:
        result = re.findall(pattern,line) ## filetype - list '([hello]{9})' - right pattern
        if (result.__sizeof__() > 0) and (result.__len__() > 0):
            for i in result:
                for j in i:
                    k = k + j
                sol.append(k)
                k = ''
    word_s = sorted(list(word))
    # print("word_s",word_s)
    for i in range(0,sol.__len__()):
        sol_s = sorted(list(sol[i]))
        if sol_s == word_s:
            print(sol[i],end=",")

unn()
for i in sol:
    finder(i.pop())
