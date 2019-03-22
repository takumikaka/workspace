class Root{
    static{
        System.out.println("Static initialization block of root.");
    }
    {
        System.out.println("Common initialization block of root.");
    }
    public Root(){
        System.out.println("Root without parameter constructors.");
    }
}

class Mid extends Root{
    static{
        System.out.println("Static initialization block of mid.");
    }
    {
        System.out.println("Common initialization block of mid.");
    }
    public Mid(){
        System.out.println("mid without parameter constructors.");
    }
    public Mid(String msg){
        System.out.println("Root band parameter constructor. " + msg);
    }
}

class Leaf extends Mid{
    static{
        System.out.println("Static initialization block of leaf.");
    }
    {
        System.out.println("Common initialization block of leaf.");
    }
    public Leaf(){
        super("Hello Java!");
        System.out.println("Execute the constructor of the leaf.");
    }
}

public class TestTwo{
    public static void main(String[] args){
        new Leaf();
        new Leaf();
    }
}
