/***************************************
 *         初始表单提交按钮            *
 ***************************************/
function initFormSubmitButton(scope) {
    logger.debug('initFormSubmitButton is called');
    scope.find('.form-submit-button').on('click', function () {
        logger.debug('form-submit-button.click is called');
        formId = $(this).data('form-id');
        form = $('#' + formId);
        form.submit();
    });
}

/***************************************
 *         滑动控件的初始化            *
 ***************************************/
function initSlider(scope) {
    // 遍历所有.slider-input并设置其最大最小值以及当前值
    scope.find('.slider-input').each(function () {
        $(this).slider({
            min: $(this).data("min"), max: $(this).data("max"), value: value = $(this).data("value")
        });
        inputId = $(this).data("input-id");
        $("#" + inputId).val($(this).data("value"));
        //console.log("inputId=" + inputId);
    });

    // 绑定.slider-input事件
    scope.find('.slider-input').slider({
        slide: function (event, ui) {
            //inputId = $(this).data("input-id");
            //console.log("inputId=" + inputId);
            $("#" + inputId).val(ui.value);
        }
    });
}

/*

 $( "#slider-range-min" ).slider({
 range: "min",
 value: 37,
 min: 1,
 max: 700,
 slide: function( event, ui ) {
 $( "#amount" ).val( "$" + ui.value );
 }
 });
 */
/***************************************
 *        所有控件初始化操作工作       *
 ***************************************/
function initial(scope) {
    initSlider(scope);
    initFormSubmitButton(scope);
}

/***************************************
 *          全局初始化加载操作         *
 ***************************************/
$(document).ready(function () {
    // 绑定body中的所有相关控件的事件
    // 并初始化switch和select
    initial($('body'));
});
