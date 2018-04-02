public class ModTest{
    public static void main(String[] args){
        double a = 1.1;
        double b = 2.2;
        double mod = a / b;
        System.out.println(mod);
        System.out.println("a / 0.0: " + a / 0.0);
        System.out.println("0 / 0.0: " + 0 / 0.0);
        System.out.println("0 / a: " + 0 / a);
    }
}
