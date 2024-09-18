from typing import Dict, Optional

from computer import *

class ResaleShop:

    # What attributes will it need?
    itemID: int # We'll increment this every time we add a new item 
    inventory : Dict[int, Computer] = {}     # so that we always have a new value for the itemID


    # How will you set up your constructor?
    def __init__(self, inventory: dict):
        self.inventory = inventory
        self.itemID = 0

    # What methods will you need?

    def buy(self, computer: Dict):
      self.itemID += 1 # increment itemID
      self.itemID = computer
      self.inventory[self.itemID] = {
        "description": computer.description,
        "processor_type": computer.processor_type,
        "hard_drive_capacity": computer.hard_drive_capacity,
        "memory": computer.memory,
        "operating_system": computer.operating_system,
        "year_made": computer.year_made,
        "price": computer.price
    }
      return self.itemID
    
    def update_price(self, item_id: int, new_price: int):
      if item_id in self.inventory:
          self.inventory[item_id]["price"] = new_price
      else:
          print("Item", item_id, "not found. Cannot update price.")

    def sell(self, item_id: int):
      if item_id in self.inventory:
          del self.inventory[item_id]
          print("Item", item_id, "sold!")
      else: 
          print("Item", item_id, "not found. Please select another item to sell.")
        
    def print_inventory(self, inventory):
    # If the inventory is not empty
      if self.inventory:
         # For each item
         for item_id in self.inventory:
            # Print its details
            print(f'Item ID: {item_id} : {inventory[item_id] }')
      else:
        print("No inventory to display.")

    def refurbish(self, item_id: int, new_os: Optional[str] = None):
      if item_id in self.inventory:
          computer = self.inventory[item_id] # locate the computer
          if int(computer["year_made"]) < 2000:
              computer["price"] = 0 # too old to sell, donation only
          elif int(computer["year_made"]) < 2012:
              computer["price"] = 250 # heavily-discounted price on machines 10+ years old
          elif int(computer["year_made"]) < 2018:
              computer["price"] = 550 # discounted price on machines 4-to-10 year old machines
          else:
              computer["price"] = 1000 # recent stuff

          if new_os is not None:
              computer["operating_system"] = new_os # update details after installing new OS
      else:
           print("Item", item_id, "not found. Please select another item to refurbish.")


def main():
        computer = Computer(
        "Mac Pro (Late 2013)",
        "3.5 GHc 6-Core Intel Xeon E5",
        1024, 64,
        "macOS Big Sur", 2013, 1500
    )
        inventory : Dict[int, Computer] = {"description": computer.description, "processor_type": computer.processor_type, "hard_drive_capacity": computer.hard_drive_capacity, "memory": computer.memory, "operating_system": computer.operating_system, "year_made": computer.year_made, "price": computer.price}     # so that we always have a new value for the itemID


        shop = ResaleShop(inventory)

      

        # Print a little banner
        print("-" * 21)
        print("COMPUTER RESALE STORE")
        print("-" * 21)

        # Add it to the resale store's inventory
        print("Buying", "description")
        print("Adding to inventory...")
        computer_id = shop.buy(computer)
        print("Done.\n")

        # Make sure it worked by checking inventory
        print("Checking inventory...")
        shop.print_inventory(inventory)
        print("Done.\n")

        # Now, let's refurbish it
        new_OS = "MacOS Monterey"
        print("Refurbishing Item ID:", computer_id, ", updating OS to", new_OS)
        print("Updating inventory...")
        shop.refurbish(computer_id, new_OS)
        print("Done.\n")

        # Make sure it worked by checking inventory
        print("Checking inventory...")
        shop.print_inventory(inventory)
        print("Done.\n")
        
        # Now, let's sell it!
        print("Selling Item ID:", computer_id)
        shop.sell(computer_id)
        
        # Make sure it worked by checking inventory
        print("Checking inventory...")
        shop.print_inventory(inventory)
        print("Done.\n")
            
main()

