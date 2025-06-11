#tic-tac-toe game
#declare hash map
#print the board
#ask for turns to play
#fill the map in board
#print winner
theboard={'top-L':' ','top-M':' ','top-R':' ',
       'mid-L':' ','mid-M':' ','mid-R':' ',
       'bot-L':' ','bot-M':' ','bot-R':' '}
def winner(board,player):
       w=[['top-L','top-M','top-R'],
          ['top-M','mid-M','mid-R'],
          ['bot-L','bot-M','bot-R'],
          ['top-L','top-M','bot-L'],
          ['top-M','mid-M','bot-M'],
          ['top-R','mid-R','bot-R'],
          ['top-L','mid-M','bot-R'],
          ['top-R','mid-M','bot-R']
          ]
       for com in w:
              if all(board[pos]==player for pos in com):
                     return True
              return False
def priboard(board):
       print(board['top-L']+'|'+board['top-M']+'|'+board['top-R'])
       print('-+-+-')
       print(board['mid-L']+'|'+board['mid-M']+'|'+board['mid-R'])
       print('-+-+-')
       print(board['bot-L']+'|'+board['bot-M']+'|'+board['bot-R'])
turn='X'
for i in range(9):
       priboard(theboard)
       print('Turn for ' + turn + ' move to make:')
       move=input('enter your move:')
       theboard[move] = turn
       if turn == 'X':
              turn = 'O'
       else:
              turn = 'X'
priboard(theboard)