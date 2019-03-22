public class ContinueTest{
    public static void main(String[] args){
        int [] numbers = {10, 20, 30, 40, 50};
        for(int x: numbers){
            if(x==30){
                System.out.print("x is:" + x);
                System.out.print("\n");
                continue;
            }
            System.out.print(x);
            System.out.print(",");
            System.out.print("\n");
        }
    }
}
