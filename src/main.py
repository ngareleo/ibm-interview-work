import pandas as pd
import numpy as np
from helpers import open_csv_file

class OperateOnFile:

    def __init__(self) -> None:
        result1 = self.prob_of_taking_shuttle_from_kijauri()
        result2 = self.most_travelled_routes()
        result3 = self.prob_next_character_after_MK()
        print(f"The probability that a passenger travelling from Kijauri will take a Shuttle if they depart before 07:30 is {result1}")
        print(f"The most probable next character after MK is {result3}")
        print(f"Most travelled route is {result2}")


    def prob_of_taking_shuttle_from_kijauri(self):
        """Returns prob(taking shuttle if travelling from kijauri and depart_time < 07:30"""
        data = open_csv_file()

        """
            prob(taking shuttle if travelling from kijauri and depart from 07:30) = (c/b)
        """

        b = 0 #count(All who travelled from kijauri and departed before 07:30)
        c = 0 #count(Took shuttle and travelled from kijauri and departed before 07:30)
        for chunk in data:
            from_kijauri = chunk[(chunk["travel_from"] == "Kijauri") & (chunk["travel_time"] < 730)]
            from_kijauri_and_took_shuttle = chunk[chunk["car_type"] == "shuttle"]
            
            b += from_kijauri.size
            c += from_kijauri_and_took_shuttle.size
        
        return c / b

    def most_travelled_routes(self):
        data = open_csv_file()
        for chunk in data:
            travelled_from = chunk.travel_from
            print(travelled_from)


    def prob_next_character_after_MK(self):
        """Returns the most probable character that comes after MK in payment receipts"""
        data = open_csv_file()
        next_char_frequency = dict()

        for chunk in data:
            # filter all the transactions with MK in the payment receipt
            receipts_with_mk = chunk[chunk.payment_receipt.str.contains("MK")].payment_receipt
            for receipt in receipts_with_mk:
                loc:int = receipt.find("MK")
                # loc + 2 gives us the next character after the MK
                if loc+2 < len(receipt) - 1:
                    next_char: int = receipt[loc+2] 

                    """Updating the frequency table"""
                    temp = next_char_frequency.get(next_char)
                    if not temp:
                        next_char_frequency[next_char] = 1
                    else:
                        next_char_frequency.update({next_char: temp+1})

        """sorting items in the frequency table based on value"""
        most_common:tuple = sorted(next_char_frequency.items(), key=lambda item: item[1], reverse=True) #
        return most_common[0][0]



if __name__ == "__main__":
    op = OperateOnFile()