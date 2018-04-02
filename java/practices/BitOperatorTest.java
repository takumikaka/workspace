public class BitOperatorTest{
    public static void main(String[] args){
        int a = 5; // 0000 0101
        int b = 26; //0001 1010
        System.out.println("a & b: " + (a & b)); // 0000 0000 = 0
        System.out.println("a | b: " + (a | b)); // 0001 1111 = 31
        System.out.println("~a: " + ~a); // 1111 1010 = 250
        System.out.println("a ^ b: " + (a ^ b)); // 0001 1111 = 31
        System.out.println(" a << 2: " + (a << 2)); // 0001 0100 = 20
        System.out.println(" b >> 3: " + (b >> 3)); // 0000 0011 = 3
    }
}
