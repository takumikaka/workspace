package org.xn.chapter6.practice;

public class Player
{
    private String name;
    private String location;
    private boolean flag = true;
    private String[] pok = new String[5];
    public Player(){}
    public Player(String name, String location)
    {
        this.name = name;
        this.location = location;
    }

    public String toString()
    {
        StringBuffer buf = new StringBuffer();
        for(int i = 1; i < pok.length; i ++)
        {
            buf.append("[").append(pok[i]).append("]");
        }
        return "Player: " + name + ", Botton Card: " + "[" + pok[0] + "]" + ", Face Card: " + buf.toString();
    }

    public String getInfo(String info)
    {
        return info;
    }

    public boolean getFlag()
    {
        return flag;
    }

    public void setFlag(boolean flag)
    {
        this.flag = flag;
    }

    public String getName(String name)
    {
        return name;
    }

    public void setName(String name)
    {
        this.name = name;
    }

    public String[] getPok()
    {
        return pok;
    }

    public void setPok(String[] pok)
    {
        this.pok = pok;
    }

    public String getLocation()
    {
        return location;
    }

    public void setLocation(String location)
    {
        this.location = location;
    }

    public static void main(String[] args)
    {
        //Player player = new Player("Jack", "shang");
        //player.setLocation("shang");
        //System.out.println(player.getLocation());
    }
}
