public class DivTest{
    public static void main(String[] args){
        double a = 1.1;
        double b = 2.2;
        double c = -3.3;
        double div = a / b;

        System.out.println(div);
        System.out.println("a / 0.0:" + a / 0.0);
        System.out.println("c / 0.0:" + c / 0.0);
        System.out.println("b / 0:" + b / 0);
    }
}
