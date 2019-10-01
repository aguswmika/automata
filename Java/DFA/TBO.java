import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class TBO {
    public static void main(String[] args) {
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        
        int i;
        String string = null; //menampung string
        int menu = 0;
      
        System.out.print("DFA statis\n"
                        +"Alfabet ={'0','1'}\n"
                        +"Masukkan string : ");
        
        try{
            //menyimpan string masukan user
            string = input.readLine();
            
            //perulangan memeriksa apakah semua char string ada dalam alfabet
            for (i = 0;i < string.length();i++){
                //jika ada char string yang tidak ada di alfabet
                if(!(string.charAt(i)=='0' || string.charAt(i)=='1')){
                    System.out.println("ERROR: String mengandung symbol di luar alfabet");
                    return;
                }
            }
            
        }catch(IOException e){
            System.out.print("ERROR: "+e.getMessage());   
        }    
        
        System.out.print("1.L1 adalah himpunan semua string yang mengandung substring 101\n"
                        +"2.L2 adalah himpunan semua string yang mengandung prefiks 101\n"
                        +"3.L3 adalah himpunan semua string yang mengandung sufiks 101\n"
                        +"4.L4 adalah himpunan semua string yang mengandung jumlah simbol 0 genap\n"
                        +"5.L5 adalah himpunan semua string yang mengandung jumlah simbol 1 ganjil\n"
                        +"Masukkan bahasa yang ingin digunakan : ");
        
        try{
            //menyimpan string masukan user
            menu = Integer.parseInt(input.readLine());
           
        }catch(IOException e){
            System.out.print("ERROR: "+e.getMessage());   
        }  
        
        // membuat obyek dari mesin DFA
        DFA dfa = new DFA();
        
        // menginisialisasi nilai initial state
        int initialState;
        // menginisialisasi nilai final state
        int[] finalState;
        // menginisialisasi nilai tabel transition state 
        int[][] transitionStates;
        // menginisialisasi nilai simbol
        char[] symbols = {'0', '1'};
        
        switch(menu){
            case 1:
                // mengeset nilai initial state
                initialState = 0;
                
                // mengeset jumlah final state
                finalState = new int[1];
                // mengeset nilai final state
                finalState[0] = 3;
                
                // mengeset jumlah nilai pada tabel transition state
                transitionStates = new int[4][2];
                // mengeset jumlah nilai tabel transition state
                transitionStates[0][0] = 0;
                transitionStates[0][1] = 1;
                transitionStates[1][0] = 2;
                transitionStates[1][1] = 1;
                transitionStates[2][0] = 0;
                transitionStates[2][1] = 3;
                transitionStates[3][0] = 3;
                transitionStates[3][1] = 3;
                   
                // memasukkan nilai initial state ke mesin DFA
                dfa.setInitialState(initialState);
                // memasukkan nilai final state ke mesin DFA
                dfa.setFinalStates(finalState);
                // memasukkan nilai simbol ke mesin DFA
                dfa.setSymbols(symbols);
                // memasukkan nilai tabel transition state ke mesin DFA
                dfa.setTransitionStates(transitionStates);
                
                // mengecek apakah DFA menerima string yang dimasukkan
                // oleh pengguna
                if(dfa.accept(string) == 1)
                    System.out.println("-> String diterima");
                else
                    System.out.println("-> String ditolak");
                    
                break;
                
            case 2:
                // mengeset nilai initial state
                initialState = 0;
                // mengeset jumlah final state
                finalState = new int[1];
                // mengeset nilai final state
                finalState[0] = 3;
                
                // mengeset jumlah nilai pada tabel transition state
                transitionStates = new int[5][2];
                // mengeset jumlah nilai tabel transition state
                transitionStates[0][0] = 4;
                transitionStates[0][1] = 1;
                transitionStates[1][0] = 2;
                transitionStates[1][1] = 4;
                transitionStates[2][0] = 4;
                transitionStates[2][1] = 3;
                transitionStates[3][0] = 3;
                transitionStates[3][1] = 3;
                transitionStates[4][0] = 4;
                transitionStates[4][1] = 4;
                
                // memasukkan nilai initial state ke mesin DFA
                dfa.setInitialState(initialState);
                // memasukkan nilai final state ke mesin DFA
                dfa.setFinalStates(finalState);
                // memasukkan nilai simbol ke mesin DFA
                dfa.setSymbols(symbols);
                // memasukkan nilai tabel transition state ke mesin DFA
                dfa.setTransitionStates(transitionStates);
                
                // mengecek apakah DFA menerima string yang dimasukkan
                // oleh pengguna
                if(dfa.accept(string) == 1)
                    System.out.println("-> String diterima");
                else
                    System.out.println("-> String ditolak");
                    
                break;
                
            case 3:
                // mengeset nilai initial state
                initialState = 0;
                // mengeset jumlah final state
                finalState = new int[1];
                // mengeset nilai final state
                finalState[0] = 3;
                
                // mengeset jumlah nilai pada tabel transition state
                transitionStates = new int[4][2];
                // mengeset jumlah nilai tabel transition state
                transitionStates[0][0] = 0;
                transitionStates[0][1] = 1;
                transitionStates[1][0] = 2;
                transitionStates[1][1] = 1;
                transitionStates[2][0] = 0;
                transitionStates[2][1] = 3;
                transitionStates[3][0] = 0;
                transitionStates[3][1] = 1;
                
                // memasukkan nilai initial state ke mesin DFA
                dfa.setInitialState(initialState);
                // memasukkan nilai final state ke mesin DFA
                dfa.setFinalStates(finalState);
                // memasukkan nilai simbol ke mesin DFA
                dfa.setSymbols(symbols);
                // memasukkan nilai tabel transition state ke mesin DFA
                dfa.setTransitionStates(transitionStates);
                
                // mengecek apakah DFA menerima string yang dimasukkan
                // oleh pengguna
                if(dfa.accept(string) == 1)
                    System.out.println("-> String diterima");
                else
                    System.out.println("-> String ditolak");
                    
                break;
                
            case 4:
                // mengeset nilai initial state
                initialState = 0;
                // mengeset jumlah final state
                finalState = new int[1];
                // mengeset nilai final state
                finalState[0] = 0;
                
                // mengeset jumlah nilai pada tabel transition state
                transitionStates = new int[2][2];
                // mengeset jumlah nilai tabel transition state
                transitionStates[0][0] = 1;
                transitionStates[0][1] = 0;
                transitionStates[1][0] = 0;
                transitionStates[1][1] = 1;
                
                // memasukkan nilai initial state ke mesin DFA
                dfa.setInitialState(initialState);
                // memasukkan nilai final state ke mesin DFA
                dfa.setFinalStates(finalState);
                // memasukkan nilai simbol ke mesin DFA
                dfa.setSymbols(symbols);
                // memasukkan nilai tabel transition state ke mesin DFA
                dfa.setTransitionStates(transitionStates);
                
                // mengecek apakah DFA menerima string yang dimasukkan
                // oleh pengguna
                if(dfa.accept(string) == 1)
                    System.out.println("-> String diterima");
                else
                    System.out.println("-> String ditolak");
                    
                break;
                
            case 5:
                // mengeset nilai initial state
                initialState = 0;
                // mengeset jumlah final state
                finalState = new int[1];
                // mengeset nilai final state
                finalState[0] = 1;
                
                // mengeset jumlah nilai pada tabel transition state
                transitionStates = new int[2][2];
                // mengeset jumlah nilai tabel transition state
                transitionStates[0][0] = 0;
                transitionStates[0][1] = 1;
                transitionStates[1][0] = 1;
                transitionStates[1][1] = 0;
                
                // memasukkan nilai initial state ke mesin DFA
                dfa.setInitialState(initialState);
                // memasukkan nilai final state ke mesin DFA
                dfa.setFinalStates(finalState);
                // memasukkan nilai simbol ke mesin DFA
                dfa.setSymbols(symbols);
                // memasukkan nilai tabel transition state ke mesin DFA
                dfa.setTransitionStates(transitionStates);
                
                // mengecek apakah DFA menerima string yang dimasukkan
                // oleh pengguna
                if(dfa.accept(string) == 1)
                    System.out.println("-> String diterima");
                else
                    System.out.println("-> String ditolak");
                    
                break;
            
        
            default:
                System.out.println("Menu salah");
                break;
        }
    }
    
}
