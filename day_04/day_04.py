def match(board, nums):
    for i in range(5):
        # rows
        if all(board[i][j] in nums for j in range(5)):
            return True
        # columns
        if all(board[j][i] in nums for j in range(5)):
            return True
    return False


def count_board(board, sequence):
    total = 0
    for i in range(5):
        for j in range(5):
            if (board[i][j] not in sequence):
                total += board[i][j]
    return total

lines = []

with open('day_04/data.txt') as f:
# with open('day_04/unit_test.txt') as f:
    for l in f:
        lines.append(l.strip())

numbers = [int(x) for x in lines[0].split(',')]        

boards = []
for i in range(2, len(lines), 6):
    board = []
    for j in range(5):
        board.append([int(x) for x in lines[i+j].split(' ') if x != ''])  # removes that weird non-space
    boards.append(board)


for i in range(5, len(numbers)):
    for board in boards:
        if match(board, numbers[:i]):
            winning_board = board
            seq = numbers[:i]
            break
    else:
        continue
    break

total = count_board(winning_board, seq)
print(f"Day 4a: {total * seq[-1]}")

winner_idx = []
for i in range(5, len(numbers)):
    for idx, board in enumerate(boards):
        if match(board, numbers[:i]) and not (idx in winner_idx):
            winner_idx.append(idx)
            seq = numbers[:i]
            total = count_board(board, seq)

            # print out all of them and report the last one
            print(f"Day 4b: {total * seq[-1]}")