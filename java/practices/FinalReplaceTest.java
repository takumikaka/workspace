public class FinalReplaceTest{
    public static void main(String[] args){
        final int a = 5 + 2;
        final double b = 1.3 / 2;
        final String str = "Crazy Java!";
        final String book = "Crazy Java: " + 99.0;
        final String book2 = "Crazy Java: " + String.valueOf(99.0);
        System.out.println(book == "Crazy Java: 99.0");
        System.out.println(book2 == "Crazy Java: 99.0");
    }
}
