public class OstrichTwo extends BirdTest{
    public String msg = "Can running...";

    public void flyOwer(){
        System.out.println(msg);
    }

    public void flyBase(){
        System.out.println(super.msg);
    }

    public static void main(String[] args){
        OstrichTwo ot = new OstrichTwo();
        ot.flyOwer();
        ot.flyBase();
    }
}
