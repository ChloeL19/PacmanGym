from gym.envs.registration import register

register(
    id='BerkeleyPacman-v0',
    entry_point='gym_pacman.envs:PacmanEnv',
)

register(
    id='BerkeleyPacmanPO-v0',
    entry_point='gym_pacman.envs:PartiallyObservablePacmanEnv',
)
