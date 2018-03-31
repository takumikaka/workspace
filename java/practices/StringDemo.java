public class StringDemo{
    public static void main(String[] args){
        char[] charArray = {'H', 'e', 'l', 'l', 'o'};
        String printHello = new String(charArray);
        System.out.println(printHello);
        String site = "www.baidu.com";
        int len = site.length();
        System.out.println("site length:" + len);
        String s = "www.baidu.com";
        char result = s.charAt(8);
        System.out.println(result);
    }
}
