public class NumberTest{
    public static void main(String[] args){
        Integer n1 = 20;
        int m1 = n1;
        Integer n2 = 20;
        int m2 = n2;
        if(n1 == n2){
            System.out.println("true");
            System.out.println("n1 is:" + n1);
            System.out.println("n2 is:" + n2);
            System.out.println("m1 is:" + m1);
            System.out.println("m2 is:" + m2);
        }else{
            System.out.println("false");
            System.out.println("n1 is:" + n1);
            System.out.println("n2 is:" + n2);
            System.out.println("m1 is:" + m1);
            System.out.println("m2 is:" + m2);
        }
    }
}
