public class CommandTest2{
    public static void main(String[] args){
        ProcessArray pa = new ProcessArray();
        int[] target = {-1, 1, 7, -2};
        pa.process(target, new Command(){
            public void process(int[] target){
                int sum = 0;
                for(int tmp : target){
                    sum += tmp;
                }
                System.out.println("The sum is: " + sum);
            }
        }
        );
    }
}
