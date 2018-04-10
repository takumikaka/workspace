public class PrimitiveTransferTest{
    public static void swap(int a, int b){
        int temp = a;
        a = b;
        b = temp;
        System.out.println("In the swap method, the value of a is: " + a + " the value of b is: " + b);
    }

    public static void main(String[] args){
        int a = 6;
        int b = 9;
        PrimitiveTransferTest pt = new PrimitiveTransferTest();
        pt.swap(a, b);
        System.out.println("When the exchange is finished, the value of the a is " + a + " the value of b is: " + b);
    }
}
