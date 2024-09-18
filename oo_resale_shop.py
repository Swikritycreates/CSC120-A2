from typing import Dict, Optional

from computer import Computer

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
      self.inventory[self.itemID] = computer
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
        
    def print_inventory(self):
    # If the inventory is not empty
      if self.inventory:
         # For each item
         for item_id in self.inventory:
            # Print its details
            print(f'Item ID: {item_id} : {self.inventory[item_id].year_made, self.inventory[item_id].price, self.inventory[item_id].description,self.inventory[item_id].hard_drive_capacity,self.inventory[item_id].operating_system, self.inventory[item_id].processor_type, self.inventory[item_id].memory }')
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
        inventory : Dict[int, Computer] = {}     # so that we always have a new value for the itemID

        shop = ResaleShop(inventory)

        computer1 = Computer(
            "Mac Pro (Late 2013)",
            "3.5 GHc 6-Core Intel Xeon E5",
            1024, 64,
            "macOS Big Sur", 2013, 1500
        )
        shop.buy(computer1)
        shop.print_inventory()
        shop.sell(1)
        shop.refurbish(1, "Windows 11")
        shop.update_price(1,40)
main()

