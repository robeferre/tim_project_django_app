$(document).ready(function() {

    $('.remove-button').click(function() { // catch the form's submit event

        var id = $(this).attr('id');

        $.ajax({ // create an AJAX call...

            type: "POST",
            url: "/ajax/delete_doc/",
            data: {'id':id },


            success: function(success) { // on success..

                if (success=='true'){

                    location.reload();

                }
                else{

                    alert("Não foi possível deletar o documento pois o usuário logado não é o proprietário!")

                }


            }
        });

        return false;
    });

});
