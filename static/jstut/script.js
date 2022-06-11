$(document).ready(function() {
        $('form').submit(function(event) {
                event.preventDefault()
                form = $("form")

                $.ajax({
                        'url': '/ajax/register/',
                        'url': '/ajax/accounts/login',
                        'type': 'POST',
                        'data': form.serialize(),
                        'dataType': 'json',
                        'success': function(data) {
                            alert(data['success'])
                        },
                    }) // END of Ajax method
                $('#username').val('')
                $("#email").val('')
                $("#password1").val('')
                $("#password2").val('')
            }) // End of submit event

    }) // End of document ready function