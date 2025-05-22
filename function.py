import db_helper
import random

class OrderIDGenerator:
    def __init__(self):
        self.generated_ids = set()

    def generate(self):   
        while True:
            new_id = random.randint(1000, 9999)
            if new_id not in db_helper.fetch_order_ids() and new_id not in self.generated_ids:
                self.generated_ids.add(new_id)
                return new_id
            
generator = OrderIDGenerator()


def read_welcome_message():
    with open('welcome_msg.txt', 'r',encoding="utf-8") as file:
        content = file.read()
        message = content.strip().split('\n\n')

        return random.choice(message)

if __name__ == "__main__":
    print("This module is not meant to be run directly.")
    print("Please use the main application to interact with the chatbot.")
    print(read_welcome_message())

