public class Recursive{
    public static int fn(int num){
        if(num == 0){
            return 1;
        }else if(num == 1){
            return 4;
        }else{
            return 2 * fn(num - 1) + fn(num - 2);
        }
    }

    public static void main(String[] args){
        int result = fn(10);
        System.out.println(result);
    }
}
