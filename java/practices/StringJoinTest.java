public class StringJoinTest{
    public static void main(String[] args){
        String str1 = "CrazyJava.";
        String str2 = "Crazy" + "Java.";
        System.out.println("str1 equal str2? " + (str1 == str2));

        final String str3 = "Crazy";
        final String str4 = "Java.";
        String str5 = str3 + str4;
        System.out.println("str1 equal str5? " + (str1 == str5));
    }
}
