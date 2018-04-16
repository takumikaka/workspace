public class EqualTest{
    public static void main(String[] args){
        int it = 12;
        float ft = 12.0f;
        System.out.println("12 equal 12.0f? " + (it == ft));

        char ch = 'A';
        System.out.println("A equal 12? " + (it == ch));

        String st1 = "Hello";
        String st2 = "Hello";
        System.out.println("st1 equal st2?" + (st1 == st2));
    }
}
