public class DrawSquare{
    int a, b;
    int h;
    int i, j;
    public void draw(int h){
        for(i = 1; i <= h; i++){
            for(j = 1; j <= h; j++){
                if(j == (h + 3) / 2 - i || j == (h - 1) / 2 + i || j == i - (h - 1 ) / 2 || j == (3 * h + 1) / 2 - i){
                    System.out.print("*");
                }else{
                    System.out.print(" ");
                }
            }
            System.out.println();
        }
    }
    public static void main(String[] args){
        DrawSquare demo = new DrawSquare();
        int a = 35;
        demo.draw(35);
    }
}
