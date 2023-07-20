# templates
header = """<head>
<link rel="stylesheet" type="text/css" href="zenburn.css" />
</head>"""
body = """<body>
<h1 style="text-align: center;"> Nice Free Things </h1>
<hr>
<pre class="vert">

且取堂中木佛燒
特       ,  古
奇       o> 寺
何  \   /   天
利   <()    寒
舍    ||    度
無    ``    一
既          宵
飄飄雪冷風禁不

</pre>
"""
title = """<hr>
<h2 style="text-align:center;"> {} </h2>
<hr>"""
image_template = """<img class="slideshow-img {}" src="{}" alt={}>
"""
slideshow_head = """<div class="slideshow">
<a class="prev" onclick="plusSlides(-1, {})">&#10094;</a>
"""
slideshow_foot = """<a class="next" onclick="plusSlides(1, {})">&#10095;</a>
</div>"""

footer = """</body>
<style>
.vert {
font-family:monospace;
font-size:21px; 
letter-spacing:8px;
text-align:center;
}
.slideshow-img {
display:none;
margin-left:auto;
margin-right:auto;
margin-top:34px;
margin-bottom:34px;
max-width:100%;
}
.slideshow{
text-align:center;
position:relative;
}
.prev, .next {
  cursor: pointer;
  width: auto;
  color: var(--fg-white);
  font-weight: bold;
  font-size: 34px;
  border-radius: 0 3px 3px 0;
  user-select: none;
  position:absolute;
  top: 50%;
  transform: translate(0%,-50%);
}
.prev {
left: 0%;
}
.next {
  right: 0%;
  border-radius: 3px 0 0 3px;
}
.prev:hover, .next:hover {
  color: var(--green);
}
</style>
<script>
var slideIndices = [1, 1]
var i = 0;
while(true) {
  var slides = document.getElementsByClassName("slideshow-img "+i.toString());
  if(slides.length == 0) break;
  showSlides(1, i);
  i += 1;
}

// Next/previous controls
function plusSlides(n, r) {
  slideIndices[r] += n
  showSlides(slideIndices[r], r);
}

// Thumbnail image controls
function currentSlide(n, r) {
  slideIndices[r] = n
  showSlides(slideIndices[r], r);
}

function showSlides(n, r) {
  var i;
  var slides = document.getElementsByClassName("slideshow-img "+r.toString());
  if (n > slides.length) {slideIndices[r] = 1}
  if (n < 1) {slideIndices[r] = slides.length}
  for (i = 0; i < slides.length; i++) {
      slides[i].style.display = "none";
  }
  slides[slideIndices[r]-1].style.display = "block";
} 
</script>
"""
# generate gallery
import os
import csv
path = "./nfts/"
displays = path + "displays.csv"
with open(displays, "r") as f:
    reader = csv.reader(f)
    for rownum, row in enumerate(reader):
        body += title.format(row[0])
        image_dir = path + row[1] + "/"
        images = os.listdir(image_dir)
        body += slideshow_head.format(rownum)
        for i in images[::-1]:
            body += image_template.format(rownum, image_dir+i, i)
        body += slideshow_foot.format(rownum)
with open("gallery.html", "w+") as f:
    f.write(header)
    f.write(body)
    f.write(footer)
