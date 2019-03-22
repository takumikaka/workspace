public class GrendTestBetter{
    public static void main(String[] args){
        GenderBetter gb = GenderBetter.valueOf("Female");
        gb.setName("Nv");
        System.out.println(gb + " means: " + gb.getName());
        gb.setName("Nan");
        System.out.println(gb + " means: " + gb.getName());
    }
}
