public class SwitchTest{
    public static void main(String[] args){
        char grade = 'C';
        switch(grade)
        {
            case 'A':
                System.out.print("Good!!!\n");
                break;
            case 'B':
            case 'C':
                System.out.print("Nomal!!\n");
                break;
            case 'D':
                System.out.print("Pass!\n");
                break;
            case 'F':
                System.out.print("Bad...\n");
                break;
            default:
                System.out.print("No grade...\n");
        }
        System.out.print("You grade is:" + grade + "\n");
    }
}
