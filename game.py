import math

class Game:
    def __init__(self):
        self.board = [
            [1, 1, 1],
         [1, 1, 1, 1, 1],
      [1, 1, 1, 1, 1, 1, 1],
      [1, 1, 1, 0, 1, 1, 1],
      [1, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1],
            [1, 1, 1]
            ]
        
    def move(self, x, y, direction):
        if direction == 1:
            if x + 2 < len(self.board[y]):
                if self.board[y][x] == 1 and self.board[y][x + 1] == 1 and self.board[y][x + 2] == 0:
                    self.board[y][x + 1] = 0
                    self.board[y][x] = 0
                    self.board[y][x + 2] = 1
                else:
                    return float("-inf")
            else:
                return float("-inf")
        elif direction == 2:
            if x - 2 >= 0 and x < len(self.board[y]):
                if self.board[y][x] == 1 and self.board[y][x - 1] == 1 and self.board[y][x - 2] == 0:
                    self.board[y][x - 1] = 0
                    self.board[y][x] = 0
                    self.board[y][x - 2] = 1
                else:
                    return float("-inf")
            else:
                return float("-inf")
        elif direction == 3:
            if y + 2 < 7:
                if x < len(self.board[y + 2]) and x < len(self.board[]):
                    if self.board[y][x] == 1 and self.board[y + 1][x] == 1 and self.board[y + 2][x] == 0:
                        self.board[y - 1][x] = 0
                        self.board[y][x] = 0
                        self.board[y - 2][x] = 1
                    else:
                        return float("-inf")
                else:
                    return float("-inf")
            else:
                return float("-inf")
        elif direction == 4:
            if y - 2 >= 0:
                if x < len(self.board[y - 2]):
                    if self.board[y][x] == 1 and self.board[y - 1][x] == 1 and self.board[y - 2][x] == 0:
                        self.board[y - 1][x] = 0
                        self.board[y][x] = 0
                        self.board[y - 2][x] = 1
                    else:
                        return float("-inf")
                else:
                    return float("-inf")
            else:
                return float("-inf")
        else:
            return float("-inf")

        count_1 = 0
        for row in self.board:
            for col in row:
                if col == 1:
                    count_1 += 1

        if count_1 == 1:
            return float("inf")

        total_score = 0
        locations = []

        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                locations.append([i, j])

        for loc in locations:
            for loc2 in locations:
                if loc != loc2:
                    total_score += -(math.sqrt((loc2[1] - loc[1]) ** 2 + (loc2[0] - loc[0]) ** 2))

        return total_score

    def get_score(self):
        count_1 = 0
        for row in self.board:
            for col in row:
                if col == 1:
                    count_1 += 1

        if count_1 == 1:
            return float("inf")

        total_score = 0
        locations = []

        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                locations.append([i, j])

        for loc in locations:
            for loc2 in locations:
                if loc != loc2:
                    total_score += -(math.sqrt((loc2[1] - loc[1]) ** 2 + (loc2[0] - loc[0]) ** 2))

        return total_score

    def copy(self):
        g = Game()
        g.board = self.board

        return g