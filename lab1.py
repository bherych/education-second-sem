class Matrix:

    def __init__(self, rows, cols, direction):
        self.rows = rows
        self.cols = cols
        self.matrix = [[0] * cols for _ in range(rows)]
        self.num = 1
        self.step = 0
        self.x, self.y = 0, 0 
        self.direction = direction

    def mark(self):
        self.step += 1
        print(self.step, self.x, self.y)
        self.matrix[self.y][self.x] = self.step

        return

    def left(self):
        if self.x == 0:
            return
        
        self.x -= 1
        self.mark()

        return

    def right(self):
        if self.x == self.cols - 1:
            return
        
        self.x += 1
        self.mark()

        return


    def down(self):
        if self.y == self.rows - 1:
            return
        
        self.y += 1
        self.mark()

        return

    def up(self):
        if self.y == 0:
            return
        
        self.y -= 1
        self.mark()

        return


    def up_right(self):
        while self.x <= self.cols and self.y > 0:
            self.x += 1
            self.y -= 1
            self.mark()

        return

    def up_left(self):
        while self.x > 0 and self.y > 0:
            self.x -= 1
            self.y -= 1
            self.mark()
            

        return


    def down_left(self):
        while self.x > 0 and self.y < self.rows - 1:
            self.x -= 1
            self.y += 1
            self.mark()
        
        return

    def down_right(self):

        while self.x < self.cols - 1 and self.y < self.rows - 1:
            self.x += 1
            self.y += 1
            self.mark()

        return
    

    def process(self):

        if self.direction == "left":
            end_value = (0, self.rows - 1)
            self.x = self.cols - 1
        else:
            end_value = (self.cols - 1, self.rows - 1)

        self.mark()

        while (self.x, self.y) != end_value: # TODO:
                
            if self.direction == "right":
                self.right()

                if self.y == 0:
                    self.direction = "down_left"
                else:
                    self.direction = "up_right"

                continue

            if self.direction == "up_right":
                self.up_right()

                if self.x == self.cols - 1:
                    self.direction = "down"
                else:
                    self.direction = "right"

                continue

            if self.direction == "down":
                self.down()

                if self.x == 0:
                    self.direction = "up_right"
                else:
                    self.direction = "down_left"

                continue
            
            if self.direction == "down_left":
                self.down_left()

                if self.y == self.rows -1:
                    self.direction = "right"
                else:
                    self.direction = "down"

                continue

            if self.direction == "left":
                self.left()

                if self.y == 0:
                    self.direction = "down_right"
                else:
                    self.direction = "up_left"
                
                continue

            if self.direction == "down_right":
                self.down_right()

                if self.y == self.rows - 1:
                    self.direction = "left"
                else: 
                    self.direction = "down_reverse"

                continue
            
            if self.direction == "up_left":
                self.up_left()

                if self.x == 0:
                    self.direction = "down_reverse"
                else:
                    self.direction = "left"

                continue

            if self.direction == "down_reverse":
                self.down()

                if self.x == 0:
                    self.direction = "down_right"
                else:
                    self.direction = "up_left"

                continue



        result = [el for sublist in self.matrix for el in sublist]
        return result

    
