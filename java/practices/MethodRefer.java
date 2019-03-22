import javax.swing.JFrame;

@FunctionalInterface
interface Converter{
    Integer converter(String from);
}

@FunctionalInterface
interface MyTest{
    String test(String a, int b, int c);
}

@FunctionalInterface
interface YourTest{
    JFrame win(String title);
}

public class MethodRefer{
    public static void main(String[] args){
        //Converter converter1 = from -> Integer.valueOf(from);
        Converter converter1 = Integer :: valueOf;
        Integer value1 = converter1.converter("117");
        System.out.println(value1);

        //Converter converter2 = from -> "fkit.org".indexOf(from);
        Converter converter2 = "fkit.org" :: indexOf;
        Integer value2 = converter2.converter("o");
        System.out.println(value2);

        //Mytest mt = (a, b, c) -> a.substring(b, c);
        MyTest mt = String :: substring;
        String str = mt.test("I Love Python!", 2, 8);
        System.out.println(str);

        //YourTest yt = (String a) -> new JFrame(a);
        YourTest yt = JFrame :: new;
        JFrame jf = yt.win("My windows");
        System.out.println(jf);
    }
}
