class BaseClass{
    public int name = 117;
    public void base(){
        System.out.println("The common method of the parent class.");
    }
    public void test(){
        System.out.println("The overlaid method of the parent class.");
    }
}

public class SubClassTwo extends BaseClass{
    public String name = "Master Chief";
    public void test(){
        System.out.println("A method of overlaying the parent class of a subclass.");
    }
    public void sub(){
        System.out.println("The common method of subclass.");
    }

    public static void main(String[] args){
        BaseClass bc = new BaseClass();
        System.out.println(bc.name);
        bc.base();
        bc.test();

        SubClassTwo sct = new SubClassTwo();
        System.out.println(sct.name);
        sct.test();
        sct.sub();

        BaseClass test = new SubClassTwo();
        System.out.println(test.name);
        test.base();
        test.test();
        //test.sub();
    }
}
