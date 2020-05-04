$(function(){
	$("#dataSubmit").click(function(){
	    if ($('#checkUser').prop('checked'))
        {
            var xval = getBusyOverlay('viewport', { color: 'white', opacity: 0.75, text: 'viewport: loading...', style: 'text-shadow: 0 0 3px black;font-weight:bold;font-size:16px;color:white' }, { color: '#ff0', size: 100, type: 'o' });
            $.ajax({
                type:"POST",
                url: '/PIAS/callDNN',

                data:{
                    "selecte_PatentType":$("#selecte_PatentType").val(),
                    "selecte_Foreigner":$("#selecte_Foreigner").val(),
                    "selecte_PlaintiffNumber":$("#selecte_PlaintiffNumber").val(),
                    "selecte_PlaintiffTypesr":$("#selecte_PlaintiffTypesr").val(),
                    "selecte_DefendantNumber":$("#selecte_DefendantNumber").val(),

                    "selecte_DefendantTypesr":$("#selecte_DefendantTypesr").val(),
                    "selecte_CompanyMoney":$("#selecte_CompanyMoney").val(),
                    "selecte_OfferMoney":$("#selecte_OfferMoney").val(),
                    "selecte_Region":$("#selecte_Region").val(),
                    "selecte_IllegalNums":$("#selecte_IllegalNums").val(),

                    "selecte_intention":$("#selecte_intention").val(),
                },
                dataType:'json',
                beforeSend: function() {
                    if (xval) {
                        xval.settext("正在分析中，请稍后......");//此处可以修改默认文字，此处不写的话，就按照默认文字来。
                    }
                },
                complete: function(){
                    // 设置 进度条到80%
                },
                success:function(data){
                    xval.remove(); //此处是移除遮罩层
                    $("#result1").text("估算的赔偿金额区间为:"+data["result"])
                },
                error:function(data){
                    xval.remove(); //此处是移除遮罩层
                    alert("error"+data)

                }
            });
        }
	    else {
	        alert("确认信息输入无误了吗？");
        }

      })
})
