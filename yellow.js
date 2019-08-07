//changes the non-white pixels to yellow

var duke = new SimpleImage("duke_blue_devil.png");

for (var dot of duke.values()){
    if (dot.getBlue() == 255) {
    }

    else {
        dot.setRed(255);
        dot.setBlue(0);
        dot.setGreen(255);
    }
}

print(duke);
