class Bush:
    def __init__(self,
                 graph_idx,
                 fire_status,
                 protect_status):
        self.graph_idx = graph_idx
        self.on_fire = fire_status
        self.protect_status = protect_status