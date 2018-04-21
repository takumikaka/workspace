public class BetterPrinter implements Output{
    private String[] printData = new String[MAX_CACHE_LINE * 2];
    private int dataNum = 0;
    public void out(){
        while(dataNum > 0){
            System.out.println("High speed printer printing: " + printData[0]);
            System.arraycopy(printData, 1, printData, 0, --dataNum);
        }
    }
    public void getData(String msg){
        if(dataNum >= MAX_CACHE_LINE * 2){
            System.out.println("The output queue is full, add failure.");
        }
        else{
            printData[dataNum++] = msg;
        }
    }
    public void print(String... msgs){
        for(String msg : msgs){
            System.out.println(msg);
        }
    }
}
