public class MammalInt implements Animal{
    public void eat(){
        System.out.println("eat.....");
    }
    public void travel(){
        System.out.println("travel.....");
    }

    public static void main(String[] args){
        MammalInt mi = new MammalInt();
        mi.eat();
        mi.travel();
    }
}
