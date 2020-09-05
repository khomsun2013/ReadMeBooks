import os


import sys
from xml.etree import ElementTree as ET

chrs='F'

f = open("part1.txt", "w")
for file in os.listdir("./static/"+chrs):
    if file.endswith(".png"):
    	div = ET.Element('div', attrib={'class': 'mySlides'})
    	img = ET.Element('img', attrib={'src':'{{ url_for(\'static\',filename=\''+chrs+'/'+str(file)+'\') }}','class': 'center','style':'width:25%'})
    	div.append(img)
    	ET.ElementTree(div).write(f, encoding='unicode',method='html')
tail='''
    <a class="prev" onclick="plusSlides(-1)">❮</a>
    <a class="next" onclick="plusSlides(1)">❯</a>
    <div class="caption-container">
    <p id="caption"></p>
    </div>
    '''
f.write(tail)
f.close

cnt=0
f1 = open("part2.txt", "w")
for file in os.listdir("./static/"+chrs):
    if file.endswith(".png"):
      cnt+=1
      div = ET.Element('div', attrib={'class': 'column'})
      img = ET.Element('img', attrib={'src':'{{ url_for(\'static\',filename=\''+chrs+'/'+str(file)+'\') }}','class': 'demo cursor','style':'width:100%','onclick':'currentSlide({})'.format(cnt),'alt':str(file[2:-4])})
      div.append(img)
      print(cnt,str(file))
      ET.ElementTree(div).write(f1, encoding='unicode',method='html')
tail1='''
</div>

<script>
var slideIndex = 1;
showSlides(slideIndex);

function plusSlides(n) {
  showSlides(slideIndex += n);
}

function currentSlide(n) {
  showSlides(slideIndex = n);
}

function showSlides(n) {
  var i;
  var slides = document.getElementsByClassName("mySlides");
  var dots = document.getElementsByClassName("demo");
  var captionText = document.getElementById("caption");
  if (n > slides.length) {slideIndex = 1}
  if (n < 1) {slideIndex = slides.length}
  for (i = 0; i < slides.length; i++) {
      slides[i].style.display = "none";
  }
  for (i = 0; i < dots.length; i++) {
      dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[slideIndex-1].style.display = "block";
  dots[slideIndex-1].className += " active";
  captionText.innerHTML = dots[slideIndex-1].alt;
}
</script>

</body>
</html>
'''
f1.write(tail1)
f1.close


filenames = ['part0.txt', 'part1.txt', 'part2.txt']
with open('./templates/'+chrs+'.html', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)

 #   <img src={{ url_for("static",filename='img7.jpg') }}" class='center'>
 #   </div>'