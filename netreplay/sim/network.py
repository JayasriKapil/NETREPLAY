import random

class NetworkState:
    def __init__(self, seed=42):
        self.rng = random.Random(seed)
        self.time = 0.0
        # Default state
        self.link = "wifi"
        self.rtt_ms = 40.0
        self.loss_prob = 0.01
        
    def step(self, dt=0.1):
        self.time += dt
        
    def get_state(self):
        return {
            "time": self.time,
            "link": self.link,
            "rtt_ms": self.rtt_ms,
            "loss_prob": self.loss_prob
        }