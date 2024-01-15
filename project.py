import time
import random

class Lane:
    def __init__(self,speed,waiting_time,state=0):
        self.lane_ = []
        self.speed = speed
        self.waiting_time = waiting_time
        self.state = state

    def add_custmor(self,value):
        self.lane_.append(value)
        print(len(self.lane_))


    def remove_custmor(self,value):
        self.lane_.remove(value)
        
    def display_lane(self):
        if self.state == 0:
            return "Closed"
        elif self.state == 1:
            return f"*" * len(self.lane_)
        

    


class regualr_lane(Lane):
    def __init__(self,speed,waiting_time,state=0):
        super().__init__(speed,waiting_time,state)
        self.lane_type = "REG"
        self.lane_capacity = 5
        self.till = 1
    def change_lane_status(self):
        if len(self.lane_) == 0:
                self.state = "Closed"
        elif len(self.lane_) < self.lane_capacity:
                self.state = "Open"
        else:
             self.state = "Full"
    
class self_service_till(Lane):
    def __init__(self,speed,waiting_time,state=0):
        super().__init__(speed,waiting_time,state)
        self.till = 8
        self.lane_capacity = 15
        self.lane_type = "SELF"
    def change_lane_status(self):
        if len(self.lane_) == 0:
                self.state = "Closed"
        elif len(self.lane_) < self.lane_capacity:
                self.state = "Open"
        else:
             self.state = "Full"




class Basket:
    def __init__(self, time_frame) -> None:
        self.time_frame = time_frame
        self._Basket_size = self._basket_size()

    def _basket_size(self):
        if self.time_frame == 1:
            return random.randint(1, 11)
        else:
            rand_value = random.randint(0, 10)
            if rand_value < 5:
                return self.time_frame * random.randint(10, 100) * 0.3
            else:
                return self.time_frame * random.randint(10, 100) * 0.7

    def get_basket_size(self):
        return self._Basket_size

    
    
class Customr:
    def __init__(self,time_frame,lane=None):
        self.time_frame = time_frame
        self.basket = Basket(time_frame)
        self.lottery_winner = 0
        self.lane = lane
        self._check_out_time_REG = None
        self._check_out_time_SELF = None
    def Lottery_winner(self):
        if self.basket.get_basket_size() < 10:
            pass
        elif self.basket.get_basket_size() >= 10:
            if random.randint(0,100) > 90:
                self.lottery_winner = 1
            else:
                pass
    def Check_out_time(self):
        self._check_out_time_REG = 4 * self.basket.get_basket_size() 
        self._check_out_time_SELF = 6 * self.basket.get_basket_size()
        return [self._check_out_time_REG, self._check_out_time_SELF]
    def Custmore_data_show(self):
        return f"""
                C1 -> items in basket: {self.basket.get_basket_size()}
                      time to process basket at cashier till: {self.Check_out_time()[0]} seconds
                      time to process basket at self service till: {self.Check_out_time()[1]} seconds
               """




