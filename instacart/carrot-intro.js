/* Brand intro shared by the home card and case-study hero. */
(function(){
  window.jdInstacartIntro = async function(player, host){
    var overlay=host.querySelector('.carrot-intro');
    if(!overlay || matchMedia('(prefers-reduced-motion: reduce)').matches) return;
    var logo=overlay.querySelector('img'),animations=[],observer=null;
    await player.wait(0);
    player.show(false);
    host.setAttribute('data-intro-active','true');
    overlay.hidden=false;
    var seen=player.vis;
    if('IntersectionObserver' in window){
      observer=new IntersectionObserver(function(entries){
        seen=entries[0].isIntersecting;
        animations.forEach(function(animation){
          if(animation.playState==='finished'||animation.playState==='idle')return;
          if(seen)animation.play();else animation.pause();
        });
      },{threshold:.05});
      observer.observe(host);
    }
    function animate(element,frames,settings){
      // Follow the supplied preview speed for both the homepage and case-study hero.
      var timing=Object.assign({},settings,{duration:settings.duration/(player.rate||1)});
      var animation=element.animate(frames,timing);animations.push(animation);
      if(!seen)animation.pause();
      return animation.finished;
    }
    try{
      await animate(logo,[
        {opacity:0,transform:'translateY(22px) scale(.55)'},
        {opacity:1,transform:'translateY(-5px) scale(1.08)',offset:.72},
        {opacity:1,transform:'translateY(0) scale(1)'}
      ],{duration:650,easing:'cubic-bezier(.2,.75,.25,1)',fill:'both'});
      await player.wait(620);
      await Promise.all([
        animate(logo,[{opacity:1,transform:'translateY(0) scale(1)'},{opacity:0,transform:'translateY(-18px) scale(.84)'}],{duration:420,easing:'cubic-bezier(.4,0,.2,1)',fill:'both'}),
        animate(overlay,[{opacity:1},{opacity:0}],{duration:500,easing:'ease-in-out',fill:'both'})
      ]);
    }finally{
      if(observer)observer.disconnect();
      overlay.hidden=true;
      host.removeAttribute('data-intro-active');
      animations.forEach(function(animation){animation.cancel()});
    }
  };
})();
