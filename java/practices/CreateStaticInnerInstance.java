class StaticOut{
    static class StaticIn{
        public StaticIn(){
            System.out.println("Static internal class constructor.");
        }
    }
}

public class CreateStaticInnerInstance{
    public static void main(String[] args){
        StaticOut.StaticIn in = new StaticOut.StaticIn();
    }
}
