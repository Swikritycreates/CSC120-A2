# Import a few useful containers from the typing module
from typing import Dict, Union

# Import the functions we wrote in procedural_resale_shop.py
from procedural_resale_shop import update_price, refurbish

class Computer:

    # required attributes
    description: str
    processor_type: str
    hard_drive_capacity: int
    memory: int
    operating_system: str
    year_made: int
    price: int

    # Constructor fir computer class
    def __init__(self, description: str,
                    processor_type: str,
                    hard_drive_capacity: int,
                    memory: int,
                    operating_system: str,
                    year_made: int,
                    price: int):
        self.description = description
        self.processor_type = processor_type
        self.hard_drive_capacity = hard_drive_capacity
        self.memory = memory
        self.operating_system = operating_system
        self.year_made = year_made
        self.price = price


#main of Computer class
def main():

    
    # First, let's make a computer
    computer = Computer("Mac Pro (Late 2013)", "3.5 Ghc 6-core Intel Xeon 5", 1024, 64, "macos Big Sur", 2013, 1500
 )


#Only call main() if I am running this program directly
if __name__ == "__main__":
  main()

