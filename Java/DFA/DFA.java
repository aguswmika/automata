public class DFA {
    //properti menampung initial state
    private int initialState;
    //properti menampung sejumlah final state
    private int[] finalStates;
    //properti menampung tabel state transition
    private int[][] transitionStates;
    //properti menampung sejumlah simbol
    private char[] symbols;

    
    /*
    ** digunakan untuk mengambil nilai initial state 
    ** menuju properti initialState
    */
    public void setInitialState(int initialState) {
        this.initialState = initialState;
    }
    
    /*
    ** digunakan untuk mengambil nilai tabel state transition
    ** menuju properti transitionStates
    */
    public void setTransitionStates(int[][] transitionStates) {
        this.transitionStates = transitionStates;
    }
    
    /*
    ** digunakan untuk mengambil nilai final state
    ** menuju properti finalStates
    */
    public void setFinalStates(int[] finalStates) {
        this.finalStates = finalStates;
    }
    
    /*
    ** digunakan untuk mengambil nilai simbol
    ** menuju properti symbols
    */
    public void setSymbols(char[] symbols) {
        this.symbols = symbols;
    }
    
    
    /*
    ** digunakan untuk mengambil nilai state
    ** dari tabel transition state yang ada pada
    ** properti transitionStates 
    */
    public int transform(int state, char symbols) {
        int i;
        
        // melakukan pencarian dari properti simbol
        // untuk menemukan key dari simbol tersebut
        for (i = 0; i < this.symbols.length; i++) {
            // mengecek simbol yang ingin dicari dengan
            // simbol yang ada pada properti symbols
            if(symbols == this.symbols[i])
                break;
        }
        
        // mengembalikan nilai state selanjutnya
        // dari current state dan simbol yang dimasukkan
        return this.transitionStates[state][i];
    }
    
    /*
    ** digunakan untuk mengecek apakah string yang
    ** dimasukan apakah diterima oleh DFA
    */
    public int accept(String string){
        // mengeset nilai awal dari current state
        // dengan initial state
        int current = this.initialState;
        
        // digunakan untuk melakukan increment pada 
        // tiap looping
        int i;
        
        // looping untuk mencari state selanjutnya dari
        // current state dan simbol yang dimasukkan
        for (i = 0; i < string.length(); i++) {
            // menampung nilai state selanjutnya 
            // kemudian mengubah nilai current state
            // karena sudah berpindah state
            current = this.transform(current, string.charAt(i));
        }
        
        // menginisialisasi nilai untuk
        // mengecek nilai apakah string 
        // diterima atau tidak
        int end = 0;
        
        // mengecek nilai dari current state
        // apakah sudah berada pada final state
        // atau tidak
        for (i = 0; i < this.finalStates.length; i++) {
            
            // mengecek nilai current state
            // apakah sama dengan nilai final state
            if(current == this.finalStates[i])
                // jika iya, maka nilai variable
                // end menjadi 1 atau diterima
                end = 1;
        }
        
        // mengembalikan nilai dari string diterima
        // atau tidak oleh DFA
        return end;
    }

}
