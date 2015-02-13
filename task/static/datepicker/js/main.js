/**
* Returns the week number for this date. dowOffset is the day of week the week
* "starts" on for your locale - it can be from 0 to 6. If dowOffset is 1 (Monday),
* the week returned is the ISO 8601 week number.
* @param int dowOffset
* @return int
*/
Date.prototype.getWeek = function (dowOffset) {
/*getWeek() was developed by Nick Baicoianu at MeanFreePath: http://www.epoch-calendar.com */

dowOffset = typeof(dowOffset) == 'int' ? dowOffset : 0; //default dowOffset to zero
var newYear = new Date(this.getFullYear(),0,1);
var day = newYear.getDay() - dowOffset; //the day of week the year begins on
day = (day >= 0 ? day : day + 7);
var daynum = Math.floor((this.getTime() - newYear.getTime() -
(this.getTimezoneOffset()-newYear.getTimezoneOffset())*60000)/86400000) + 1;
var weeknum;
//if the year starts before the middle of a week
if(day < 4) {
weeknum = Math.floor((daynum+day-1)/7) + 1;
if(weeknum > 52) {
nYear = new Date(this.getFullYear() + 1,0,1);
nday = nYear.getDay() - dowOffset;
nday = nday >= 0 ? nday : nday + 7;
/*if the next year starts before the middle of
the week, it is week #1 of that year*/
weeknum = nday < 4 ? 1 : 53;
}
}
else {
weeknum = Math.floor((daynum+day-1)/7);
}
return weeknum;
};



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

    $('.spacing').click(function() {
      var time = $(this).text()
      console.log(time);
      $('.due_date').each(function(index, val){
        var str = $(this).text();
        var due = Date.parse(str);
        var today = Date.parse('today');
        if (due.getFullYear() == today.getFullYear()){
          // console.log('Year');
          if (time=="Month"){
            console.log('Month');
            if (due.getMonth() != today.getMonth()){
              $(this).closest('tr').css('display', 'None');
            }
            else{
              $(this).closest('tr').css('display', 'table-row'); 
            }
          }
          else if(time == "Week"){
            console.log('Week');
            if (due.getMonth() == today.getMonth()){
              if(due.getWeek() != today.getWeek()){
                $(this).closest('tr').css('display', 'None');
              }
              else{
                $(this).closest('tr').css('display', 'table-row'); 
              }
            }
            else{
              $(this).closest('tr').css('display', 'None');
            }
          }
          else if(time == "Day"){
            console.log('Day');
            if (due.getMonth() == today.getMonth()){
              if (due.getDate() != today.getDate()){
                $(this).closest('tr').css('display', 'None');
              }
              else{
                $(this).closest('tr').css('display', 'table-row'); 
              }
            }
            else{
              $(this).closest('tr').css('display', 'None');
            }
          }
          else if(time == "All"){
            $(this).closest('tr').css('display', 'table-row'); 
          }
        }
        else {
          $(this).closest('tr').css('display', 'None');
        }
      });
    });
});
