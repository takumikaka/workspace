public class RecursiveTwo{
    public static int fn(int num){
        if(num == 20){
            return 1;
        }else if(num == 21){
            return 4;
        }else{
            return fn(num + 2) - 2 * fn(num + 1);
        }
    }

    public static void main(String[] args){
        int result = fn(10);
        System.out.println(result);
    }
}
