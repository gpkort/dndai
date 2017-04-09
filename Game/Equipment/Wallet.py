
class Wallet(object):

    def __init__(self, copper: int= 0, silver: int = 0, electrum: int = 0, gold: int = 0, platinum: int = 0):
        self.cp = copper
        self.sp = silver
        self.ep = electrum
        self.gp = gold
        self.pp = platinum
        # self.gems = {}

    # def add_gem(self, name: str, value_in_gold: int=0):
    #     assert name is not None or len(name) == 0
    #
    #     i = 1
    #     while name in self.gems:
    #         name = name + str(i)
    #
    #     self.gems[name, value_in_gold]
    #
    # def get_gem(self, name: str)-> object:
    #     return self.__gems.pop(name)

    def fill_wallet(self, wallet):
        self.cp += wallet.cp
        self.sp += wallet.sp
        self.ep += wallet.ep
        self.gp += wallet.gp
        self.pp += wallet.pp


"""
100 cp = 1 gp 
2 ep = 1 gp
10 sp = 1 gp 
5 gp = 1 pp
1 pp = 5 gp = 10ep = 50sp = 500cp
"""
