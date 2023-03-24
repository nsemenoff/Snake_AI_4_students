from agent_1 import Agent
from snake_game import Snake
import numpy as np

if __name__ == '__main__':
    game = Snake(10) # Create game object
    status = game.read_status() # read status sample
    agent = Agent(status) # Create agent object
    epochs = 1000

    status_list = []
    control_list = []

    while epochs > 0:
        epochs -= 1
        control = agent.move(status)
        finish = game.move(control)
        status = game.read_status()

        print(np.round(status), control, game.loop)

        control_list.append(control)
        status_list.append(status)

        if finish > 0:
            agent.train(status_list, control_list, finish)
            status_list.clear()
            control_list.clear()
        elif finish<0:
            status_list.clear()
            control_list.clear()

    agent.save_nn()
