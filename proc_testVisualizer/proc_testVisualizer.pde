/* [Memo]
- https://processing.org/reference/libraries/sound/SoundFile.html
- https://drive.google.com/file/d/0BzyVHU69QO3mdkp0NFF4NlV4TEk/view
*/

import processing.sound.*;

boolean status = false; // Now status
boolean before = true; // Before status
PImage closeImg, openImg;
SoundFile hi, bye;

void setup(){
  size(1300, 700);
  noStroke();
  setBack();
  closeImg = loadImage("door_close.png");
  openImg = loadImage("door_open.png");
  hi = new SoundFile(this, "/Users/tkoyama/Works/kokasai17/proc_testVisualizer/door_hello.wav");
  bye = new SoundFile(this, "/Users/tkoyama/Works/kokasai17/proc_testVisualizer/door_close.wav");
}

void setBack(){
  background(#cccccc);
}

void draw(){
  
  if(mousePressed){
    status = true;
  }else{
    status = false;
  }
  
  if(status && !before){ // open
    before=true;
    setBack();
    image(openImg, 200, 0);
    hi.play();
  }else if(!status && before){ // close
    before=false;
    setBack();
    image(closeImg, 200, 0);
    bye.play();
  }
}