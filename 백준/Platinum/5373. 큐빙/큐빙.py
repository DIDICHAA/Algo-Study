class Cube:
    def __init__(self):
        self.up = [['w'] * 3 for _ in range(3)]
        self.down = [['y'] * 3 for _ in range(3)]
        self.front = [['r'] * 3 for _ in range(3)]
        self.back = [['o'] * 3 for _ in range(3)]
        self.left = [['g'] * 3 for _ in range(3)]
        self.right = [['b'] * 3 for _ in range(3)]

    def rotate(self, param):
        plate = param[0]
        if param[1] == '-':
            direction = 0
        else:
            direction = 1
        if plate == 'L':
            tmp = self.front[0][0], self.front[1][0], self.front[2][0]
            if direction:
                self.left = list(map(list, zip(*self.left[::-1])))

                for i in range(3):
                    self.front[i][0] = self.up[i][0]
                for i in range(3):
                    self.up[i][0] = self.back[2-i][0]
                for i in range(3):
                    self.back[i][0] = self.down[i][0]
                for i in range(3):
                    self.down[i][0] = tmp[2-i]
            else:
                self.left = list(map(list, zip(*self.left)))[::-1]

                for i in range(3):
                    self.front[i][0] = self.down[2-i][0]
                for i in range(3):
                    self.down[i][0] = self.back[i][0]
                for i in range(3):
                    self.back[i][0] = self.up[2-i][0]
                for i in range(3):
                    self.up[i][0] = tmp[i]
        elif plate == 'R':
            tmp = self.front[0][2], self.front[1][2], self.front[2][2]
            if direction:
                self.right = list(map(list, zip(*self.right[::-1])))

                for i in range(3):
                    self.front[i][2] = self.down[2-i][2]
                for i in range(3):
                    self.down[i][2] = self.back[i][2]
                for i in range(3):
                    self.back[i][2] = self.up[2-i][2]
                for i in range(3):
                    self.up[i][2] = tmp[i]
            else:
                self.right = list(map(list, zip(*self.right)))[::-1]

                for i in range(3):
                    self.front[i][2] = self.up[i][2]
                for i in range(3):
                    self.up[i][2] = self.back[2-i][2]
                for i in range(3):
                    self.back[i][2] = self.down[i][2]
                for i in range(3):
                    self.down[i][2] = tmp[2-i]
        elif plate == 'U':
            tmp = self.front[0][:]
            if direction:
                self.up = list(map(list, zip(*self.up[::-1])))

                for i in range(3):
                    self.front[0][i] = self.right[0][i]
                for i in range(3):
                    self.right[0][i] = self.back[0][2-i]
                for i in range(3):
                    self.back[0][i] = self.left[0][2-i]
                for i in range(3):
                    self.left[0][i] = tmp[i]
            else:
                self.up = list(map(list, zip(*self.up)))[::-1]

                for i in range(3):
                    self.front[0][i] = self.left[0][i]
                for i in range(3):
                    self.left[0][i] = self.back[0][2-i]
                for i in range(3):
                    self.back[0][i] = self.right[0][2-i]
                for i in range(3):
                    self.right[0][i] = tmp[i]
        elif plate == 'D':
            tmp = self.front[2][:]
            if direction:
                self.down = list(map(list, zip(*self.down)))[::-1]

                for i in range(3):
                    self.front[2][i] = self.left[2][i]
                for i in range(3):
                    self.left[2][i] = self.back[2][2-i]
                for i in range(3):
                    self.back[2][i] = self.right[2][2-i]
                for i in range(3):
                    self.right[2][i] = tmp[i]
            else:
                self.down = list(map(list, zip(*self.down[::-1])))

                for i in range(3):
                    self.front[2][i] = self.right[2][i]
                for i in range(3):
                    self.right[2][i] = self.back[2][2-i]
                for i in range(3):
                    self.back[2][i] = self.left[2][2-i]
                for i in range(3):
                    self.left[2][i] = tmp[i]
        elif plate == 'F':
            tmp = self.up[2][:]
            if direction:
                self.front = list(map(list, zip(*self.front[::-1])))

                for i in range(3):
                    self.up[2][i] = self.left[2-i][2]
                for i in range(3):
                    self.left[i][2] = self.down[2][i]
                for i in range(3):
                    self.down[2][i] = self.right[2-i][0]
                for i in range(3):
                    self.right[i][0] = tmp[i]
            else:
                self.front = list(map(list, zip(*self.front)))[::-1]

                for i in range(3):
                    self.up[2][i] = self.right[i][0]
                for i in range(3):
                    self.right[i][0] = self.down[2][2-i]
                for i in range(3):
                    self.down[2][i] = self.left[i][2]
                for i in range(3):
                    self.left[i][2] = tmp[2-i]
        elif plate == 'B':
            tmp = self.up[0][:]
            if direction:
                self.back = list(map(list, zip(*self.back)))[::-1]

                for i in range(3):
                    self.up[0][i] = self.right[i][2]
                for i in range(3):
                    self.right[i][2] = self.down[0][2-i]
                for i in range(3):
                    self.down[0][i] = self.left[i][0]
                for i in range(3):
                    self.left[i][0] = tmp[2-i]
            else:
                self.back = list(map(list, zip(*self.back[::-1])))

                for i in range(3):
                    self.up[0][i] = self.left[2-i][0]
                for i in range(3):
                    self.left[i][0] = self.down[0][i]
                for i in range(3):
                    self.down[0][i] = self.right[2-i][2]
                for i in range(3):
                    self.right[i][2] = tmp[i]


T = int(input())
for case in range(1, T + 1):
    cube = Cube()
    N = int(input())
    commands = list(input().split())
    for command in commands:
        cube.rotate(command)
    for row in cube.up:
        print(*row, sep='')