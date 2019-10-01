class NFA:
    transitionStates = {
        'q0': {
            '0': {'q0', 'q1'}, 
            '1': {'q0'}
        },
        'q1': {
            '1': {'q2'}
        }
    }
    symbols = ['0', '1']
    finalStates = ['q2']
    result = False

    def setSymbols(self, symbols):
        self.symbols = symbols
    
    def setFinalStates(self, finalStates):
        self.finalStates = finalStates

    def setTransitionStates(self, transitionStates):
        self.transitionStates = transitionStates

    def transition(self, currState, currSymbol):
        transitions = []
        for state in self.transitionStates:
            if currState == state:
                for symbol in self.transitionStates[state]:
                    if currSymbol == symbol:
                        return list(self.transitionStates[state][symbol])

        return transitions

    def accept(self, string, initialState):
        current = [initialState]
        pos = 0
        for i in string:
            print("Percobaan ",(pos+1), ": s=",current,"string=",string[pos:],"i=",i)
            if len(current) > 1:
                for state in current:
                    self.accept(string[pos:], state)
            elif len(current) == 1:
                current = self.transition(current[0], i)
            else:
                return False
            pos = pos + 1

        if len(current) == 1:
            for x in self.finalStates:
                if x == current[0]:
                    self.result = True
        
        return self.result

nfa = NFA()
string = '100101'
print(nfa.accept(string, 'q0'))


