import time
class Lane:
    def __init__(self,lane_size,speed,waiting_time,state=0):
        self.lane_size = lane_size
        self.speed = speed
        self.waiting_time = waiting_time
        self.state = state

    def add_custmor(self,value):
        self.lane_size = self.lane_size + value

    def remove_custmor(self,value):
        self.lane_size = self.lane_size - value
        
    def display_lane(self):
        if self.state == 0:
            return "Closed"
        elif self.state == 1:
            return f"* " * self.lane_size

    def change_lane_status(self,value):
            self.state = value



class regualr_lane(Lane):
    def __init__(self,lane_size,speed,waiting_time,state=0):
        super().__init__(lane_size,speed,waiting_time,state)
        self.lane_type = "REG"
        self.till = 1
    
class self_service_till(Lane):
    def __init__(self,lane_size,speed,waiting_time,state=0):
        super().__init__(lane_size,speed,waiting_time,state)
        self.till = 8
        self.lane_type = "SELF"

lane1 = regualr_lane(lane_size=0,speed=0,waiting_time=0,state=0)
lane2 = regualr_lane(lane_size=10,speed=0,waiting_time=0,state=1)
lane3 = regualr_lane(lane_size=0,speed=0,waiting_time=0,state=0)
lane4 = regualr_lane(lane_size=0,speed=0,waiting_time=0,state=0)

for i in range(10):
    lane1 = regualr_lane(lane_size=i,speed=0,waiting_time=0,state=1)
    lane2 = regualr_lane(lane_size=i,speed=0,waiting_time=0,state=1)
    print(f""" 
              L1(REG)-> {lane1.display_lane()}
              L2(REG)-> {lane2.display_lane()}
              L3(REG)-> {lane3.display_lane()}
              L4(REG)-> {lane4.display_lane()}
          """,end='\r')
    print("\033[H\033[J", end='')
    time.sleep(0.5)
