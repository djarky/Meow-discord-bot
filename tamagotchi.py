
import pytz
from datetime import datetime
import asyncio

zona_horaria="America/La_Paz"

tama_com=("meow feed","meow sleep","meow awake","meow status","meow play")

from foods import FOODS_LIST, FAV_FOODS, HATE_FOODS

class Tamagotchi:
    def __init__(self, name):
        self.name = name
        self.hunger = 50
        self.energy = 50
        self.happiness = 50
        self.last_update = datetime.now(pytz.timezone(zona_horaria))
        self.sleeping = False
        self.foods = FOODS_LIST 

        self.favorite_foods = FAV_FOODS
        self.hated_foods = HATE_FOODS
        
        self.max_value = 100
        self.min_value = 0

        self.value_rate = 5

       
##
    def fix_values(self):
        if self.energy < 0:
            self.energy = 0
        if self.hunger < 0:
            self.hunger = 0
        if self.happiness < 0:
            self.happiness = 0           
        
        if self.energy > 100:
            self.energy = 100
        if self.hunger > 100:
            self.hunger = 100
        if self.happiness > 100:
            self.happiness = 100                
##
    def feed(self, food):
        if food not in [food_tuple[0] for food_tuple in self.foods]:
          raise ValueError("El alimento no está en la lista de alimentos permitidos")
    
        if food in self.favorite_foods:
            self.happiness += 10
        elif food in self.hated_foods:
            self.happiness -= 10
                
        for food_tuple in self.foods:
            if food_tuple[0] == food:
                nutrition = food_tuple[1]
                break
        
        self.hunger += nutrition
        
        self.fix_values()
##

    def show_foods(self):
        foods_names = [food[0] for food in self.foods ]
        foods_names.sort()
        result = "use ```meow feed [food]```\n Las comidas disponibles son:\n ```\n "
        for food in foods_names:
            result += f"-{food}\n"
        return result+"```"

      
##    
    def sleep(self):
        self.sleeping = True
    def awake(self):
        self.sleeping = False
    
    def play(self):
        self.happiness += 10
        self.energy -=5
        if self.happiness > 100:
            self.happiness = 100
        if self.energy <0:
            self.energy = 0
    
##    
    def status(self):
        status_string = "Status:\n"
        if self.sleeping:
            status_string += "zzz\n"
        status_string +="```\n"          
        status_string += F"HUNGER      : {self.print_bars(self.hunger)}\n"
        status_string += F"ENERGY      : {self.print_bars(self.energy)}\n"
        status_string += F"HAPPINESS   : {self.print_bars(self.happiness)}"
        return status_string+"```"    




####  
    def update(self):
        current_time = datetime.now(pytz.timezone(zona_horaria))
        time_difference = (current_time - self.last_update).total_seconds() / 3600.0
      #auto sleep awake
        hour = current_time.hour
        if hour >= 23 or hour <= 6: 
            self.sleep()
            print("auto zz")
        if hour >= 12 and hour <= 16: 
            self.awake() 
			#si duerme o no
        if self.sleeping:
            self.energy += int(time_difference * 20)
            self.hunger -= int(time_difference * 2)

        else:
            self.energy -= int(time_difference * 10)
            self.hunger -= int(time_difference * 5)
		
        if self.hunger < 50 or self.energy < 50:
            self.happiness -= int(time_difference * 5)           
        self.fix_values()        

  
        self.last_update = current_time
##
    
    def save(self, file_name):
        with open(file_name, "w") as f:
            f.write(f"{self.name}\n")
            f.write(f"{self.hunger}\n")
            f.write(f"{self.energy}\n")
            f.write(f"{self.happiness}\n")
            f.write(f"{self.last_update}\n")
            
            f.write(f"{self.sleeping}\n")
##    
    def load(self, file_name):
        with open(file_name, "r") as f:
            self.name = f.readline().strip()
            self.hunger = int(f.readline().strip())
            self.energy = int(f.readline().strip())
            self.happiness = int(f.readline().strip())
            self.last_update = datetime.fromisoformat(f.readline().strip())
            
            self.sleeping = str_to_bool(f.readline().strip())
##    
    def print_bars(self, value):
        bars = "█" * (value // 10)
        remainder = value % 10
        if remainder > 0:
            if remainder >= 5:
                bars += "▓"
            else:
                bars += "░"
        bars += "░" * (10 - len(bars))
        return f"[{bars}]"

##
    def run_tamagotchi(self, command):

        self.load("tamagotchi.txt")
        self.update()
        #print(command+"unu")

        if command.split()[0].lower()== "feed":
            feed_cmd =command.split()
            feed_cmd.pop(0)
            the_food = ' '.join(feed_cmd)
                        
            try:
                self.feed(the_food)
            except ValueError:
                return self.show_foods()
        elif command == "sleep":
            self.sleep()
        elif command == "awake":
            self.awake()
        elif command == "play":
            self.play()

        self.update()
        self.save("tamagotchi.txt")
        return self.status()

##
    async def update_loop(self):
        while True:
            await asyncio.sleep(3700)  
            print("update")
            self.load("tamagotchi.txt")
            self.update()  
            self.save("tamagotchi.txt")
          
##

def str_to_bool(s):
    if s == 'True':
         return True
    elif s == 'False':
         return False
    else:
         raise ValueError


def is_tama_cmd(s):
    return (len(s.split())>=2 and (s.lower()in tama_com or (s.split()[0].lower()=="meow" and s.split()[1].lower()=="feed"))) 
  

    
