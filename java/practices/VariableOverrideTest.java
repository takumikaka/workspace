public class VariableOverrideTest{
    private String name = "Gonku";
    private static double price = 11.7;

    public static void main(String[] args){
        int price = 117;
        System.out.println(price);
        System.out.println(new VariableOverrideTest().price);
        VariableOverrideTest vot = new VariableOverrideTest();
        vot.info();
    }

    public void info(){
        String name = "Jack";
        System.out.println(name);
        System.out.println(this.name);
    }
}
