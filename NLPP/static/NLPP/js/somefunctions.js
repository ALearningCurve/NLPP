      



//what happens when you hit a word

var hit_word = restorable(hit_text_node, function(node) {
        var hw = '';

        function getHitText(node, parent_font_style) {
          log("getHitText: '" + node.textContent + "'");

          if (XRegExp(word_re).test( node.textContent )) {
            $(node).replaceWith(function() {
                return this.textContent.replace(XRegExp("^(.{"+Math.round( node.textContent.length/2 )+"}\\p{L}*)(.*)", 's'), function($0, $1, $2) {
                    return '<transblock>'+escape_html($1)+'</transblock><transblock>'+escape_html($2)+'</transblock>';
                });
            });

            $('transblock').css(parent_font_style);

            var next_node = document.elementFromPoint(e.clientX, e.clientY).childNodes[0];

            if (next_node.textContent == node.textContent) {
              return next_node;
            }
            else {
              return getHitText(next_node, parent_font_style);
            }
          }
          else {
            return null;
          }
        }

//actually translating the word

function translate(word, sl, tl, last_translation, onresponse, sendResponse) {
  var options = {
    url: "https://translate.google.com/translate_a/t",
    data: {
      q: word,
      sl: sl,
      tl: tl,
      ie: 'UTF8',
      oe: 'UTF8'
   };

  if (/\s/.test(word)) {
    $.extend(options, {
        accepts: '*/*',
        dataType: 'text',
        success: function on_success(data) {
          onresponse(eval(data), word, sl, tl, last_translation, sendResponse, ga_event_name);
        }
    });

