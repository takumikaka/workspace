public class NullAccessStatic{
    private static void test(){
        System.out.println("The class method of static modification.");
    }

    public static void main(String[] args){
        NullAccessStatic nas = null;
        nas.test();
    }
}
