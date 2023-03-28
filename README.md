# Snake_AI_4_students
Very compact and short AI snake game

using files:

*snake_game.py* - class for step-by-step game play

*agent_1.py* - class for DQN learning neural network

*main.py* - main script

# main idea

> while True: \
>  control = agent.move(status) # think about next move \
>  status, finish = game.move(control) # look at the game, make one move and read status  \

i.e. we make one step control by agent (neural network), then pass this control to the snake game and read status for the next step control by agent

# training DQN

>        control_list.append(control)
>        status_list.append(status)
>
>        if finish > 0:
>            agent.train(status_list, control_list, finish)
>            status_list.clear()
>            control_list.clear()

we collect all the status data from the game, all the control data from agent, and then pass it to the training function using information is it good or bad for the game. So, if the snake has eaten food it's good, so, we amplify control for that route. If snake was killed it's bad, so, we seduct this route.

>     if finish==1:
>         for i in range(len(control_list)):
>            q = np.argmax(control_list[i])
>            control_list[i][0][q] -= 1/len(control_list[0][0])*i;
>     elif finish==2: # apple eating
>         for i in range(len(control_list)):
>             q = np.argmax(control_list[i])
>             control_list[i][0][q] += 10.0 / status_list[i][0][6];

>        # train
>        x = np.array(status_list, dtype='float32')
>        y = np.array(control_list, dtype='float32')
>        self.model.train_on_batch(x, y)

So, train_on_batch works with the default parameters

