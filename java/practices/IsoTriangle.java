public class IsoTriangle{
    public static void main(String[] args){
        int num = 4;
        for(int i = 1; i <= num; i++){
            for(int j = 0; j < num - i; j++){
                System.out.print(" ");
            }
            for(int j = 1; j <= i * 2 - 1; j++ ){
                System.out.print("*");
            }
            System.out.println();
        }
    }
}
