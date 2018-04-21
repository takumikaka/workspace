public class OutputTest implements Output{
    public void out(){
        System.out.println(MAX_CACHE_LINE);
    }
    public void getData(String msg){
        return;
    }

    public static void main(String[] args){
        OutputTest opt = new OutputTest();
        opt.out();
    }
}
