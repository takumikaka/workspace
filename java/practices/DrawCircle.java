import java.util.*;

public class DrawCircle{
    public static void main(String[] args){
        int r;
        Scanner scan = new Scanner(System.in);
        System.out.print("Please enter the radius of the circle R (an integer greater than 3): ");
        r = scan.nextInt();
        for(int y = 0; y<= 2 * r; y += 2){
            long x = Math.round(r - Math.sqrt(2 * r * y - y * y));
            long longLength = 2 * (r - x);
            for(int i = 0; i <= x; i++){
                System.out.print(" ");
            }
            System.out.print("*");
            for(double j = 0; j < longLength; j++){
                System.out.print(" ");
            }
            System.out.println("*");
        }
    }
}
