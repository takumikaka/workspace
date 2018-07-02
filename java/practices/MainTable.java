package org.xn.chapter6.practice;

public class MainTable
{
    public MainTable()
    {
        init();
        while(true)
        {
            goGame();
        }
    }

    private static Player boss = new Player();

    private static Player up = new Player();
    private static Player down = new Player();
    private static Player left = new Player();
    private static Player right = new Player();

    private static String[] total = Poker.poker;
    private int count = 0;
    private static String info = "Wait for the game to start.";

    public static void getTable()
    {
        System.out.println("\n\n");
        System.out.println("\t\t\t\t\t\t\t                                "+up);
        System.out.println("\t\t\t\t\t\t\t ***************************************************************************");
        System.out.println("\t\t\t\t\t\t\t *                                                                           * ");
        System.out.println("\t\t\t\t\t\t\t *                                                                           * ");
        System.out.println("\t\t\t\t\t\t\t *                                                                           * ");
        System.out.println("\t\t\t\t\t\t\t *                                                                           * ");
        System.out.println(left);
		System.out.println("\t *                          "+boss.getInfo(info)+"\t\t\t\t\t     * "+right);
        System.out.println("\t\t\t\t\t\t\t *                                                                           * ");
        System.out.println("\t\t\t\t\t\t\t *                                                                           * ");
        System.out.println("\t\t\t\t\t\t\t *                                                                           * ");
        System.out.println("\t\t\t\t\t\t\t *                                                                           * ");
        System.out.println("\t\t\t\t\t\t\t ***************************************************************************");
        System.out.println("\t\t\t\t\t\t\t                                "+down);

        System.out.println("\t\tPlease enter the number 0, Start the game.");
    }

    public static void init()
    {
        boss.setName("Boss");
        up.setName("Up");
        down.setName("Down");
        left.setName("Left");
        right.setName("Right");

        boss.setFlag(true);
        up.setFlag(true);
        down.setFlag(true);
        left.setFlag(true);
        right.setFlag(true);

        boss.setPok(total);
        up.setPok(new String[5]);
        down.setPok(new String[5]);
        left.setPok(new String[5]);
        right.setPok(new String[5]);
    }

    String[] bossPoker = null;
    String[] upPoker = null;
    String[] downPoker = null;
    String[] leftPoker = null;
    String[] rightPoker = null;

    public void sendPoker()
    {
        bossPoker = boss.getPok();
        upPoker = up.getPok();
        downPoker = down.getPok();
        leftPoker = left.getPok();

        if(count == 0)
        {
            int t1 = (int)(Math.random() * 52.0);
            int t2 = (int)(Math.random() * 52.0);
            int t3 = (int)(Math.random() * 52.0);
            int t4 = (int)(Math.random() * 52.0);

            upPoker[0] = bossPoker[t1];
            downPoker[0] = bossPoker[t2];
            leftPoker[0] = bossPoker[t3];
            rightPoker[0] = bossPoker[t4];
            count++;
        }

        if(count == 5)
        {
            info = "Game Over!";
            gameOver();
        }
        if(up.getFlag())
        {
            upPoker[count] = checkPoker((int)(Math.random() * 52.0));
        }
        if(down.getFlag())
        {
            downPoker[count] = checkPoker((int)(Math.random() * 52.0));
        }
        if(left.getFlag())
        {
            leftPoker[count] = checkPoker((int)(Math.random() * 52.0));
        }
        if(right.getFlag())
        {
            rightPoker[count] = checkPoker((int)(Math.random() * 52.0));
        }
        count++;
    }

    public String checkPoker(int t)
    {
        return bossPoker[t];
    }

    public void goGame()
    {
        getTable();
        Operate op = new Operate();
        int temp = op.getZero("Press '0' to send card.", "Input Error, Try again:");
        if(count == 5)
        {
            gameOver();
        }
        if(temp == 0 && count == 0)
        {
            info = "Gaming!";
            sendPoker();
        }else
        {
            checkPlayer();
            sendPoker();
        }
    }

    public void gameOver()
    {
        info = "Game Over!";
        getTable();
        System.out.println("Game Over!");
        System.exit(0);
    }

    public void checkPlayer()
    {
        Operate op = new Operate();
        int t1 = op.getOneTwo("Player: " + up.getName() + "Follow press '1', not press '2':", "Input Error, Try again:");
        if(t1 == 1)
        {
            up.setFlag(true);
        }else if(t1 == 2)
        {
            up.setFlag(false);
        }else
        {
            System.out.println("Input Error, Try again:");
        }

        int t2 = op.getOneTwo("Player: " + xia.getName() + "Follow press '1', not press '2':", "Input Error, Try again:");
        if(t1 == 1)
        {
            xia.setFlag(true);
        }else if(t1 == 2)
        {
            xia.setFlag(false);
        }else
        {
            System.out.println("Input Error, Try again:");
        }

        int t3 = op.getOneTwo("Player: " + left.getName() + "Follow press '1', not press '2':", "Input Error, Try again:");
        if(t1 == 1)
        {
            left.setFlag(true);
        }else if(t1 == 2)
        {
            left.setFlag(false);
        }else
        {
            System.out.println("Input Error, Try again:");
        }

        int t4 = op.getOneTwo("Player: " + right.getName() + "Follow press '1', not press '2':", "Input Error, Try again:");
        if(t1 == 1)
        {
            right.setFlag(true);
        }else if(t1 == 2)
        {
            right.setFlag(false);
        }else
        {
            System.out.println("Input Error, Try again:");
        }
    }
}
