public class StringBufferTest{
    public static void main(String[] args){
        StringBuffer sBuffer = new StringBuffer("URL:");
        sBuffer.append("www.");
        sBuffer.append("baidu.");
        sBuffer.append("com");
        System.out.println(sBuffer);

        StringBuffer tBuffer = new StringBuffer("This is test word");
        tBuffer.insert(5, "the ");
        System.out.println(tBuffer);

        tBuffer.delete(5, 9);
        System.out.println(tBuffer);

        tBuffer.replace(5, 8, "the ");
        System.out.println(tBuffer);
    }
}
