@FunctionalInterface
interface Converter{
    Integer converter(String from);
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
    }
}
