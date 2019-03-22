@FunctionalInterface
interface Displayable{
    void display();
    default int add(int a, int b){
        return a + b;
    }
}

public class LambdaAndInner{
    private int age = 17;
    private static String name = "[Crazy Java Center]";
    public void test(){
        String book = "Crazy Java";
        Displayable dis = () -> {
            System.out.println("The local variable of book is: " + book);
            System.out.println("External variables of name is: " + name);
            System.out.println("External variables of age is: " + age);
        };
        dis.display();
        System.out.println(dis.add(3, 5));
    }
    public static void main(String[] args){
        LambdaAndInner lai = new LambdaAndInner();
        lai.test();
    }
}
