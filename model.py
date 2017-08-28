import tkinter as tk


class Environment:
    def __init__(self, shape, car_file_path):
        """
        :param (int, int) shape: The shape of the board
        :param str car_file_path: Path to game file

        :var (int, int, int, int) self.cars: Car information and init state
        :var tk_*: tkinter variables
        """
        self.shape = shape
        self.cars = self.read_car_file(car_file_path)

        # Canvas stuff
        self.tk_master = None
        self.tk_canvas = None

    def get_successor_states(self, current_state):
        """
        1. Generate list of all occupied tiles.
        2. Iterate over all cars.
        3. Checks if move forwards in orientation direction is possible
        4. Checks if move backwards in orientation direction is possible
        :param ((int, int)) current_state:
        :return [((int, int))]: a list of all proceeding states of current_state
        """
        ret = []
        occupied = self.get_occupied_positions(current_state)  # 1
        for i in range(len(current_state)):  # 2
            orientation = self.cars[i][0]
            next_plus = list(current_state[i])
            next_plus[orientation] += 1 + self.cars[i][3] - 1
            if next_plus not in occupied and next_plus[orientation] < self.shape[orientation]:  # 3
                state = list(current_state)
                next_plus[orientation] -= self.cars[i][3] - 1
                state[i] = tuple(next_plus)
                ret.append(tuple(state))

            next_min = list(current_state[i])
            next_min[orientation] -= 1
            if next_min not in occupied and next_min[orientation] >= 0:  # 4
                state = list(current_state)
                state[i] = tuple(next_min)
                ret.append(tuple(state))
        return ret

    @staticmethod
    def h(state):
        """
        The heuristic function:
        Calculates how "good" the state is.
        Decreases by the power of two as car0 approaches termination state
        :param ((int, int),) state:
        :return int:
        """
        ret = 2**(6-state[0][0])
        return ret

    def is_terminal_state(self, state):
        """
        Checks if the given state is a termination state
        :param ((int, int),) state:
        :return boolean:
        """
        if state[0][0] + self.cars[0][3]-1 == self.shape[0]-1:
            return True
        return False


    def get_occupied_positions(self, state):
        """
        Generates a list of all occupied tiles from given a given state
        """
        ret = []
        for car in range(len(state)):
            for pos in self.get_car_position(car, state[car]):
                ret.append(pos)

        return ret

    def get_car_position(self, car_num, car_pos):
        """
        Returns tiles occupied by a given car
        """
        ret = []
        for i in range(self.cars[car_num][3]):
            orientation = self.cars[car_num][0]
            ret.append([car_pos[0] + i if orientation == 0 else car_pos[0],
                        car_pos[1] + i if orientation == 1 else car_pos[1]])
        return ret

    def read_car_file(self, file):
        """
        Reads a game state file and checks if all cars are within the board, but not colliding cars. Life is too short
        """
        ret = []
        with open(file, 'r') as f:
            for line in f:
                car = [int(x) for x in line.split(',')]
                if car[1] + (car[3]-1 if car[0] == 0 else 0) > self.shape[0] \
                        or car[2] + (car[3]-1 if car[0] == 1 else 0) > self.shape[1]:
                    raise ValueError("Car is outside of board!")
                ret.append(car)
        return ret


    def draw_state(self, state):
        """
        Initializes the canvas and makes a rather ugly visual representation of the state.
        """
        colors = ['gold', 'coral', 'cyan', 'red', 'green', 'green yellow', 'sandy brown', 'light slate blue',
                  'peach puff', 'deep sky blue', 'orange', 'slate gray', 'indian red']
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
            self.tk_canvas.create_rectangle(state[i][0] * 100, state[i][1] * 100, x, y, fill=colors[i])
            self.tk_canvas.create_text(x-50 * (self.cars[i][3] if orientation == 0 else 1),
                                       y-50 * (self.cars[i][3] if orientation == 1 else 1), text=str(i+1))

        self.tk_master.update()
