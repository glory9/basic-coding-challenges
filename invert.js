// color inverts the image

var photo = new SimpleImage("hippieflower.jpg");
photo.setSize(232,160);
print(photo);

function swapRedGreen(p) {
    var a = p.getRed();
    var b = p.getGreen();
    p.setGreen(a);
    p.setRed(b);
}
for (var pix of photo.values()) {
    swapRedGreen(pix);
}

print(photo);
