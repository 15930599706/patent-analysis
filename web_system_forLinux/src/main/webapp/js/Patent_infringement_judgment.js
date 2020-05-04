$(function(){
	$("#formSubmit").click(function(){
	    if ($("#claimOfRight").val() != "" && $("#productFeature").val() != "" && $('#checkUser').prop('checked'))
        {
            var xval = getBusyOverlay('viewport', { color: 'white', opacity: 0.75, text: 'viewport: loading...', style: 'text-shadow: 0 0 3px black;font-weight:bold;font-size:16px;color:white' }, { color: '#ff0', size: 100, type: 'o' });
            $.ajax({
                type:"POST",
                url: '/PIAS/callVSM',

                data:{
                    "claimOfRight":$("#claimOfRight").val(),
                    "productFeature":$("#productFeature").val(),
                },
                dataType:'json',
                beforeSend: function() {
                    if (xval) {
                        xval.settext("正在分析中,大约需要两分钟时间，请稍后......");//此处可以修改默认文字，此处不写的话，就按照默认文字来。
                    }
                },
                complete: function(){
                    // 设置 进度条到80%
                },
                success:function(data){
                    xval.remove(); //此处是移除遮罩层
                    $("#result1").text("专利文本与产品特征文本的相似度为:"+data["textSimilarityResult"])
                    if (data["textSimilarity"] == "YES"){
                        $("#result2").text("经判定产品侵权!")
                    }
	                else {
                        $("#result2").text("经判定产品没有侵权!")
                    }

                },
                error:function(data){
                    xval.remove(); //此处是移除遮罩层
                    alert("error"+data)

                }
            });
        }
	    else {
	        alert("检查文本是否输入，确认信息输入无误了吗？");
        }

      })
})
