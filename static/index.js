
$(document).ready(function () {

    alert("BLERP");

    $(".nora-intro").hide();
    $("#nora-nora").hide();
    

    $(".nora-intro").fadeIn(4000, function() {
        // Animation complete
    });
    $("#nora-nora").fadeIn(4000, function() {
        // Animation complete
    });

    $.ajax({
        method: "GET",
        url: "http://cbf1bcba.ngrok.io/getUserData",
        datatype: "json"
    })
    .done(function( msg ) {
        parsedData = JSON.parse(msg);
        updatePictures(parsedData);
    });


    $('body').on('click','td img', function () {
        var clickedUrl = $(this).attr("src");

        $.ajax({
            method: "POST",
            url: "http://cbf1bcba.ngrok.io/bankAnalytics",
            datatype: "json",
            data: { phone: "+19084774708", url : clickedUrl} ,
        }).done(function(data) {
            var pData = JSON.parse(data);
            
            var content = $('.modal-content');
            content.append("<img src="+clickedUrl+"/>");
            
        });
    });
});


function updatePictures(parsedData) {
    var items = parsedData.items;

    for (i in items) {
        var imageURL = items[i].image;
        
        if ($('.images').children().last().children().size() == 3) {
            $('.images').append("<tr></tr>");
        }

        $('.images').children().last().append("<td><img class=\"img-responsive img-thumbnail\" data-toggle=\"modal\" data-target=\".bs-example-modal-lg\"src="+imageURL+"></td>");
    }
}