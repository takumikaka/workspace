public class ConstructorOverload{
    public String msg;
    public int num;

    public ConstructorOverload(){

    }

    public ConstructorOverload(String msg, int num){
        this.msg = msg;
        this.num = num;
    }

    public static void main(String[] args){
        ConstructorOverload co1 = new ConstructorOverload();
        ConstructorOverload co2 = new ConstructorOverload("Hello Java", 117);
        System.out.println("co1.msg is: " + co1.msg + " co1.num is: " + co1.num);
        System.out.println("co2.msg is: " + co2.msg + " co2.num is: " + co2.num);
    }
}
