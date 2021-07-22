class atm(object):

    def __init__(self,cardnumber,pinnumber):
        self.cardnumber = cardnumber
        self.pinnumber = pinnumber

    def Cashwidrawl(self):
        print("ruppees xyz")
    def BalanceEnquiry(self):
        print("BalanceEnquiry abc ")
    
atm = atm(800151114008,8)

print(atm.Cashwidrawl())
print(atm.BalanceEnquiry())
