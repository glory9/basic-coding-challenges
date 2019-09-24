var canvas = document.getElementById("c1");
var image = null;
var filtered;
var grayImage;
var crimson;
var colorful;

function loadImage(){

  var fileinput = document.getElementById("img");
  image = new SimpleImage(fileinput);
  colorful = new SimpleImage(fileinput);
  crimson = new SimpleImage(fileinput);
  filtered = new SimpleImage(fileinput);
  grayImage = new SimpleImage(fileinput);
  image.drawTo(canvas);
  if (image != null){
    alert("Image loaded successfully");
  }
}

function filter1(){

  clearScreen();

  for (var pix of filtered.values()){
    var x = pix.getRed();
    var y = pix.getBlue();
    pix.setRed(0.9 * x);
    pix.setBlue(0.55 * y);
  }
  filtered.drawTo(canvas);
}

function grayScale(){

  clearScreen();

  for (var pixel of grayImage.values()){
    var val =((pixel.getRed()+pixel.getBlue()+pixel.getGreen())/3);
    pixel.setRed(val);
    pixel.setBlue(val);
    pixel.setGreen(val);
    }
  grayImage.drawTo(canvas);
}

function doCrimson(){

  clearScreen();

  for (var pix of crimson.values()){

    pix.setRed(215);
  }
  crimson.drawTo(canvas);
}

function doColorful(){
  clearScreen();

  var key = colorful.getWidth()
  
  for (var pix of colorful.values()){

    if (pix.getX() <= key/4){
      pix.setRed(200);
    }
    else if (pix.getX() <= key/2){
      pix.setBlue(155);
    }
    else if (pix.getX() <= (key * 0.75)){
      pix.setGreen(205);
      pix.setBlue(150);
    }
    else {
      pix.setGreen(150);
    }
  }

  colorful.drawTo(canvas);
}

function clearScreen(){
  var c1 = document.getElementById("c1");
  var ctx = c1.getContext("2d");
  ctx.clearRect(0,0,c1.width,c1.height);
}

function resetImg(){
  clearScreen();
  var fff = document.getElementById("img");
  var immg = new SimpleImage(fff);
  immg.drawTo(canvas);
}
