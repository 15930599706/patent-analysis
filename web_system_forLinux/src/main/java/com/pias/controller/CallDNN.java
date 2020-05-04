package com.pias.controller;

import com.csvreader.CsvReader;
import com.pias.Interface.DNNInterface;
import net.sf.json.JSONObject;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import java.nio.charset.Charset;
import java.util.*;

//http://localhost:8080/PIAS_project/callDNN
@RestController
@RequestMapping("/PIAS")
public class CallDNN {
    @RequestMapping(value="/callDNN",method= RequestMethod.POST)
    private JSONObject callDNN(@RequestParam("selecte_PatentType") String selecte_PatentType,
                               @RequestParam("selecte_Foreigner") String selecte_Foreigner,
                               @RequestParam("selecte_PlaintiffNumber") String selecte_PlaintiffNumber,
                               @RequestParam("selecte_PlaintiffTypesr") String selecte_PlaintiffTypesr,
                               @RequestParam("selecte_DefendantNumber") String selecte_DefendantNumber,
                               @RequestParam("selecte_DefendantTypesr") String selecte_DefendantTypesr,
                               @RequestParam("selecte_CompanyMoney") String selecte_CompanyMoney,
                               @RequestParam("selecte_OfferMoney") String selecte_OfferMoney,
                               @RequestParam("selecte_Region") String selecte_Region,
                               @RequestParam("selecte_IllegalNums") String selecte_IllegalNums,
                               @RequestParam("selecte_intention") String selecte_intention){
        System.out.println("进来了！");
        String features = "["+selecte_PatentType+","+selecte_Foreigner+","+selecte_PlaintiffNumber
                +","+selecte_PlaintiffTypesr+","+selecte_DefendantNumber+","+selecte_DefendantTypesr
                +","+selecte_CompanyMoney+","+selecte_OfferMoney+","+selecte_Region+","+selecte_IllegalNums
                +","+selecte_intention+"]";

        System.out.println(features);

        //生成文件唯一标识符（UUID）
        String uuid = UUID.randomUUID().toString();
        System.out.println(uuid);

        //调用接口
        DNNInterface dnnInterface = new DNNInterface();
        System.out.println(dnnInterface.getDNN(uuid,features));

        //读取结果csv文件
        CallDNN callDNN = new CallDNN();
        JSONObject json=JSONObject.fromObject(callDNN.readResultCsv(uuid));
        System.out.println(json.toString());

        return json;
    }

    private Map<String,String> readResultCsv(String uuid){
        List<String> tmpresult = new ArrayList<>();
        Map<String,String> result=new HashMap<String, String>();
        CsvReader reader = null;
        try {
            //如果生产文件乱码，windows下用gbk，linux用UTF-8
            reader = new CsvReader("/root/bishe/DNN_model_package/output/" + uuid+"_ModelOutput.csv", ',', Charset.forName("UTF-8"));

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