$(document).ready(function() {
  $.ajaxSetup({
             beforeSend: function(xhr, settings) {
                 function getCookie(name) {
                     var cookieValue = null;
                     if (document.cookie && document.cookie != '') {
                         var cookies = document.cookie.split(';');
                         for (var i = 0; i < cookies.length; i++) {
                             var cookie = jQuery.trim(cookies[i]);
                             // Does this cookie string begin with the name we want?
                         if (cookie.substring(0, name.length + 1) == (name + '=')) {
                             cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                             break;
                         }
                     }
                 }
                 return cookieValue;
                 }
                 if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
                     // Only send the token to relative URLs i.e. locally.
                     xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
                 }
             }
        });
    // datepicker settings
    $('#id_due_date').datepicker({
        format: "yyyy-mm-dd",
    });

    $('.0').attr('bgcolor', '#CCFF99');
    $('.1').attr('bgcolor', '#FFFF66');
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
        var str = $(this).text();
        var due = Date.parse(str);
        var today = Date.parse('today');
        console.log(due);
        if (due.getFullYear() < today.getFullYear()){
          $(this).closest('tr').attr('bgcolor', '#FF5959');
        }
        else if(due.getFullYear() == today.getFullYear()){
          if (due.getMonth() < today.getMonth()){
            $(this).closest('tr').attr('bgcolor', '#FF5959');
          }
          else if(due.getMonth() == today.getMonth()){
            if (due.getDate() < today.getDate()){
              $(this).closest('tr').attr('bgcolor', '#FF5959');
            }
          }
        }
    });

    $('.status').change(function(){
      task_id = $(this).closest('tr').attr('id');;
      console.log(task_id);
      status = $(this).val();
      console.log(status);
      $.ajax({
                type:"POST",
                url:"/task/update/",
                data : { id : task_id , status: status},
                traditional : true,
                datatype : 'html',
                success: function(){
                    if(status == 0)
                      $('#'+task_id).attr('bgcolor', '#CCFF99');
                    else if (status == 1)
                      $('#'+task_id).attr('bgcolor', '#FFFF66');
                    else
                      $('#'+task_id).attr('bgcolor', '#99FFCC');
                    $('#'+task_id).attr('class', status);
                    console.log('task updated');
                }
            });
    });

    $('.status').change(function(){
      task_id = $(this).closest('tr').attr('id');;
      console.log(task_id);
      status = $(this).val();
      console.log(status);
      $.ajax({
                type:"POST",
                url:"/task/update/",
                data : { id : task_id , status: status},
                traditional : true,
                datatype : 'html',
                success: function(){
                    if(status == 0)
                      $('#'+task_id).attr('bgcolor', '#CCFF99');
                    else if (status == 1)
                      $('#'+task_id).attr('bgcolor', '#FFFF66');
                    else
                      $('#'+task_id).attr('bgcolor', '#99FFCC');
                    $('#'+task_id).attr('class', status);
                    console.log('task updated');
                }
            });
    });

    $('.priority').change(function(){
      task_id = $(this).closest('tr').attr('id');;
      console.log(task_id);
      priority = $(this).val();
      console.log(status);
      $.ajax({
                type:"POST",
                url:"/task/update/",
                data : { id : task_id , priority: priority},
                traditional : true,
                datatype : 'html',
                success: function(){
                    console.log('task updated');
                }
            });
    });

    $('.delete').click(function(){
      task_id = $(this).closest('tr').attr('id');;
      console.log(task_id);
      $.ajax({
                type:"POST",
                url:"/task/delete/",
                data : { id : task_id},
                traditional : true,
                datatype : 'html',
                success: function(){
                    $('#'+task_id).remove();
                    console.log('task deleted');
                }
            });
    });

});
