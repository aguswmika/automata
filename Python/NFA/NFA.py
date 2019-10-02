class NFA:
    __transitionStates = {
        "q0": {
            "0": {"q0", "q1"}, 
            "1": {"q0"}
        },
        "q1": {
            "1": {"q2"}
        }
    }
    __symbols = ["0", "1"]
    __finalStates = ["q2"]
    __result = False

    def setSymbols(self, symbols):
        self.__symbols = symbols
    
    def setFinalStates(self, finalStates):
        self.__finalStates = finalStates

    def setTransitionStates(self, transitionStates):
        self.__transitionStates = transitionStates

    def transition(self, currentState, currentSymbol):
        for state in self.__transitionStates:
            if currentState == state:
                for symbol in self.__transitionStates[state]:
                    if currentSymbol == symbol:
                        return list(self.__transitionStates[state][symbol])

        return []

    def transitionEpsilon(self, currentState):
        for state in self.__transitionStates:
            if currentState == state:
                for symbol in self.__transitionStates[state]:
                    if 'eps' == symbol:
                        return list(self.__transitionStates[state][symbol])

        return []

    def accept(self, string, initialState):
        current = [initialState]
        pos = 0
        max_length = len(string)
        epsilon = False
        while pos != max_length:
            if len(current) > 1:
                for state in current:
                    self.accept(string[pos:], state)
            elif len(current) == 1:
                temp = current[0]
                current = self.transition(temp, string[pos])

                if len(current) == 0:
                    current = self.transitionEpsilon(temp)
                    if len(current):
                        epsilon = True
            else:
                return False

            if epsilon == False:
                pos = pos + 1
            else:
                epsilon = False

        if len(current) >= 1:
            for x in self.__finalStates:
                for state in current:
                    if x == state:
                        self.__result = True
        
        return self.__result


# membuat objek NFA
nfa = NFA()

# menerima input string dari keyboard
string = input("Masukan string : ")

print("1. L1 adalah himpunan semua string yang mengandung substring 101")
print("2. L2 adalah himpunan semua string yang mengandung prefiks 101")
print("3. L3 adalah himpunan semua string yang mengandung sufiks 101")
print("4. L4 adalah himpunan semua string yang mengandung jumlah simbol 0 genap")
print("5. L5 adalah himpunan semua string yang mengandung jumlah simbol 1 ganjil")
pilihan = int(input("Masukkan bahasa yang ingin digunakan : "))

if pilihan == 1:
    nfa.setTransitionStates({
        "q0" : {
            "0" : {"q0"},
            "1" : {"q0", "q1"}
        },
        "q1": {
            "0": {"q2"},
        },
        "q2": {
            "1": {"q3"}
        },
        "q3": {
            "0": {"q3"},
            "1": {"q3"}
        },
    })
    initialState = "q0"
    nfa.setFinalStates(["q3"])

elif pilihan == 2:
    nfa.setTransitionStates({
        "q0": {
            "1": {"q1"}
        },
        "q1": {
            "0": {"q2"},
        },
        "q2": {
            "1": {"q3"}
        },
        "q3": {
            "0": {"q3"},
            "1": {"q3"}
        },
    })

    initialState = "q0"
    nfa.setFinalStates(["q3"])

elif pilihan == 3:
    nfa.setTransitionStates({
        "q0": {
            "1": {"q0", "q1"}
        },
        "q1": {
            "0": {"q2"},
        },
        "q2": {
            "1": {"q3"}
        }
    })

    initialState = "q0"
    nfa.setFinalStates(["q3"])

elif pilihan == 4:
    nfa.setTransitionStates({
        "q0": {
            "eps": {"q1"},
        },
        "q1": {
            "0": {"q2"},
            "1": {"q0", "q1"},
        },
        "q2": {
            "0": {"q1"},
            "1": {"q2"}
        }
    })

    initialState = "q0"
    nfa.setFinalStates(["q1"])

elif pilihan == 5:
    nfa.setTransitionStates({
        "q0": {
            "0": {"q0"},
            "1": {"q0", "q1"}
        },
        "q1": {
            "0": {"q1"},
        }
    })

    initialState = "q0"
    nfa.setFinalStates(["q1"])

else:
    print("Pilihan tidak sesuai")

if nfa.accept(string, initialState) == True:
    print("-> String diterima")
else:
    print("-> String tidak diterima")
