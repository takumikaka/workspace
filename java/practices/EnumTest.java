public class EnumTest{
    public void judge(SeasonEnum s){
        switch(s){
            case Spring:
                System.out.println("Spring is good.");
                break;
            case Summer:
                System.out.println("Summer is hot!");
                break;
            case Fail:
                System.out.println("Fail is good.");
                break;
            case Winter:
                System.out.println("Winter is cold!");
                break;
        }
    }

    public static void main(String[] args){
        for(SeasonEnum s : SeasonEnum.values()){
            System.out.println(s);
        }
        new EnumTest().judge(SeasonEnum.Summer);
    }
}
