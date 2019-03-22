public class PrintCommand implements Command{
    public void process(int[] target){
        for(int tmp : target){
            System.out.println("The element that iteratively outputs the array of objects: " + tmp);
        }
    }
}
