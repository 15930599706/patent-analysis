<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>
<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title>专利文本分析系统</title>
    <link rel="stylesheet" href="../css/index.css">
    <link rel="stylesheet" href="../css/Patent_litigation_estimates.css">
    <script src="http://libs.baidu.com/jquery/1.10.2/jquery.min.js"></script>
    <script src="../js/cvi_busy_lib.js"></script>
  <script src="../js/Patent_litigation_estimates.js"></script>
  </head>
  <body>
    <div class="topWapper">
      <span class="topBar">专利文本分析系统</span>
      <span class="time" id="ymd">当前时间:2019年4月5日,星期五</span>
      <script>
          var date = new Date()
          var year = date.getFullYear()
          var month = date.getMonth()+1
          var day = date.getDate()
          if (date.getDay() == 1) {
            var week = '一'
          }
          else if (date.getDay() ==2 ) {
            var week = '二'
          }
          else if (date.getDay() ==3 ) {
            var week = '三'
          }
          else if (date.getDay() ==4 ) {
            var week = '四'
          }
          else if (date.getDay() == 5) {
            var week = '五'
          }
          else if (date.getDay() == 6) {
            var week = '六'
          }
          else if (date.getDay() == 7) {
            var week = '日'
          }
          document.getElementById("ymd").innerHTML = year+"年"+month+"月"+day+"日"+",星期"+week
      </script>
    </div>
    <div class="leftWapper">
      <ul class="functionWapper">
        <li class="function" id="msgMananger"><a href="/PIAS/main">产品侵权判断</a></li>
        <li class="function" id="monitor"><a href="/PIAS/Patent_litigation_estimates">涉诉金额预估</a></li>
      </ul>
    </div>
    <div class="main">
      <div class="mainWapper">
        <ul class="select_ul">
          <li class="select_li">
            <span>专利类型：</span>
            <select name="" id="selecte_PatentType" class="shortselect">
                  <option value="" disabled>---请选择--</option>
                  <option value="0" selected="selected">发明专利</option>
                  <option value="1">实用新型专利</option>
                  <option value="2">外观专利</option>
             </select>
          </li>
            <li class="select_li">
                <span>专利权人是否为外国人：</span>
                <select name="" id="selecte_Foreigner" class="shortselect">
                    <option value="" disabled>---请选择--</option>
                    <option value="0" selected="selected">不是外国人</option>
                    <option value="1">是外国人</option>
                </select>
            </li>
          <li class="select_li">
            <span>原告数量：</span>
            <select name="" id="selecte_PlaintiffNumber" class="shortselect">
                  <option value="" disabled>---请选择--</option>
                  <option value="0" selected="selected">单个</option>
                  <option value="1">多个</option>
             </select>
          </li>
          <li class="select_li">
            <span>原告类型：</span>
            <select name="" id="selecte_PlaintiffTypesr" class="shortselect">
                  <option value="" disabled>---请选择--</option>
                  <option value="0" selected="selected">非企业</option>
                  <option value="1">企业(包括企业和个人)</option>
             </select>
          </li>
          <li class="select_li">
            <span>被告数量：</span>
            <select name="" id="selecte_DefendantNumber" class="shortselect">
                  <option value="" disabled>---请选择--</option>
                  <option value="0" selected="selected">单个</option>
                  <option value="1">多个</option>
             </select>
          </li>
          <li class="select_li">
            <span>被告类型：</span>
            <select name="" id="selecte_DefendantTypesr" class="shortselect">
                  <option value="" disabled>---请选择--</option>
                  <option value="0" selected="selected">非企业</option>
                  <option value="1">企业(包括企业和个人)</option>
             </select>
          </li>
            <li class="select_li">
                <span>侵权企业注册资本：</span>
                <select name="" id="selecte_CompanyMoney" class="shortselect">
                    <option value="" disabled>---请选择--</option>
                    <option value="1" selected="selected">无(自然人或者个体工商户)</option>
                    <option value="2">0元<注册资本≤10万元</option>
                    <option value="3">10万元<注册资本≤100万元</option>
                    <option value="4">100万元<注册资本≤500万元</option>
                    <option value="5">500万元<注册资本≤1000万元</option>
                    <option value="6">注册资本>1000万元</option>
                </select>
            </li>
            <li class="select_li">
                <span>请求赔偿金额：</span>
                <select name="" id="selecte_OfferMoney" class="shortselect">
                    <option value="" disabled>---请选择--</option>
                    <option value="0" selected="selected">0元</option>
                    <option value="1" >0元<请求赔偿金额≤1万元</option>
                    <option value="2">1万元<请求赔偿金额≤10万元</option>
                    <option value="3">10万元<请求赔偿金额≤20万元</option>
                    <option value="4">20万元<请求赔偿金额≤50万元</option>
                    <option value="5">50万元<请求赔偿金额≤100万元</option>
                    <option value="6">100万元<请求赔偿金额≤1000万元</option>
                    <option value="7">请求赔偿金额>1000万元</option>
                </select>
            </li>
          <li class="select_li">
            <span>侵权地区：</span>
            <select name="" id="selecte_Region" class="shortselect">
                  <option value="" disabled>---请选择--</option>
                  <option value="1" selected="selected">华中</option>
                  <option value="2">华北</option>
                  <option value="3">华东</option>
                  <option value="4">华南</option>
                  <option value="5">西北</option>
                  <option value="6">东北</option>
                  <option value="7">西南</option>
             </select>
          </li>

          <li class="select_li">
            <span>侵权行为数量：</span>
            <select name="" id="selecte_IllegalNums" class="shortselect">
                  <option value="" disabled>---请选择--</option>
                  <option value="1" selected="selected">1</option>
                  <option value="2">2</option>
                  <option value="3">3</option>
                  <option value="4">4</option>
                  <option value="5" >5</option>
             </select>
             <span style="font-size:10px;">侵权行为包括制造、销售、生产、使用、进口</span>
          </li>


          <li class="select_li">
            <span>是否恶意侵权：</span>
            <select name="" id="selecte_intention" class="shortselect">
                  <option value="" disabled>---请选择--</option>
                  <option value="0" selected="selected">非恶意侵权</option>
                  <option value="1">恶意侵权</option>
             </select>
          </li>
        </ul>
      </div>
    </div>
    <div class="rightWapper">
      <ul class="functionWapper">
        <li class="function1" >
            <input  id="checkUser" type="checkbox" name="checkUser" required="required"><span style="color:black">已确认信息输入无误</span>
        </li>
        <li class="function2" >
          <input  class="sub"  id="dataSubmit"   value="预测赔偿金额">
        </li>
        <li class="function2" >
          <span id="result1" style="font-size:13px;color:red;"></span>
            <p id="result2" style="ont-size:13px;color:red;"></p>
        </li>
        <li>

        </li>
      </ul>
    </div>
  </body>
</html>
