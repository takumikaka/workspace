package org.xn.chapter6.practice;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Operate
{
    private BufferedReader buf = null;
    public Operate()
    {
        this.buf = new BufferedReader(new InputStreamReader(System.in));
    }
    public String getString(String info)
    {
        String str = null;
        System.out.print(info);
        try
        {
            str = this.buf.readLine();
        }catch(IOException e){
            e.printStackTrace();
        }
        return str;
    }
    public int getZero(String info, String err)
    {
        int temp = 0;
        boolean flag = true;
        while(flag)
        {
            String str = this.getString(info);
            if(str.equals("0"))
            {
                temp = Integer.parseInt(str);
                flag = false;
            }
            else
            {
                System.out.print(err);
            }
        }
        return temp;
    }
    public int getOneTwo(String info, String err)
    {
        int temp = 0;
        boolean flag = true;
        while(flag)
        {
            String str = this.getString(info);
            if(str.equals("1")||str.equals("2"))
            {
                temp = Integer.parseInt(str);
                flag = false;
            }
            else
            {
                System.out.print(err);
            }
        }
        return temp;
    }
}
