public enum GenderBetterInter implements GenderDesc{
    Male, Female;
    private String name;
    public void setName(String name){
        switch(this){
            case Male:
                if(name.equals("Nan")){
                    this.name = name;
                }else{
                    System.out.println("Parameter error!");
                    return;
                }
                break;
            case Female:
                if(name.equals("Nv")){
                    this.name = name;
                }else{
                    System.out.println("Parameter error!");
                    return;
                }
                break;
        }
    }
    public String getName(){
        return name;
    }
    public void info(){
        System.out.println("This is an enumerated class for defining sex.");
    }
}
