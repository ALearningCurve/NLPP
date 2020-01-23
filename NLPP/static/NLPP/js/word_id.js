function get_selection() {
    var txt = '';
    if (window.getSelection) {
        txt = window.getSelection();
    } else if (document.getSelection) {
        txt = document.getSelection();
    } else if (document.selection) {
        txt = document.selection.createRange().text;
    }

    return txt;
}

$(document).dblclick(function(e) {
    var t = get_selection();

    translate_api_call(t.toString());
});


function translate_api_call(p_text="hola", p_lang="es-en") {
  $.ajax({
        type: "POST",
        url: '{% url 'posts:translate' %}',
        data: {
						csrfmiddlewaretoken: '{{ csrf_token }}',
						text: p_text,
						lang: p_lang,
              },
        success:  function(response){
               alert(response);
           }
    });
}
