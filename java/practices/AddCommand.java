public class AddCommand implements Command{
    public void process(int[] target){
        int sum = 0;
        for(int tmp : target){
            sum = sum + tmp;
        }
        System.out.println("The sum of the array elements is: " + sum);
    }
}
