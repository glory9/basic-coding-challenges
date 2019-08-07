//this program creates an image with 4 differently colored quadrants and puts it in a frame
var image =new SimpleImage(200,200);

for (var pixel of image.values()) {
    var a = pixel.getX();
    var b = pixel.getY();

    if (a <= image.getWidth()/2) {
        pixel.setRed(255);
    }
    if (b >= image.getHeight()/2) {
        pixel.setBlue(255);
    }
    else if ( a > image.getWidth()/2) {
        pixel.setGreen(255);
    }
}


function setBlack(p) {
    p.setBlue(0);
    p.setRed(0);
    p.setGreen(0);
}

function addBorder(immg, borThick) {

    for (var pix of immg.values()) {
        if (pix.getY() < borThick) {
            setBlack(pix);
        }
        if (pix.getY() >= immg.getHeight()- borThick) {
            setBlack(pix);
        }
        if (pix.getX() < borThick) {
            setBlack(pix);
        }
        if (pix.getX() >= immg.getWidth()- borThick) {
            setBlack(pix);
        }

    }
}

addBorder(image, 7);
print(image);
