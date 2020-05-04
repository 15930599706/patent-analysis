package com.pias.controller;

import com.csvreader.CsvReader;
import com.pias.Interface.DNNInterface;
import com.pias.Interface.VSMInterface;
import net.sf.json.JSONObject;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.nio.charset.Charset;
import java.util.*;

//http://localhost:8080/PIAS_project/callVSM
@RestController
@RequestMapping("/PIAS")
public class CallVSM {

    @RequestMapping(value="/callVSM",method= RequestMethod.POST)

    private JSONObject callVSM(@RequestParam("claimOfRight") String claimOfRight, @RequestParam("productFeature") String productFeature) throws InterruptedException {

        System.out.println("进来了正式！");
        System.out.println(claimOfRight);
        System.out.println(productFeature);
        //生成文件唯一标识符（UUID）
        String uuid = UUID.randomUUID().toString();
        System.out.println(uuid);

        //输入文本转换成txt文件"Y:\myPyCharmWorkStation\graduation_project\VSM_Word2Vec_model_package\input"
        try{
            String claimF =  uuid + "_claims_init.txt";
            BufferedWriter bw = new BufferedWriter(new FileWriter("/root/bishe/VSM_Word2Vec_model_package/input/"+claimF));
            bw.write(claimOfRight);
            bw.close();				//关闭文件

            String productF =  uuid + "_product_init.txt";
            BufferedWriter bw2 = new BufferedWriter(new FileWriter("/root/bishe/VSM_Word2Vec_model_package/input/"+productF));
            bw2.write(productFeature);
            bw2.close();				//关闭文件
        }catch(IOException e) {
            e.printStackTrace();
        }

        //调用接口
        VSMInterface vsmInterface = new VSMInterface();
        System.out.println(vsmInterface.getVSM(uuid));

        //读取结果csv文件
        CallVSM callVSM = new CallVSM();
        JSONObject json=JSONObject.fromObject(callVSM.readResultCsv(uuid));
        System.out.println(json.toString());
        return json;
    }
    private Map<String,String> readResultCsv(String uuid){
        List<String> tmpresult = new ArrayList<>();
        Map<String,String> result=new HashMap<String, String>();
        CsvReader reader = null;
        try {
            //如果生产文件乱码，windows下用gbk，linux用UTF-8
            reader = new CsvReader("/root/bishe/VSM_Word2Vec_model_package/output/"+uuid+"_ModelOutput.csv", ',', Charset.forName("UTF-8"));

            // 不读取标题
            //reader.readHeaders();
            // 逐条读取记录，直至读完

            while (reader.readRecord()) {
                //读取第一列/读取第二列
                tmpresult.add(reader.get(0));
                tmpresult.add(reader.get(1));
            }
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            if (null != reader) {
                reader.close();
            }
        }
        result.put(tmpresult.get(0),tmpresult.get(2));
        result.put(tmpresult.get(1),tmpresult.get(3));

        System.out.println(result);
        return result;
    }

}