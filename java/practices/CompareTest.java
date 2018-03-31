public class CompareTest{
    public static void main(String[] args){
        String str1 = "Hello Java";
        String str2 = "hello java";
        String str3 = "hello java & Hello Java";

        int result = str1.compareTo(str2);
        System.out.println(result);

        result = str2.compareTo(str3);
        System.out.println(result);

        result = str3.compareTo(str1);
        System.out.println(result);
    }
}
