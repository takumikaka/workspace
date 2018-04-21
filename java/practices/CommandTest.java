public class CommandTest{
    public static void main(String[] args){
        ProcessArray pa = new ProcessArray();
        int[] target = {-1, -2, 2, 1};
        pa.process(target, new PrintCommand());
        System.out.println("---------------------");
        pa.process(target, new AddCommand());
    }
}
