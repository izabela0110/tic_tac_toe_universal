# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 21:17:03 2024

@author: izabe
"""

from colorama import init as colorama_init
from colorama import Fore
from colorama import Style
import sys

colorama_init()

def get_coordinates (user_input):
    user_input_a = int(user_input.split(',')[0])
    user_input_b = int(user_input.split(',')[1])
    user_symbol = user_input.split(',')[2]
    return (user_input_a,user_input_b,user_symbol)

def check_if_avail(board, a, b, c):
    if board[a-1][b-1]==' ':
        board[a-1][b-1]=c
    else:
        print(f'{Fore.RED}WARNING!!!Field is already taken{Style.RESET_ALL}')
    return (board)

def draw_board2 (size):
    print (' ---'*size)
    for x in range(size):
        for y in range(size):
            print (f'| {board[x][y]} ',end='')
        print('|\n'+' ---'*size)
        
def horizontal_check (board, size):
    for i in range (size):
        result_list = []
        for j in range (size):
            result_list.append(board[i][j])
        result_set = set(result_list)
        if result_set=={'x'}:
            return ('Player x has won! Congratulations')
        elif result_set=={'o'}:
            return ('Player o has won! Congratulations')
        
def vertical_check (board, size):            
    for i in range (size):
        result_list = []
        for j in range(size):
            result_list.append(board[j][i])
        result_set = set(result_list)
        if result_set=={'x'}:
            return ('Player x has won! Congratulations')
        elif result_set=={'o'}:
            return ('Player o has won! Congratulations')
        
def diagonal_check (board, size):
    result_list = []
    result_list_2 = []
    for i in range(size):
        result_list.append(board[i][i])
        result_list_2.append(board[i][size-1-i])
    result_set = set(result_list)
    result2_set = set(result_list_2)
    if result_set=={'x'} or result2_set=={'x'}:
        return ('Player x has won! Congratulations')
    elif result_set=={'o'} or result2_set=={'o'}:
        return ('Player o has won! Congratulations')
    
def is_there_a_winner (board, size):
    horizonal_check_result = horizontal_check(board,size)
    vertical_check_result = vertical_check(board, size)
    diagonal_check_result = diagonal_check(board, size)
    if horizonal_check_result!=None:
        print(horizonal_check_result)
        return(horizonal_check_result)
    elif vertical_check_result!=None:
        print(vertical_check_result)
        return(vertical_check_result)
    elif diagonal_check_result!=None:
        print(diagonal_check_result)
        return(diagonal_check_result)
    


if __name__=="__main__":
    print('Welcome to the Tic Tac Toe game!')
    size = 'wrong'
    size = input('Please give the size of the board (enter a number):\n')

    while not size.isdigit():
        size = input('You have not entered a number, please try again:\n')
    size = int(size)
    
    board =  [[' ' for i in range (size)] for i in range (size)]
    
    while True:
        user_input_a=0
        user_input_b=0
        user_symbol=0
        while not 1<=user_input_a<=size or not 1<=user_input_b<=size or user_symbol not in ['x','o','X','O']:
            user_input = input("""Please give your move in the format: a,b,c, where:\
                       \na - row number and 1<=a<=board size,\
                           \nb - column number and 1<=b<=board size,\
                               \nc - x or o\
                                   \nor press q to end the game:\n""")
            if user_input=='q':
                print('Thanks for the game')
                sys.exit()                            
            user_input_a, user_input_b, user_symbol = get_coordinates(user_input)

        board = check_if_avail(board,user_input_a,user_input_b,user_symbol)
        draw_board2(size)
        result = is_there_a_winner(board, size)
        if any(' ' in sublist for sublist in board)==False:
            print('No fields available. Noone has won')
            break
        if result =='Player o has won! Congratulations' or result=='Player x has won! Congratulations':
            break
        
    