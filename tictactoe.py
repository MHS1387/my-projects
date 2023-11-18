import sys
from math import *
import random

class Game():
    def __init__(self):
        self.choice_map = [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],

            [0, 3, 6],
            [1, 4, 7],
            [2, 5, 8],

            [0, 4, 8],
            [6, 4, 2]

        ]
        self.main_shape = '''
        %s|%s|%s
        -+-+-
        %s|%s|%s
        -+-+-
        %s|%s|%s
        '''
        self.list_of_str = [
        ' ', ' ', ' ',
        ' ', ' ', ' ',
        ' ', ' ', ' '
        ]


        self.a = False
        self.dlpw = True
        self.win_oprationstatus = False
        self.list_of_positions = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        self.loop = True
        self.random_choice_of_wo = random.choice([0, 1])



    def start(self):
        self.first_or_second = input('''are you playing first(I bet you can't beat me): yes/no
''')
        if self.first_or_second == 'yes':
            self.player()
        else:
            self.win_opration()
            

    def player(self):
        while self.loop:
            if self.is_won(self.materilize(self.make_3d_list(self.list_of_str))): return
            print('''chose your position
        q|w|e
        -+-+-
        a|s|d
        -+-+-
        z|x|c''')
            pos_of_player = input()
            position = {}
            position['q'] = 0
            position['w'] = 1
            position['e'] = 2
            position['a'] = 3
            position['s'] = 4
            position['d'] = 5
            position['z'] = 6
            position['x'] = 7
            position['c'] = 8
            try:
                self.list_num = position[pos_of_player]
            except:
                continue

            if self.list_of_str[self.list_num] == ' ':
                self.list_of_str[self.list_num] = 'x'
            else:
                print('you cant chose on a chosen position')
                continue
            shape = self.main_shape % tuple(self.list_of_str)
            print(shape)
            if self.first_or_second == 'yes':
                self.dont_let_p_win()
                continue
            else:
                self.win_opration()
                continue

    def test_computer(self):
        list = []
        for index, item in enumerate(self.list_of_str):
            if item == ' ':
                list.append(index)
        random_choice = random.choices(list)
        self.list_of_str[random_choice[0]] = 'o'
        shape = self.main_shape % tuple(self.list_of_str)
        print(shape)        

    def dont_let_p_win(self):
        choice = None

        if self.is_won(self.materilize(self.make_3d_list(self.list_of_str))):
            return
        
        if not self.loop:
            return

        if self.corner(' '):
            choice = 4
        if self.center():
            choice = 0
        if self.bad_situation():
            choice = 2
        if choice == None:
            try:
                x = self.help_of_dont_let(self.materilize(self.make_3d_list(self.list_of_str)), False)[0]
                y = self.help_of_dont_let(self.materilize(self.make_3d_list(self.list_of_str)), False)[1]
                choice = self.choice_map[x][y]
            except:
                self.test_computer()
                return
                    
        self.list_of_str[choice] = 'o'
        shape = self.main_shape % tuple(self.list_of_str)
        print(shape)
        self.is_won(self.materilize(self.make_3d_list(self.list_of_str)))

    def bad_situation(self):
        if self.list_of_str == [
            'o', ' ', ' ',
            ' ', 'x', ' ',
            ' ', ' ', 'x'
            ]:
            return True

        
    def help_of_dont_let(self, in_ar, win_op):
        result = []
        for index, item in enumerate(in_ar):
            if item.count('o') == 2:
                for index2, item2 in enumerate(item):
                    if item2 == ' ':
                        result.append(index)
                        result.append(index2)
                        return result
        if win_op: 
            return
        for index, item in enumerate(in_ar):
            if item.count('x') == 2:
                for index2, item2 in enumerate(item):
                    if item2 == ' ':
                        result.append(index)
                        result.append(index2)
                        return result
        for index, item in enumerate(in_ar):
            if item.count('o') == 1 and item.count(' ') == 2:
                for index2, item2 in enumerate(item):
                    if item2 == ' ':
                        result.append(index)
                        result.append(index2)
                        return result

    def corner(self, dl_or_wo):
        self.list_of_str_fake =[
            ' ', ' '     , ' ',
            ' ', dl_or_wo, ' ',
            ' ', ' '     , ' '
            ]
        num = [0, 2, 6, 8]
        emty_list = []
        for i in num:
            l = list(self.list_of_str_fake)
            l[i] = 'x'
            if l == self.list_of_str:
                emty_list.append(i)
                emty_list.append(True)
                return emty_list
        return False
    def center(self):
        player_calac = [
            ' ', ' ', ' ',
            ' ', 'x', ' ',
            ' ', ' ', ' '
        ]
        if self.list_of_str == player_calac:
            return True

    def win_opration(self):
        choice = None
        self.dlpw = True

        if self.list_of_str[4] == ' ' and self.random_choice_of_wo == 0:
            if self.list_of_str[0] == ' ':
                choice = 0
            elif self.list_of_str[2] == ' ' and self.list_of_str[1] == ' ' and self.list_of_str[5] == ' ':
                choice = 2
            elif self.list_of_str[6] == ' ' and self.list_of_str[3] == ' ' and self.list_of_str[7] == ' ' :
                choice = 6
            else:
                choice = 8
        else:
            self.dlpw = False
        ''' self.list_of_str
        [0], [1], [2],
        [3], [4], [5],
        [6], [7], [8]
        '''
        
        if self.list_of_str[4] == ' ' and self.random_choice_of_wo == 1:
            choice = 4
        corner = self.corner('o')
        if corner:
            map = {0:8, 2:6, 8:0, 6:2}
            choice = map[corner[0]]
            self.dlpw = True

        
        try:
            x = self.help_of_dont_let(self.materilize(self.make_3d_list(self.list_of_str)), self.dlpw)[0]
            y = self.help_of_dont_let(self.materilize(self.make_3d_list(self.list_of_str)), self.dlpw)[1]
            choice = self.choice_map[x][y]
        except: 
            None
        if choice == None:
            self.test_computer()
            return
        if self.is_won(self.materilize(self.make_3d_list(self.list_of_str))): return
        self.list_of_str[choice] = 'o'
        shape = self.main_shape % tuple(self.list_of_str)
        print(shape)
        self.player()
    


    def is_won(self, in_array):
        game_ends = False
        for i in in_array:
            if i[0] == 'o' and i[0] == i[1] == i[2]:
                print('o won')
                game_ends = True
                
            if i[0] == 'x' and i[0] == i[1] == i[2]:
                print('x won')
                game_ends = True
            
        if self.check_tie(self.list_of_str):
            print('nobody won')
            game_ends = True

        if game_ends: 
            self.loop = False
            if input('do you wana play again:y/n\
                                                ') == 'y':
                game = Game()
                game.start()

        else: return False
    
    def check_tie(self, list):
        for i in list:
            if i == ' ':
                return False
        return True 
    def make_3d_list(self, lis):
        x = 0
        first_three = (list(lis[x:x+3]))
        x += 3
        second_three = (list(lis[x:x+3]))
        x += 3
        last_three = (list(lis[x:x+3]))

        make_3d_list = []

        make_3d_list.append(first_three)
        make_3d_list.append(second_three)
        make_3d_list.append(last_three)

        return make_3d_list
    def materilize(self, input):
        return [
            input[0],
            input[1],
            input[2],
            [
                input[0][0],
                input[1][0],
                input[2][0],
            ],
            [
                input[0][1],
                input[1][1],
                input[2][1],
            ],
            [
                input[0][2],
                input[1][2],
                input[2][2],
            ],
            [
                input[0][0],
                input[1][1],
                input[2][2],
            ],
            [
                input[2][0],
                input[1][1],
                input[0][2],
            ],

        ]

game = Game()
game.start()

