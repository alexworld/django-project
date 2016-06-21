function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);

            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

$(function() {
    $.ajaxSetup({
        headers: { "X-CSRFToken": getCookie("csrftoken") }
    });
});

$(document).ready(function() {
    $('.login').click(function(event) {
        event.preventDefault();
        console.log("form submitted");
        console.log($(this).attr('action'));
        console.log($(this).attr('method'));
        console.log($("#login_form").serialize());
        
        $.ajax({
            url: $(this).attr('action'),
            method: $(this).attr('method'),
            data: $("#login_form").serialize(),

            success: function(msg) {
                console.log('LOL');
                document.write(msg);
//                $("#blog-nav").load(location.href + " #blog-nav");
            }
        });
    });
});

$(document).ready(function() {
    $('.register').click(function(event) {
        event.preventDefault();
        console.log("form submitted");
        console.log($(this).attr('action'));
        console.log($(this).attr('method'));
        console.log($("#register_form").serialize());
        
        $.ajax({
            url: $(this).attr('action'),
            method: $(this).attr('method'),
            data: $("#register_form").serialize(),

            success: function(msg) {
                console.log('LOL');
                document.write(msg);
//                $("#blog-nav").load(location.href + " #blog-nav");
            }
        });
    });
});

$(document).ready(function() {
    $('.logout').click(function(event) {
        event.preventDefault();
        console.log("form submitted");
        console.log($(this).attr('action'));
        console.log($(this).attr('method'));
        
        $.ajax({
            url: $(this).attr('action'),
            method: $(this).attr('method'),

            success: function(msg) {
                console.log('LOL');
                window.location = document.location.origin;
//                $("#blog-nav").load(location.href + " #blog-nav");
            }
        });
    });
});

$(document).ready(function() {
    $('.plus').click(function(event) {
        event.preventDefault();
        console.log("form submitted");
        console.log($(this).attr('action'));
        console.log($(this).attr('method'));
        console.log($(this).attr('object'));
        console.log($(this).attr('plus'));
        
        $.ajax({
            url: $(this).attr('action'),
            method: $(this).attr('method'),
            data: {object: $(this).attr('object'), plus: $(this).attr('plus')},

            success: function(msg) {
                window.location = document.location;
            }
        });
    });
});

$(document).ready(function() {
    $('.create_post').click(function(event) {
        event.preventDefault();
        console.log("form submitted");
        console.log($(this).attr('action'));
        console.log($(this).attr('method'));
        console.log($("#post_form").serialize());
        
        $.ajax({
            url: $(this).attr('action'),
            method: $(this).attr('method'),
            data: $("#post_form").serialize(),

            success: function(msg) {
                console.log('LOL');
                window.location = document.location.origin;
//                $("#blog-nav").load(location.href + " #blog-nav");
            }
        });
    });
});

$(document).ready(function() {
    $('.edit_post').click(function(event) {
        event.preventDefault();
        console.log("form submitted");
        console.log($(this).attr('action'));
        console.log($(this).attr('method'));
        console.log($("#post_form").serialize());
        
        $.ajax({
            url: $(this).attr('action'),
            method: $(this).attr('method'),
            data: $("#post_form").serialize(),

            success: function(msg) {
                console.log('LOL');
                window.location = '../';
//                $("#blog-nav").load(location.href + " #blog-nav");
            }
        });
    });
});


$(document).ready(function() {
    $('.create_comment').click(function(event) {
        event.preventDefault();
        console.log("form submitted");
        console.log($(this).attr('action'));
        console.log($(this).attr('method'));
        console.log($("#comment_form").serialize());
        
        $.ajax({
            url: $(this).attr('action'),
            method: $(this).attr('method'),
            data: $("#comment_form").serialize(),

            success: function(msg) {
                console.log('LOL');
                window.location.href = '../';
//                $("#blog-nav").load(location.href + " #blog-nav");
            }
        });
    });
});

$(document).ready(function() {
    $('.edit_comment').click(function(event) {
        event.preventDefault();
        console.log("form submitted");
        console.log($(this).attr('action'));
        console.log($(this).attr('method'));
        console.log($("#comment_form").serialize());
        
        $.ajax({
            url: $(this).attr('action'),
            method: $(this).attr('method'),
            data: $("#comment_form").serialize(),

            success: function(msg) {
                console.log('LOL');
                window.location.href = "../../";
//                $("#blog-nav").load(location.href + " #blog-nav");
            }
        });
    });
});
