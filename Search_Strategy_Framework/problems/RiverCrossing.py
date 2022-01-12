from problems.Problem import Problem


class Stare:
    barca = 0
    sotii = [0, 0]
    soti = [0, 0]
    n = 2

    def HasHusband(self, mal):
        husbandlist = []
        k = 0
        for husband in self.soti:
            if husband == mal:
                husbandlist.append(k)
            k += 1
        return husbandlist

    def HasWife(self, mal):
        wifelist = []
        k = 0
        for wife in self.sotii:
            if wife == mal:
                wifelist.append(k)
            k += 1
        return wifelist

    def IsValid(self):
        for i in range(0, 2):
            husbands = self.HasHusband(i)
            wives = self.HasWife(i)
            if self.HasWife(i) and self.HasHusband(i):
                for wife in self.HasWife(i):
                    if self.sotii[wife] != self.soti[wife]:
                        return False
        return True

    def __eq__(self, other):
        if other.barca != self.barca:
            return False
        if other.n != self.n:
            return False
        for i in range(0,self.n):
            if self.sotii[i] != other.sotii[i]:
                return False
            if self.soti[i] != other.soti[i]:
                return False
        return True

    def __hash__(self):
        return hash(str(self))

    def copy(self):
        stare = Stare()
        stare.barca = self.barca
        stare.soti = self.soti.copy()
        stare.sotii = self.sotii.copy()
        stare.n = self.n
        return stare

    def __str__(self):
        str_soti = [str(int) for int in self.soti]
        str_sotii = [str(int) for int in self.sotii]
        return "{barca:" + str(self.barca) + ", soti:" + ",".join(str_soti) + " sotii:" + ",".join(str_sotii) + "}"


class RiverCrossing(Problem):
    def GetCost(self, state1, state2):
        return 1

    initial_state = None
    final_state = None
    number_of_states =0

    def __init__(self):
        self.initial_state = Stare()
        self.final_state = Stare()
        self.final_state.barca = 1
        self.final_state.soti = [1, 1]
        self.final_state.sotii = [1, 1]
        self.all_states = [self.initial_state]
        self.all_states = self.GenerateAllStates()
        self.number_of_states = len(self.all_states)

    def GenerateNeighbors(self, state):
        result = []
        if state.barca == 0:
            for i in range(0, state.n):
                for j in range(0, state.n):
                    if i != j and state.soti[i] == state.soti[j]:
                        stare = state.copy()
                        stare.barca = 1
                        stare.soti[i] = 1
                        stare.soti[j] = 1
                        if stare.IsValid():
                            result.append(stare)

                    if state.soti[i] == state.sotii[j]:
                        stare = state.copy()
                        stare.barca = 1
                        stare.soti[i] = 1
                        stare.sotii[j] = 1
                        if stare.IsValid():
                            result.append(stare)

                    if i != j and state.sotii[i] == state.sotii[j]:
                        stare = state.copy()
                        stare.barca = 1
                        stare.sotii[i] = 1
                        stare.sotii[j] = 1
                        if stare.IsValid():
                            result.append(stare)
        else:
            for i in range(0, state.n):
                if state.soti[i] == 1:
                    stare = state.copy()
                    stare.barca = 0
                    stare.soti[i] = 0
                    if stare.IsValid():
                        result.append(stare)

                if state.sotii[i] == 1:
                    stare = state.copy()
                    stare.barca = 0
                    stare.sotii[i] = 0
                    if stare.IsValid():
                        result.append(stare)
        return result

    def GenerateAllStates(self):
        visited = []
        root = 0
        states = self.all_states.copy()
        while root < len(states):
            visited.append(states[root])
            temp_states = self.GenerateNeighbors(states[root])
            for state in temp_states:
                if state not in visited and state not in states:
                    states.append(state)
        return states

    def GetAllStates(self):
        return self.all_states

