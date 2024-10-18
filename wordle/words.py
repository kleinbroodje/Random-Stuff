words_list_La = open("wordle-La.txt", "r")
words_list_La = words_list_La.read()
words_list_La = words_list_La.split()

words_list_Ta = open("wordle-Ta.txt", "r")
words_list_Ta = words_list_Ta.read()
words_list_Ta = words_list_Ta.split()

words_list = words_list_Ta + words_list_La