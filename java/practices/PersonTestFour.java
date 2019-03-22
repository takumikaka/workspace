public class PersonTestFour{
    {
        int a = 6;
        if(a > 4){
            System.out.println("Person initialization block, the value of the local variable a is greater than 4.");
        }
    }
    {
        System.out.println("Person second initialization blocks.");
    }
    public PersonTestFour(){
        System.out.println("Person class nonparametric constructor.");
    }

    public static void main(String[] args){
        new PersonTestFour();
    }
}
