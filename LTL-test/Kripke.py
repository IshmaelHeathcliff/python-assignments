class Kripke:
    def __init__(self,num_AP = 0, AP = [], S = [], S0 = [], R = [], L = []):
        self.num_AP = num_AP
        self.AP = AP
        self.S = S
        self.S0 = S0
        self.R = R
        self.L = []

    def add_AP(self, ap):
        self.AP.append(ap)
        self.num_AP += 1

    def add_S(self, sta, bin_lst):
        if not isinstance(sta, state):
            raise TypeError("in add_S, sta doesn't have a porper form")
        self.S.append(sta, state)
        if len(bin_lst) != self.num_AP:
            raise ValueError("in add_S, the lenth of bin_lst has no porper lenth")
        if isinstance(len(bin_lst), lst):
            raise TypeError("in add_S, bin_lst doesn't have a porper form")
        L.append(bin_lst)

    def put_S0(self, S0):
        if S0 not in self.S:
            raise TypeError("in put_S0, sta is not a valid state")
        # input the maybe list
        for x in S0:
            self.S0.append(S0)

    def add_R(self, sta1, sta2):
        if sta1 not in self.S or sta2 not in self.S:
            raise TypeError("in add_R, we don't have sta1 or sta2 in S")
