import tkinter as tk


class Environment:

    def __init__(self, shape, car_file_path):
        self.shape = shape
        self.cars = self.read_car_file(car_file_path)

        self.tk_master = None
        self.tk_canvas = None

    def get_successor_states(self, current_state):
        ret = []
        occupied = self.get_occupied_positions(current_state)
        #print("--------------------------------------------")
        #print("current state: {}".format(current_state))
        #print("occupied tiles: {}".format(occupied))

        for i in range(len(current_state)):
            orientation = self.cars[i][0]
            next_plus = list(current_state[i])
            next_plus[orientation] += 1 + self.cars[i][3] -1
            if next_plus not in occupied and next_plus[orientation] < self.shape[orientation]:
                state = list(current_state)
                next_plus[orientation] -= self.cars[i][3] -1
                state[i] = tuple(next_plus)
                ret.append(tuple(state))

            next_min = list(current_state[i])
            next_min[orientation] -= 1

            if next_min not in occupied and next_min[orientation] >= 0:
                state = list(current_state)
                state[i] = tuple(next_min)
                ret.append(tuple(state))
        #[print("\t", x) for x in ret]
        return ret

    def h(self, state):
        return self.shape[0] - state[0][0] + self.cars[0][3]

    def is_terminal_state(self, state):
        if state[0][0] + self.cars[0][3] == self.shape[0]-1:
            return True
        return False


    def get_occupied_positions(self, state):
        ret = []
        for car in range(len(state)):
            for pos in self.get_car_position(car, state[car]):
                ret.append(pos)

        return ret

    def get_car_position(self, car_num, car_pos):
        ret = []
        for i in range(self.cars[car_num][3]):
            orientation = self.cars[car_num][0]
            ret.append([car_pos[0] + i if orientation == 0 else car_pos[0],
                        car_pos[1] + i if orientation == 1 else car_pos[1]])
        return ret

    def read_car_file(self, file):
        ret = []
        with open(file, 'r') as f:
            for line in f:
                car = [int(x) for x in line.split(',')]
                if car[1] + car[3] > self.shape[0] or car[2] > self.shape[1]:
                    raise ValueError("Car is outside of board!")
                ret.append(car)
        return ret

    def draw_state(self, state):

        if self.tk_master is None:
            self.tk_master = tk.Tk()
            self.tk_canvas = tk.Canvas(self.tk_master, width=600, height=600)
            self.tk_canvas.pack()

        self.tk_canvas.create_rectangle(-1, -1, self.tk_canvas.winfo_width()+1,
                                        self.tk_canvas.winfo_height()+1, fill='white')
        for i in range(len(state)):
            orientation = self.cars[i][0]
            x = 100 * (state[i][0] + self.cars[i][3] if orientation == 0 else state[i][0] + 1)
            y = 100 * (state[i][1] + self.cars[i][3] if orientation == 1 else state[i][1] + 1)
            self.tk_canvas.create_rectangle(state[i][0] * 100, state[i][1] * 100, x, y, fill='red')

        self.tk_master.update()
