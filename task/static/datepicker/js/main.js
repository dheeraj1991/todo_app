$(document).ready(function() {
    // datepicker settings
    $('#id_due_date').datepicker({
        format: "yyyy-mm-dd",
    });

    $('.0').attr('bgcolor', '#CCFF99');
    $('.1').attr('bgcolor', '#CCFF99');
    $('.2').attr('bgcolor', '#99FFCC');

    $('#add_task').click(function(){
      $('#banner_list').css('display','none');
      $('#banner_add').css('display','inline');
    });

    $('#cancel').click(function(){
      $('#banner_list').css('display','inline');
      $('#banner_add').css('display','none');
    });

    $('.due_date').each(function(index, val) {
        var date = $.datepicker.$.parseDate("M. d, yy", $(this).text());
        console.log(date);
    });
});
function no_task(){
      $('#banner_list').css('display','none');
      $('#banner_add').css('display','inline');
}