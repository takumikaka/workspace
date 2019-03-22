public class ContinueTestTwo{
    public static void main(String[] args){
        for(int num = 0; num < 10; num++){
            System.out.println("num is: " + num);
            if(num == 4){
                continue;
            }
            System.out.println("continue num is: " + num);
        }
    }
}
