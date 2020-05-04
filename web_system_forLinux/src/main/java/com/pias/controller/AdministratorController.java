package com.pias.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;

@Controller
@RequestMapping("/PIAS")
public class AdministratorController {

    @RequestMapping("/main")
    public String main(){
        System.out.println("进入到主界面了！");
        return "html/Patent_infringement_judgment";
    }
    @RequestMapping("/Patent_litigation_estimates")
    public String to_Patent_litigation_estimates(){
        System.out.println("进入到DNN了！");
        return "html/Patent_litigation_estimates";
    }
}
