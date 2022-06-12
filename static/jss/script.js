$(document).ready(function() {
        $('form').submit(function(event) {
                event.preventDefault()
                form = $("form")

                $.ajax({
                        'url': '/ajax/register/',
                        'type': 'POST',
                        'data': form.serialize(),
                        'dataType': 'json',
                        'success': function(data) {
                            alert(data['success'])
                        },
                    }) // END of Ajax method
                $('#id_username').val('')
                $("#id_email").val('')
                $("#id_password1").val('')
                $("#id_password2").val('')
            }) // End of submit event

    }) // End of document ready function