package com.pias.Interface;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.nio.charset.Charset;
import java.util.ArrayList;

public class VSMInterface
{
    public String getVSM(String textUUIDParam)
    {

        Process p;
        //CMD调用脚本
        String cmd="python3 /root/bishe/VSM_Word2Vec_model_package/VSM.py --textUUIDParam "+textUUIDParam;
        System.out.println("python脚本调用...");
        System.out.println(cmd);
        try
        {
            //执行命令
            p = Runtime.getRuntime().exec(cmd);
            //取得命令结果的输出流
            InputStream fis=p.getInputStream();
            //用一个读输出流类去读
            InputStreamReader isr=new InputStreamReader(fis, Charset.forName("UTF-8"));
            //用缓冲器读行
            BufferedReader br=new BufferedReader(isr);
            String line=null;
            //直到读完为止
            while((line=br.readLine())!=null)
            {
                //System.out.println(line);
                ArrayList List = new ArrayList();
                List.add(line);
                System.out.println(List);
            }
            System.out.println("python VSM脚本执行完毕！");
        }
        catch (IOException e)
        {
            e.printStackTrace();
        }
        return "VSM_OK";
    }
}
