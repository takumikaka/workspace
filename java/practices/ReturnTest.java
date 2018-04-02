public class ReturnTest{
    public static void main(String[] args){
        for(int num = 0; num < 5; num++){
            System.out.println("num is: " + num);
            if(num == 3){
                return;
            }
            System.out.println("return num is: " + num);
        }
    }
}
