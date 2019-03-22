public class CommandTest3{
    public static void main(String[] args){
        ProcessArray pa = new ProcessArray();
        int[] array = {-1, 2, -6, 3};
        pa.process(array, (int[] target) ->{
            int sum = 0;
            for(int tmp : target){
                sum += tmp;
            }
            System.out.println("The sum is: " + sum);
        });
    }
}
