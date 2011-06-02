// Main js code for index.html

// Validation for IE6 - Redirect to error page if browser is IE6.
if ($.browser.msie && /^6/.test($.browser.version)) { 
    // Redirect any page to error.html. No redirects for error.html
    if (!/ieError$/.test(window.location)) {
        window.location = "/defiance/default/ieError";
    }
}


// Invoke ajax call when src is clicked.
function ajaxQuery(src, evt) {
    $('.here').removeClass('here');
    $('#menu a[href="' + src.attr('href') + '"]').addClass("here");
    query = '' + encodeURIComponent('ajax') + '=' + encodeURIComponent(1);
    $.ajax({type: 'POST', url: src.attr('href'), data: query, success: function(msg) { 
        document.getElementById('content').innerHTML = msg; 
        init(); 
        } 
    });  
}


// Init function common for all pages.
function init() {
    $('.rounded').corner(); // Invokes jquery rounded corner plug-in.
    // Set ajax handlers for anchors.
    $('a.ajax').click(function(evt) {
        ajaxQuery($(this), evt);
        return false;
    });
}

// On page load, set ajax handlers for menu items.
$(function() {
    $('#menu a').click(function(evt) {
        ajaxQuery($(this), evt);
        return false;
    });
});

