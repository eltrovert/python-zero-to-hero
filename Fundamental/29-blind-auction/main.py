from art import logo
print(logo)
bids = {}
biddingFinished = False

def findHighestBidder(biddingRecord):
    highestBidder = ""
    highestBid = 0
    for bidder in biddingRecord:
        if biddingRecord[bidder] > highestBid:
            highestBid = biddingRecord[bidder]
            highestBidder = bidder
    print(f"Congratulations to {highestBidder} for winning the bidding with ${highestBid}")


while not biddingFinished:
    name = input("What is your name? ")
    price = int(input("What is your bid? $"))
    bids[name] = price

    shouldContinue = input("Are there any other bidder? Type 'yes' or 'no'. ").lower()
    if shouldContinue == "no":
        biddingFinished = True

findHighestBidder(bids)