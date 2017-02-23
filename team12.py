team_name = 'ArmyOfTwo'
strategy_name = 'Betray Only'
strategy_description = 'Only return B'
    
def move(my_history, their_history, my_score, their_score):
 
    return 'bccb'

    
def tit_tat(my_history, their_history, my_score, their_score, result):
  
    real_result = move(my_history, their_history, my_score, their_score)
    if real_result == result:
        return True
    else:
        print("move(" +
            ", ".join(["'"+my_history+"'", "'"+their_history+"'",
                       str(my_score), str(their_score)])+
            ") returned " + "'" + real_result + "'" +
            " and should have returned '" + result + "'")
        return False

if __name__ == '__main__':
     
    if tit_tat(my_history='b',
              their_history='c', 
              my_score=100,
              their_score=-500,
              result='bccb'):
         print 'Move working.'
    tit_tat(my_history='bc',
              their_history='cc', 
              my_score=100, 
              their_score=-500,
              result='bccb')             
    tit_tat(my_history='bbb',
              their_history='cbc',
              my_score=200,
              their_score=-1000,
              result='bccb')
