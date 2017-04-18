
$(document).ready(function() {
    console.log("loaded");
    $.material.init();

    $(document).on("submit", "#register-form", function(e) {
        e.preventDefault();

        var form = $('#register-form').serialize();
        $.ajax({
            url: '/post-registration',
            type: 'POST',
            data: form,
            success: function(response) {
                console.log(response);
            }
        });
    });


    $(document).on('submit', '#login-form', function(e) {
        e.preventDefault();

        var form = $(this).serialize();
        $.ajax({
            url: '/check-login',
            type: 'POST',
            data: form,
            success: function(response) {
                if(response == "error") {
                    alert("Could not log in.");
                } else {
                    console.log("Logged in as", response);
                    window.location.href = "/";
                }
            }
        });
    });


    $(document).on('click', '#logout-link', function(e) {
        e.preventDefault();

        $.ajax({
            url: '/logout',
            type: 'GET',
            success: function(response) {
                if(response == "logout successful") {
                    window.location.href = "/";
                } else {
                    alert("Something went wrong.");
                }
            }
        })
    });
});

