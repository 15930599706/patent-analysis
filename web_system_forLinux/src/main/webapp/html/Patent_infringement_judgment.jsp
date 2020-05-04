<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>
<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title>专利文本分析系统</title>
    <link rel="stylesheet" href="../css/index.css">
    <link rel="stylesheet" href="../css/Patent_infringement_judgment.css">
    <script src="http://libs.baidu.com/jquery/1.10.2/jquery.min.js"></script>
      <script src="../js/cvi_busy_lib.js"></script>
    <script src="../js/Patent_infringement_judgment.js"></script>
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
<%--          <form  id="textSubmitForm" class="textSubmitForm" method="post" ></form>--%>
          <div class="textSubmit-item">
              <textarea  id="claimOfRight"   name="claimOfRight"  required="required" placeholder="请输入专利权利要求说明"></textarea>
          </div>
          <div class="textSubmit-item">
              <textarea  id="productFeature"  name="productFeature" required="required" placeholder="请输入产品特征文本"></textarea>
          </div>
      </div>
    </div>
    <div class="rightWapper">
      <ul class="functionWapper">
        <li class="function1" >
            <input  id="checkUser" type="checkbox" name="checkUser" required="required"><span style="color:black">已确认文本信息输入无误</span>
        </li>
        <li class="function2" >
          <input  class="sub"  id="formSubmit"   value="开始侵权判定">
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
