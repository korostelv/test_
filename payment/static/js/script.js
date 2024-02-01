
$(document).ready(function() {

   // Функция сортировки 
    var sortid = $('#sorted_val').val();
    $.ajax({
        type: 'POST',
        url: "/",
        dataType: 'html',
        data: {'sorted_val': sortid}
    })
        $('#table').html(data);
    });
 































