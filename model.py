import tkinter as tk


class Environment:

    def __init__(self, shape, car_file_path):
        self.shape = shape
        self.cars = self.read_car_file(car_file_path)

    def get_successor_states(self, current_state):
        ret = []
        occupied = self.get_occupied_positions(current_state)
        for i in range(len(current_state)):
            orientation = self.cars[i][0]
            next_plus = list(current_state[i])
            next_plus[orientation] += 1
            if next_plus not in occupied and next_plus[orientation] < self.shape[orientation]:
                state = list(current_state)
                state[i] = next_plus
                ret.append(tuple(state))

            next_min = list(current_state[i])
            next_min[orientation] -= 1 + self.cars[i][3]
            if next_min not in occupied and next_plus[orientation] >= 0:
                state = list(current_state)
                next_min[orientation] += self.cars[i][3]
                state[i] = next_min
                ret.append(tuple(state))

        return ret

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
        with open(file, 'r') as file:
            for line in file:
                car = [int(x) for x in line.split(',')]
                if car[1] + car[3] > self.shape[0] or car[2] > self.shape[1]:
                    raise ValueError("Car is outside of board")
                ret.append(car)
        return ret

    def draw_state(self, state):
        master = tk.Tk()

        w = tk.Canvas(master, width=600, height=600)
        w.pack()

        for i in range(len(state)):
            orientation = self.cars[i][0]
            x = 100 * (state[i][0] + self.cars[i][3] if orientation == 0 else state[i][0] + 1)
            y = 100 * (state[i][1] + self.cars[i][3] if orientation == 1 else state[i][1] + 1)
            w.create_rectangle(state[i][0] * 100, state[i][1] * 100, x, y, fill='red')

        tk.mainloop()