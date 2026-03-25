from pathlib import Path
import numpy as np
import random
from utils.track_utils import compute_curvature, compute_slope
from omegaconf import OmegaConf

from agents.kart_agent import KartAgent
from agents.team1.agent_center import AgentCenter
from agents.team1.agent_speed import AgentSpeed
from agents.team1.agent_obstacles import AgentObstacles
from agents.team1.agent_rescue import AgentRescue
from agents.team1.agent_items import AgentItems
from agents.team1.agent_drift import AgentDrift

class Agent1(KartAgent):
    def __init__(self, env, path_lookahead=3):
        super().__init__(env)
        self.path_lookahead = path_lookahead
        self.agent_positions = []
        self.obs = None
        self.isEnd = False
        self.times_block=0
        self.name = "HAKIM HADDOUCHI"

        

    def reset(self):
        self.obs, _ = self.env.reset()
        self.agent_positions = []

    def endOfTrack(self):
        return self.isEnd

    def choose_action(self, obs):
        if(self.times_block<40):  # on laise le random nous mettre en position de marche arriere pendant un court instant
            self.times_block=self.times_block+1
            acceleration = random.random()
            steering = random.random()
            action = {
                "acceleration": acceleration,
                "steer": steering,
                "brake": False, # bool(random.getrandbits(1)),
                "drift": bool(random.getrandbits(1)),
                "nitro": bool(random.getrandbits(1)),
                "rescue":bool(random.getrandbits(1)),
                "fire": bool(random.getrandbits(1)),
                }

            return action
        else:   #si on a finit de nous en position de marche arriere on met jsuqua la fin de la course une marche arriere et on se dirige vers le point target
            target = obs["paths_end"][3] #return a vector [x,y,z]
            x = target[0] #Extracting the x
            brake=True
            acceleration=0.0


            action = {
                "acceleration": acceleration,
                "steer": x,
                "brake": brake,
                "drift": False,
                "nitro": False,
                "rescue": False,
                "fire": False,
            }
            return action













