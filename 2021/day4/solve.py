data = open("in").readlines()

nums=data[0].strip().split(',')
boards = ''.join(data[2:]).split('\n\n')
boards_wins = []

for board in boards:
    rows = [x.split() for x in board.split('\n')]
    cols = [[x[i] for x in rows if len(x) > 1] for i in range(len(rows[0]))]
    wins = rows + cols
    boards_wins.append(wins)

fastest_win = 999999
winning_board = -1
winning_nums = []


for i, board in enumerate(boards_wins):
    for w in board:
        sorted_w = sorted(w, key=lambda x:nums.index(x))
        if len(sorted_w) > 1 and all([x for x in sorted_w if x in nums]):
            last_num = sorted_w[-1]
            if nums.index(last_num) < fastest_win:
                fastest_win = nums.index(last_num)
                winning_board = i
                winning_nums = sorted_w

fastest_win_by_boards = []
fastest_nums_by_boards = []
for i, board in enumerate(boards_wins):
    fastest_win = 99999
    fastest_nums = []
    for w in board:
        sorted_w = sorted(w, key=lambda x:nums.index(x))
        if len(sorted_w) > 1 and all([x for x in sorted_w if x in nums]):
            steps = nums.index(sorted_w[-1])
            if steps < fastest_win:
                fastest_win = steps
                fastest_nums = sorted_w
    fastest_win_by_boards.append(fastest_win)
    fastest_nums_by_boards.append(fastest_nums)


slowest_board = boards[fastest_win_by_boards.index(max(fastest_win_by_boards))]
slowest_num = fastest_nums_by_boards[fastest_win_by_boards.index(max(fastest_win_by_boards))]

last_num_called = winning_nums[-1]
tomark = nums[:nums.index(last_num_called)+1]
tosum = [int(y) for x in boards[winning_board].strip().split('\n') for y in x.split() if y not in tomark]
s = sum(tosum)
sol = s*int(winning_nums[-1])
print(f"SOLUTION PT1: {sol}")

slowest_win_by = max(fastest_win_by_boards)
tomark = nums[:slowest_win_by+1]
tosum = [int(y) for x in slowest_board.strip().split('\n') for y in x.split() if y not in tomark]
s = sum(tosum)
sol = s*int(slowest_num[-1])
print(f"SOLUTION PT2: {sol}")

