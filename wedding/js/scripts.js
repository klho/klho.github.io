function gallery(data) {
 for (i = 0; i < data.length; ++i) {
  var id = "gallery-" + data[i].id;
  var bgimg = "background-image: url(img/gallery/thumbs/" + data[i].id + ".jpg);";
  var bgpos = "background-position: " + data[i].pos + ";"
  var img = "img/gallery/" + data[i].id + ".jpg";
  document.write('' +
'<li>' +
' <a class="thumblink" href="#' + id + '" style="' + bgimg + ' ' + bgpos + '"></a>' +
' <a id="' + id + '" class="lightbox" href="#_">' +
'  <img src="' + img + '" alt="' + data[i].caption + '" />' +
'  <div class="caption">' + data[i].caption + '</div>' +
' </a>' +
'</li>');
 }
}
