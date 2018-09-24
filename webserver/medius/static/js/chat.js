$(document).on('click', '.panel-heading span.icon_minim', function (e) {
    var $this = $(this);
    console.log("panel-heading")
    if (!$this.hasClass('panel-collapsed')) {
        $this.parents('.panel').find('.panel-body').slideUp();
        $this.addClass('panel-collapsed');
        $this.removeClass('glyphicon-minus').addClass('glyphicon-plus');
    } else {
        $this.parents('.panel').find('.panel-body').slideDown();
        $this.removeClass('panel-collapsed');
        $this.removeClass('glyphicon-plus').addClass('glyphicon-minus');
    }
});
$(document).on('focus', '.panel-footer input.chat_input', function (e) {
    var $this = $(this);
    if ($('#minim_chat_window').hasClass('panel-collapsed')) {
        $this.parents('.panel').find('.panel-body').slideDown();
        $('#minim_chat_window').removeClass('panel-collapsed');
        $('#minim_chat_window').removeClass('glyphicon-plus').addClass('glyphicon-minus');
    }
});
$(document).on('click', '#new_chat', function (e) {
    var size = $( ".chat-window:last-child" ).css("margin-left");
     size_total = parseInt(size) + 400;
    alert(size_total);
    var clone = $( "#chat_window_1" ).clone().appendTo( ".container" );
    clone.css("margin-left", size_total);
    console.log("click function is invoked")

});
$(document).on('click', '.icon_close', function (e) {
    //$(this).parent().parent().parent().parent().remove();
    $( "#chat_window_1" ).remove();
});


function create_new_message(type, message){
    var msg = {type:type, message:message}

};

function create_user_dlg(message){
    msg = ' \
    <div class="row msg_container base_sent"> \
        <div class="col-md-10 col-xs-10"> \
            <div class="messages msg_sent"> \
                <p>'+message+'</p> \
                <time datetime="2009-11-13T20:00">User</time> \
            </div> \
        </div> \
        <div class="col-md-2 col-xs-2 avatar"> \
            <img src="/static/img/user.png" class=" img-responsive "> \
        </div> \
    </div>'

    return msg;
};

function create_robot_dlg(message){
    msg='<div class="row msg_container base_receive"> \
        <div class="col-md-2 col-xs-2 avatar"> \
            <img src="/static/img/robot.png" class=" img-responsive "> \
        </div> \
        <div class="col-md-10 col-xs-10"> \
            <div class="messages msg_receive"> \
                <p>'+message+'</p> \
                <time datetime="2009-11-13T20:00">Medius</time> \
            </div> \
        </div> \
    </div>'
    return msg;
};

function scroll_to_bottom(){
    var chatHistory = document.getElementById("msg_body_id");
    chatHistory.scrollTop = chatHistory.scrollHeight;
    // $("#msg_body_id").scrollTop = $("#msg_body_id").scrollHeight;
    var h = chatHistory.scrollHeight;
    console.log(h);
};

function set_input_type(input_type){
    var x = document.getElementById("btn-input");
    var y = document.getElementById("sel1");
    if (input_type == "input"){
        x.style.display = "block";
        y.style.display = "none";
    } else if (input_type=="select"){
        y.style.display = "block";
        x.style.display = "none";
    } else {
        x.style.display = "block";
        y.style.display = "none";
    }
};

