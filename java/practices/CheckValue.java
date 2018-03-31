public class CheckValue{
    public static void main(String[] args){
        char c1 = 'a';
        int i1 = c1;
        System.out.println("char to int:" + i1);
        char c2 = 'A';
        int i2 = c2 + 1;
        System.out.println("char add int:" + i2);
        byte b = (byte)i2;
        System.out.println("byte b:" + b);
    }
}
