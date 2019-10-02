class NFA:
    __transitionStates = {}
    __symbols = []
    __finalStates = []
    __result = False

    # mengeset nilai simbol di property symbols
    def setSymbols(self, symbols):
        self.__symbols = symbols
    
    # mengeset nilai final state di property finalStates
    def setFinalStates(self, finalStates):
        self.__finalStates = finalStates

    # mengeset nilai tabel transition state di property transitionStates
    def setTransitionStates(self, transitionStates):
        self.__transitionStates = transitionStates

    # mencari nilai dari state selanjutnya 
    # dari tabel transition state yang ada
    # pada property transitionStates
    def transition(self, currentState, currentSymbol):
        # mencari state yang diberikan pada tabel transition state
        # dengan mengeceknya menggunakan perulangan
        for state in self.__transitionStates:
            # jika state ditemukan
            if currentState == state:
                # maka selanjutnya mencari simbol yang diberikan
                for symbol in self.__transitionStates[state]:
                    # jika simbol ditemukan
                    if currentSymbol == symbol:
                        # maka akan mengeluarkan list/array dari state selanjutnya
                        # karena pada NFA kemungkinan state yang
                        # ditemukan berjumlah lebih dari satu
                        return list(self.__transitionStates[state][symbol])

        # jika state maupun simbol tidak ditemukan
        # maka program akan mengeluarkan list/array kosong
        return []

    # mencari nilai dari state selanjutnya
    # dari tabel transition state yang ada
    # pada property transitionStates
    def transitionEpsilon(self, currentState):
        # mencari state yang diberikan pada tabel transition state
        # dengan mengeceknya menggunakan perulangan
        for state in self.__transitionStates:
            # jika state ditemukan
            if currentState == state:
                # maka selanjutnya mencari epsilon yang ada
                # pada tabel transition state
                for symbol in self.__transitionStates[state]:
                    # jika simbol ditemukan
                    if 'eps' == symbol:
                        # maka akan mengeluarkan list/array dari state selanjutnya
                        # karena pada NFA kemungkinan state yang
                        # ditemukan berjumlah lebih dari satu
                        return list(self.__transitionStates[state][symbol])

        return []

    # mengecek apakah string diterima oleh NFA
    def accept(self, string, initialState):
        # menyimpan list/array dari state terkini
        current = [initialState]

        # digunakan untuk menunjuk posisi
        # string yang akan dicek
        pos = 0

        # menyimpan panjang string
        max_length = len(string)

        # menyimpan nilai dari keberadaan 
        # suatu epsilon pada suatu transition function
        epsilon = False

        # mengecek ketika suatu transition function
        # sudah mencapai final state maka program
        # akan mengembalikan nilai True
        if self.__result == True:
            return True

        # melakukan perulangan ketika posisi
        # string belum mencapai akhir
        while pos != max_length:
            # mengecek apakah jumlah dari state terkini
            # ada lebih dari satu state atau tidak
            if len(current) > 1:
                # maka state akan dijalan satu persatu
                # dengan melakukan perulangan
                for state in current:
                    # memanggil fungsi accept (rekursif)
                    # untuk mengecek state satu persatu
                    # dengan ngoper nilai string yang
                    # belum dicek dan nilai dari state
                    # yang telah dipecah sebelumnya
                    self.accept(string[pos:], state)
            # jika statenya berjumlah satu
            elif len(current) == 1:
                # maka state akan disimpan pada variable temp
                temp = current[0]

                # menampung nilai state selanjutnya
                # kemudian mengubah nilai current state
                # karena sudah berpindah state
                current = self.transition(temp, string[pos])

                # jika state bernilai kosong ada kemungkinan
                # transition function berisikan epsilon
                if len(current) == 0:
                    # maka mencari state selanjutnya dengan 
                    # fungsi untuk mencari nilai epsilon 
                    # pada tabel transition state
                    current = self.transitionEpsilon(temp)

                    # jika ditemukan state
                    if len(current) > 0:
                        # maka variable epsilon akan bernilai True
                        epsilon = True
            
            # jika state bernilai kosong maka fungsi akan bernilai false
            else:
                return False

            # jika nilai epsilon bernilai False
            if epsilon == False:
                # maka posisi string akan berubah ke posisi selanjutnya
                pos = pos + 1
            # jika tidak
            else:
                # maka posisi string tidak berpindah dan nilai epsilon
                # kembali menjadi nilai default (False)
                epsilon = False

        # jika nilai state terkini lebih dari atau sama dengan satu
        if len(current) >= 1:
            # maka selanjutnya mencari nilai dari final state dari state terkini
            for x in self.__finalStates:
                for state in current:
                    # mengecek apakah nilai dari state terkini yang dipecah
                    # sama dengan salah satu dari final state
                    if x == state:
                        # jika iya, maka nilai propery result akan bernilai True
                        self.__result = True
        
        # mengembalikan nilai dari propery result (nilai diterimanya string)
        return self.__result


# membuat objek NFA
nfa = NFA()

# mendefinisikan simbol yang akan diterima
symbols = ["0", "1"]
nfa.setSymbols(symbols)

# menerima input string dari keyboard
string = input("Masukan string : ")

# mengecek apakah string diterima atau tidak
for x in string:
    # jika string tidak diterima maka program akan berhenti
    if not ((x == symbols[0]) or (x == symbols[1])):
        print("String tidak diterima")
        exit()


print("1. L1 adalah himpunan semua string yang mengandung substring 101")
print("2. L2 adalah himpunan semua string yang mengandung prefiks 101")
print("3. L3 adalah himpunan semua string yang mengandung sufiks 101")
print("4. L4 adalah himpunan semua string yang mengandung jumlah simbol 0 genap")
print("5. L5 adalah himpunan semua string yang mengandung jumlah simbol 1 ganjil")

# menerima input pilihan soal
pilihan = int(input("Masukkan bahasa yang ingin digunakan : "))

if pilihan == 1:
    # mendefinisikan tabel transition state
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

    # mendefinisikan initial state
    initialState = "q0"
    # mendefinisikan final state
    nfa.setFinalStates(["q3"])

elif pilihan == 2:
    # mendefinisikan tabel transition state
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

    # mendefinisikan initial state
    initialState = "q0"
    # mendefinisikan final state
    nfa.setFinalStates(["q3"])

elif pilihan == 3:
    # mendefinisikan tabel transition state
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

    # mendefinisikan initial state
    initialState = "q0"
    # mendefinisikan final state
    nfa.setFinalStates(["q3"])

elif pilihan == 4:
    # mendefinisikan tabel transition state
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

    # mendefinisikan initial state
    initialState = "q0"
    # mendefinisikan final state
    nfa.setFinalStates(["q1"])

elif pilihan == 5:
    # mendefinisikan tabel transition state
    nfa.setTransitionStates({
        "q0": {
            "eps": {"q1"}
        },
        "q1": {
            "0": {"q0"},
            "1": {"q2"}
        },
        "q2": {
            "0": {"q2"},
            "1": {"q1"}
        },
    })

    # mendefinisikan initial state
    initialState = "q0"
    # mendefinisikan final state
    nfa.setFinalStates(["q2"])

else:
    # ketika pilihan tidak sesuai
    print("Pilihan tidak sesuai")

# mengecek apakah string yang dimasukan
# dapat diterima oleh NFA
if nfa.accept(string, initialState) == True:
    print("-> String diterima")
else:
    print("-> String tidak diterima")
