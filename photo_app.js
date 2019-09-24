var canvas = document.getElementById("c1");
var image = null;

function loadImage(){

  var fileinput = document.getElementById("img");
  image = new SimpleImage(fileinput);
  image.drawTo(canvas);
  if (image != null){
    alert("Image uploaded successfully");
  }
}

function filter1(){

  var filt = document.getElementById("img");
  var filtered = new SimpleImage(filt);

  for (var pix of filtered.values()){
    var x = pix.getRed();
    var y = pix.getBlue();
    pix.setRed(0.9 * x);
    pix.setBlue(0.55 * y);
  }
  filtered.drawTo(canvas);
}

function grayScale(){

  var gy = document.getElementById("img");
  var grayImage = new SimpleImage(gy);

  for (var pixel of grayImage.values()){
    var val =((pixel.getRed()+pixel.getBlue()+pixel.getGreen())/3);
    pixel.setRed(val);
    pixel.setBlue(val);
    pixel.setGreen(val);
    }
  grayImage.drawTo(canvas);
}

function clearScreen(){
  var c1 = document.getElementById("c1");
  var ctx = c1.getContext("2d");
  ctx.clearRect(0,0,c1.width,c1.height);
}

function resetImg(){
  var fff = document.getElementById("img");
  var immg = new SimpleImage(fff);
  immg.drawTo(canvas);
}
