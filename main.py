from model import *



env = Environment((6, 6), 'envs/easy-3.txt')
s_states = env.get_successor_states([(car[1], car[2]) for car in env.cars])


env.draw_state(s_states[0])
