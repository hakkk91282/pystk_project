import numpy as np
import random

from utils.track_utils import compute_curvature, compute_slope
from agents.kart_agent import KartAgent

class Agent7(KartAgent):
    def __init__(self, env, path_lookahead=3):
        super().__init__(env)
        self.path_lookahead = path_lookahead
        self.agent_positions = []
        self.obs = None
        self.isEnd = False
        self.count=0
        self.times_block=0
        self.name = "HAKIM HADDOUCHI" # replace with your chosen name



    def reset(self):
        self.obs, _ = self.env.reset()
        self.agent_positions = []

    def endOfTrack(self):
        return self.isEnd

    def choose_action(self, obs):
        brake=False
        acceleration=0.5
        target = obs["paths_end"][0] #return a vector [x,y,z]
        x = target[0] #Extracting the x


        speed = obs["velocity"][2]
        if (speed >0 and obs["distance_down_track"] > 5.0): #if the kart goes forwad we increase the counter
            self.times_block=self.times_block+1

        if self.times_block>=200: #if we reach the 200 steps we go back 
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
