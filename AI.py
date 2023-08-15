start_state = '+++++++++'
turn = 1

def check_game_ended(s):
    checks = [s[:3],s[3:6],s[6:]] + [s[::3],s[1::3],s[2::3]] + [s[::4],s[6::-2][:3]]   
    if 'XXX' in checks:
        return 1
    elif 'OOO' in checks:
        return 2
    elif not s.count('+'):
        return 3 # draw
    return 0

def get_children(s,symb):
    end_state = check_game_ended(s)
    if end_state:
        return []
    else:
        children = []
        for i in range(len(s)):
            if s[i] == '+':
                children.append(s[:i]+symb+s[i+1:])
        return children

children_data = {}
parent_data = {}
state_res = {}
moves_to_end = {}
best_move = {}

# dfs for first time
stack = [(start_state,turn)]
while stack:
    state,turn = stack.pop()
    game_res = check_game_ended(state)
    if game_res:
        if game_res == 1:
            state_res[state] = 1
            moves_to_end[state] = 0
        elif game_res == 2:
            state_res[state] = -1
            moves_to_end[state] = 0
        elif game_res == 3:
            state_res[state] = 0
            moves_to_end[state] = 0
    else:
        children = get_children(state,'O' if turn-1 else 'X')
        for x in children:
            stack.append((x,3-turn))
            children_data[state] = children_data.get(state,set())
            children_data[state].add(x)
            parent_data[x] = parent_data.get(x,[])+[state] 

# X X 
#   O O
# O X 

stack = [start_state]
seen_once = {}

while stack:
    state = stack[-1]
    turn = 2-state.count('+')%2
    try:
        _ = state_res[state]
        stack.pop()
    except:
        seen_once[state] = seen_once.get(state,False)
        if not seen_once[state]:
            stack += children_data[state]
        else:
            wins,draws,loses=[],[],[]
            for x in children_data[state]:
                if 3-2*turn == state_res[x]:
                    wins.append((moves_to_end[x],x))
                elif state_res[x]==0:
                    draws.append((moves_to_end[x],x))
                else:
                    loses.append((moves_to_end[x],x))
            if wins:
                wins.sort()
                moves_to_end[state] = wins[0][0]+1
                state_res[state] = 3-2*turn
                best_move[state] = wins[0][1]
            elif draws:
                draws.sort()
                moves_to_end[state] = draws[0][0]+1
                state_res[state] = 0
                best_move[state] = draws[0][1]
            else:
                loses.sort()
                state_res[state] = 2*turn-3
                moves_to_end[state] = loses[0][0]+1
                best_move[state] = loses[0][1]
            stack.pop()
        seen_once[state] = True

#print(len(best_move))