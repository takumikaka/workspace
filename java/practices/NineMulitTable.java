public class NineMulitTable{
    public static void main(String[] args){
        for(int i = 1; i <= 9; i++){
            for(int j = 1; j <= 9; j++){
                if(i < j){
                    continue;
                }else{
                    int result = i * j;
                    System.out.print(i + "*" + j + "=" + result + " ");
                }
            }
            System.out.print("\n");
        }
    }
}
