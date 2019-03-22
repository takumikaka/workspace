interface Product{
    int getProduceTime();
}

public class Printer implements Output, Product{
    private String[] printData = new String[MAX_CACHE_LINE];
    private int dataNum = 0;
    public void out(){
        while(dataNum > 0){
            System.out.println("Print Printing: " + printData[0]);
            System.arraycopy(printData, 1, printData, 0, --dataNum);
        }
    }
    public void getData(String msg){
        if(dataNum >= MAX_CACHE_LINE){
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
    public int getProduceTime(){
        return 45;
    }
    public static void main(String[] args){
        Output o = new Printer();
        o.getData("This is java test");
        o.getData("Crazy java");
        o.out();
        o.getData("Crazy Android");
        o.getData("Crazy Python");
        o.out();
        o.print("son guku", "son guhan", "aqiang");
        Product p = new Printer();
        System.out.println(p.getProduceTime());
    }
}
