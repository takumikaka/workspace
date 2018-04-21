public class OutputFactory{
    public Output getOutput(){
        return new BetterPrinter();
    }
    public static void main(String[] args){
        OutputFactory of = new OutputFactory();
        Computer c = new Computer(of.getOutput());
        c.keyIn("This is java test...");
        c.keyIn("Crazy java");
        c.print();
    }
}
