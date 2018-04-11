public class Varargs{
    public static void test(int a, String[] books){
        for(String tmp : books){
            System.out.println(tmp);
        }
        System.out.println(a);
    }

    public static void main(String[] args){
        String[] books = new String[] {"This is test.", "This is java test."};
        test(6, books);
    }
}
