(function(){
  var desktop=matchMedia('(hover:hover) and (pointer:fine) and (forced-colors:none)');
  var root=document.documentElement;
  var canvas=document.createElement('canvas');
  canvas.width=canvas.height=1;
  var context=canvas.getContext('2d',{willReadFrequently:true});
  if(!context)return;

  function cursorImage(color,ring){
    var dot='<circle cx="12" cy="12" r="5.5" fill="'+color+'"/>';
    var outline=ring?'<circle cx="12" cy="12" r="8.5" fill="none" stroke="'+color+'" stroke-width="1.5"/>':'';
    var svg='<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24">'+dot+outline+'</svg>';
    return 'url("data:image/svg+xml,'+encodeURIComponent(svg)+'") 12 12,'+(ring?'pointer':'auto');
  }

  function luminance(rgb){
    var weights=[.2126,.7152,.0722];
    return weights.reduce(function(total,weight,index){
      var channel=rgb[index]/255;
      return total+weight*(channel<=.04045?channel/12.92:Math.pow((channel+.055)/1.055,2.4));
    },0);
  }

  var palette=['#DC4A36','#171717','#FFFFFF'].map(function(color){
    var rgb=color.slice(1).match(/../g).map(function(channel){return parseInt(channel,16)});
    return {dot:cursorImage(color,false),ring:cursorImage(color,true),light:luminance(rgb)};
  });
  var current;
  function show(choice){
    if(choice===current)return;
    current=choice;
    root.style.setProperty('--cursor-dot',choice.dot);
    root.style.setProperty('--cursor-ring',choice.ring);
  }

  function paint(color){
    context.fillStyle='transparent';
    context.fillStyle=color;
    context.fillRect(0,0,1,1);
  }

  function surface(node){
    context.clearRect(0,0,1,1);
    // Composite solid surfaces from the pointer target back to the page.
    context.globalCompositeOperation='destination-over';
    if(node.matches('svg :is(circle,ellipse,path,polygon,rect,text)')){
      var fill=getComputedStyle(node);
      if(fill.fill!=='none'&&fill.fillOpacity==='1')paint(fill.fill);
    }
    for(var element=node;element;element=element.parentElement){
      var color=getComputedStyle(element).backgroundColor;
      paint(color);
      if(/^rgb\(/.test(color))break;
    }
    paint('white');
    return luminance(context.getImageData(0,0,1,1).data);
  }

  function contrast(a,b){
    return (Math.max(a,b)+.05)/(Math.min(a,b)+.05);
  }

  var target,frame;
  function update(){
    frame=0;
    if(!desktop.matches||!target.isConnected)return;
    var background=surface(target);
    var red=palette[0],black=palette[1],white=palette[2];
    var alternate=contrast(black.light,background)>contrast(white.light,background)?black:white;
    show(contrast(red.light,background)>=2.5?red:alternate);
  }

  function track(event){
    if(!desktop.matches||event.pointerType!=='mouse'||!(event.target instanceof Element))return;
    target=event.target;
    if(!frame)frame=requestAnimationFrame(update);
  }

  if(desktop.matches)show(palette[0]);
  document.addEventListener('pointermove',track,{passive:true});
})();
