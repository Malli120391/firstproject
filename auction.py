import os
print("########### Welcome to Auction ###########")
def find_winner(bidder_details):
    highest__bid=0
    winner=0
    for bidder in bidder_details:
        bidding_price=bidder_details[bidder]
        if bidding_price>highest__bid:
            highest__bid=bidding_price
            winner=bidder
    print(f"Here is the list of all the bidders:{bidder_details}")
    print(f"The winner is {winner} with a bid price of {highest__bid}")
bidder_data={}
end_of_bidding=False
while not end_of_bidding:
   name=input("What is your name?: ")
   price=int(input("What is your bid?: "))
   bidder_data[name]=price
   more_bidders=input("Are there more bidders? Type 'yes' or 'no' : ").lower()
   if more_bidders=='no':
      end_of_bidding=True
      find_winner(bidder_data)
   elif more_bidders=='yes':
       os.system('cls')
