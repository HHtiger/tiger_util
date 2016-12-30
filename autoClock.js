/*
 * 自动补卡信息
 * 直接在浏览器运行
 * */
$.each($("input[type='checkbox']"), function(n, value) {
    if ($(this).parent().parent().attr("style") && ($(this).parent().parent().attr("style").indexOf('palegoldenrod') == -1)) {
        $(this).attr("checked", true);
        $(this).parent().next().next().children("select").val("8");
        if ($(this).parent().prev().find("select").length > 0) {
            $(this).parent().next().children().val("18:00:00");
        } else {
            $(this).parent().next().children().val("09:00:00");
        }

    }
});