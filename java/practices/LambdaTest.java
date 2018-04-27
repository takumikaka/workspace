public class LambdaTest{
    public static void main(String[] args){
        Object obj1 = (Runnable)() -> {
            for(int i = 0; i < 100; i++){
                System.out.println();
            }
        };
    }
}
