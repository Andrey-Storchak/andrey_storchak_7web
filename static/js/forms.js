
$(document).ready(function() {

    function showResult(responseText){
        //Show result of posted request

        //remove previous alerts
        $('.alert').removeClass('alert-danger').css({
            'display':'none'
        });;
        $('inpit').removeClass('has-error');



        var $result_field = $("#alert-result");
        if (responseText['form_errors']) {
            //add error to summary result field

            $result_field.addClass('alert-danger')
            .text(responseText['message'])
            .css({'display':'true'});

            for (var err_key in responseText['form_errors']) {
                //get error handlers
                var $err_label = $("#alert-" + err_key);

                //add errors
                $err_label.addClass("alert-danger")
                .css({"display": "true",})
                $err_label.text(responseText['form_errors'][err_key]);
            }
        }
        else {
            $result_field.addClass('alert-success')
            .text(responseText['message'])
            .css({'display':'true'});
            };
        };

    function showProgress(){
        $('.progress').css({
            'display': 'true'
        });
    };

    function hideProgress(){
        $('.progress').css({
            'display': 'none'
      });
    };


    $("#add-note").on('submit', function(event) {
        //Ajax form sending
        event.preventDefault();
        var $progress_bar = $('.progress');
        var url = $(this).attr('action');
        var method = $(this).attr('method');
        showProgress();
            $.ajax({
            type: method,
            url: url,
            data: $(this).serialize(),
            crossDomain: true,
            success: function(data, textStatus, jqXHR){
                hideProgress();
                showResult(data);
            }
            });
        });
});
