var mousePressed = false;
var lastX, lastY;
var ctx;

function getRndInteger(min, max) {
return Math.floor(Math.random() * (max - min) ) + min;
}

function InitThis(word,len) {
  aleatorio = word;
  document.getElementById('mensaje').innerHTML  = "Traduce y escribe la palabra " + aleatorio + " en Hiragana";
  
  var id0 = 'myCanvas_0'; 
  $('#'+id0).mousedown(function (e) {
    ctx = document.getElementById(id0).getContext("2d");
    mousePressed = true;
    Draw(e.pageX - $(this).offset().left, e.pageY - $(this).offset().top, false);
  });

  $('#'+id0).mousemove(function (e) {
    ctx = document.getElementById(id0).getContext("2d");
    if (mousePressed) {
        Draw(e.pageX - $(this).offset().left, e.pageY - $(this).offset().top,true);
    }
  });

  $('#'+id0).mouseup(function (e) {    
    mousePressed = false;
  });
  $('#'+id0).mouseleave(function (e) {
    mousePressed = false;
  });

  var id1 = 'myCanvas_1'; 
  $('#'+id1).mousedown(function (e) {
    ctx = document.getElementById(id1).getContext("2d");
    mousePressed = true;
    Draw(e.pageX - $(this).offset().left, e.pageY - $(this).offset().top, false);
  });

  $('#'+id1).mousemove(function (e) {
    ctx = document.getElementById(id1).getContext("2d");
    if (mousePressed) {
        Draw(e.pageX - $(this).offset().left, e.pageY - $(this).offset().top,true);
    }
  });

  $('#'+id1).mouseup(function (e) {    
    mousePressed = false;
  });
  $('#'+id1).mouseleave(function (e) {
    mousePressed = false;
  });

  var id2 = 'myCanvas_2'; 
  $('#'+id2).mousedown(function (e) {
    ctx = document.getElementById(id2).getContext("2d");
    mousePressed = true;
    Draw(e.pageX - $(this).offset().left, e.pageY - $(this).offset().top, false);
  });

  $('#'+id2).mousemove(function (e) {
    ctx = document.getElementById(id2).getContext("2d");
    if (mousePressed) {
        Draw(e.pageX - $(this).offset().left, e.pageY - $(this).offset().top,true);
    }
  });

  $('#'+id2).mouseup(function (e) {    
    mousePressed = false;
  });
  $('#'+id2).mouseleave(function (e) {
    mousePressed = false;
  });

  var id3 = 'myCanvas_3'; 
  $('#'+id3).mousedown(function (e) {
    ctx = document.getElementById(id3).getContext("2d");
    mousePressed = true;
    Draw(e.pageX - $(this).offset().left, e.pageY - $(this).offset().top, false);
  });

  $('#'+id3).mousemove(function (e) {
    ctx = document.getElementById(id3).getContext("2d");
    if (mousePressed) {
        Draw(e.pageX - $(this).offset().left, e.pageY - $(this).offset().top,true);
    }
  });

  $('#'+id3).mouseup(function (e) {    
    mousePressed = false;
  });
  $('#'+id3).mouseleave(function (e) {
    mousePressed = false;
  });
}
function Draw(x, y, isDown) {
  if (isDown) {
      ctx.beginPath();
      ctx.strokeStyle = 'black';
      ctx.lineWidth = 11;
      ctx.lineJoin = "round";
      ctx.moveTo(lastX, lastY);
      ctx.lineTo(x, y);
      ctx.closePath();
      ctx.stroke();
  }
  lastX = x; lastY = y;
}

function clearArea(len) {
  for (var i = 0; i < len; i++) {
    ctx = document.getElementById("myCanvas_"+i).getContext("2d");
    ctx.setTransform(1, 0, 0, 1, 0, 0);
    ctx.clearRect(0, 0, ctx.canvas.width, ctx.canvas.height);
  }
}

function prepareImg(len) {
  for (var i = 0; i < len; i++) {
    var canvas = document.getElementById("myCanvas_"+i);
    document.getElementById("myImage_"+i).value = canvas.toDataURL();
  }
}