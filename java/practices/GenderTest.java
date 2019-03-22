public class GenderTest{
    public static void main(String[] args){
        Gender g = Enum.valueOf(Gender.class, "Female");
        String name = "Nv";
        System.out.println(g + " means: " + name);
    }
}
