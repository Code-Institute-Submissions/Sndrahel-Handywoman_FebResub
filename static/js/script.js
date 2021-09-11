$(document).ready(function () {
    
    /* Message Alert fade-out */
    $(".alert").delay(3000).slideUp(200, function () {
        $(this).alert('close');
    });

    setTimeout(function () {
        let messages = document.getElementById('msg');
        let alert = new bootstrap.Alert(messages);
        alert.close();
    }, 2500);

});