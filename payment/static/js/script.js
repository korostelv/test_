
$(document).ready(function() {
        
    // $('th').click(function(){
    //     var table = $(this).parents('table').eq(0)
    //     var rows = table.find('tr:gt(0)').toArray().sort(comparer($(this).index()))
    //     this.asc = !this.asc
    //     if (!this.asc){rows = rows.reverse()}
    //     for (var i = 0; i < rows.length; i++){table.append(rows[i])}
    // })
    // function comparer(index) {
    //     return function(a, b) {
    //         var valA = getCellValue(a, index), valB = getCellValue(b, index)
    //         return $.isNumeric(valA) && $.isNumeric(valB) ? valA - valB : valA.toString().localeCompare(valB)
    //     }
    // }
    // function getCellValue(row, index){ return $(row).children('td').eq(index).text() }

    typePay = $('#type_pay');
    var t =$('th')
    console.log(t.eq(2))

    // $.ajax({
    //     type: "POST",
    //     url: "/sorted/" + postID + "/",
    //     data: {
    //         csrfmiddlewaretoken: '{{ csrf_token }}',
    //         post_id: postID
    //     },
    //     success: function(response) {
            // if (response.rating !== undefined) {
            //     $('.rating-count').html('<b>Рейтинг статьи: </b><span style="color: #006633;">'+response.rating+'</span>')
            // }
            // if (response.message !== undefined) {
            //     $('.message-rating').text(response.message)
            // }
        }
    });














});


