public class Overload{
    public void test(){
        System.out.println("Nonparametric!");
    }
    public void test(String msg){
        System.out.println("Overload test method: " + msg);
    }

    public static void main(String[] args){
        Overload ol = new Overload();
        ol.test();
        ol.test("Hello");
    }
}
