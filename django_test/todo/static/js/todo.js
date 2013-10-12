var handle_toggle = function ( elements, id_index ) {
    id_index = id_index || 3;
    // Toggle the strikout css on the text when we change the checkbox.
    elements.change( function () {
        // Grab the required variables.
        var id = String($(this).attr('id').slice(id_index));
        var csrf_token = $('#csrf-token').html();
        var kwargs = {'csrfmiddlewaretoken': csrf_token,
                      'task_pk': id};
        // Send the toggle command.
        $.post("/todo/toggle/", kwargs, function (data, textStatus, header){
                var statusCode = header.status.toString();
                if(statusCode == '200'){
                   // success, cross out the text and reveal the close box. 
                   $('#'+id).toggleClass("done");
                } // try to catch errors.
                else if(statusCode == '403')
                    alert("Error: you are not allowed to modify this task.");
                else if(statusCode == '400')
                    alert("Error: there was an internal error trying to find this task.")
                else
                    alert("Error: for an unknown reason the update failed");
        });
        
    });
};

var handle_delete = function ( elements, id_index ) {
    id_index = id_index || 6;
    // delete and hide the list item when we click the delete "button"
    elements.click( function() {
        // Grab the required variables.
        var id = $(this).attr('id').slice(id_index);
        var csrf_token = $('#csrf-token').html();
        var kwargs = {'csrfmiddlewaretoken': csrf_token,
                      'task_pk': id};
        // Send the delete command.                  
        $.post('/todo/delete/', kwargs, function (data, textStatus, header) {
                var statusCode = header.status.toString();
                if(statusCode == '200'){
                    // Success, hide the task row. 
                    $('#'+id).fadeOut();
                } // Try to catch errors.
                else if(statusCode == '403')
                    alert("Error: you are not allowed to delete this task.");
                else if(statusCode == '400')
                    alert("Error: there was an internal error trying to find this task.")
                else
                    alert("Error: for an unknown reason the delete failed");
        });
     
        
    });
};

$(document).ready(function () {
  
    handle_toggle($('.toggle'));  
      
    handle_delete($('.delete'));
    
    $('#newtask').submit( function() {
        // Stop the default form submission.
        event.preventDefault();
        // Grab required variables.
        var csrf_token = $('#csrf-token').html();
        var text = $("#newtext").val();
        var kwargs = {'csrfmiddlewaretoken': csrf_token,
                      'task': text};
        // Send the create command.
        $.post('/todo/create/', kwargs, function (data, textStatus, header){
            var statusCode = header.status.toString();
            if(statusCode == '200'){
                // reset the form
                $('#newtask')[0].reset();
                // create a new task row
                var newtask = '<li id="'+data+'">';
                newtask = newtask + '<input class="toggle" id="box'+data+'" type="checkbox"/> ';
                newtask = newtask + '<label class="tasktext" for="box'+data+'" id="text'+data+'">'+text+'</label>';
                newtask = newtask + '<span class="delete" id="delete'+data+'">X</span>';
                newtask = newtask + '</li>';
                // add task to the list, we put it at the top, immediately after
                // the newtask form.
                $('#newtask').after(newtask);
                // Because we use after, the task is $('#newtask').next(),
                // grab the corresponding checkbox and delete box.
                var t = $('#newtask').next();
                var checkbox = t.children('.toggle');
                var deletebox = t.children('.delete');
                
                // attach the toggle and delete listener
                handle_toggle(checkbox);
                handle_delete(deletebox);
            } // Catch errors.
            else 
                alert("Error: the new task was not saved, please try again.");
            
        });
    });
    
});
