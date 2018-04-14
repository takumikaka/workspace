class AveragePerson{
    private String name, gender, height;
    private int age;

    public AveragePerson(){
        this.name = "Man";
        this.gender = "Male";
        this.height = "175cm";
        this.age = 0;
    }

    public AveragePerson(String name, String gender, String height, int age){
        this.name = name;
        this.gender = gender;
        this.height = height;
        this.age = age;
    }

    public void setName(String name){
        this.name = name;
    }
    public String getName(){
        return this.name;
    }
    public void setGender(String gender){
        this.gender = gender;
    }
    public String getGender(){
        return this.gender;
    }
    public void setHeight(String height){
        this.height = height;
    }
    public String getHeight(){
        return this.height;
    }
    public void setAge(int age){
        this.age = age;
    }
    public int getAge(){
        return this.age;
    }
}

public class CompoundClass{
    public static void main(String[] args){
        AveragePerson ap = new AveragePerson();
        System.out.println(ap.getName());
    }
}
