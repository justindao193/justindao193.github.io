(function(){
  'use strict';
  var project=/* PROJECT_DATA */;
  var data=project.areas,select=document.getElementById('area'),result=document.getElementById('area-result');
  function choose(name){
    var d=data.find(function(x){return x.name===name});if(!d)return;
    select.value=name;result.replaceChildren();
    var b=document.createElement('b'),n=document.createElement('strong');b.textContent=name;n.textContent=d.pressure.toFixed(1)+'%';result.append(b,n);
    document.getElementById('area-rent').textContent='$'+d.rent.toLocaleString('en-CA');
    document.getElementById('area-support').textContent=d.support.toFixed(1)+'%';
    document.getElementById('area-bar-fill').style.width=d.pressure+'%';
    document.querySelectorAll('.map-canvas .area').forEach(function(p){p.classList.toggle('selected',p.dataset.name===name)});
    document.querySelectorAll('[data-area]').forEach(function(b){b.classList.toggle('on',b.dataset.area===name);b.setAttribute('aria-pressed',b.dataset.area===name?'true':'false')});
    var c=project.centres[name],marker=document.querySelector('.map-marker');marker.setAttribute('cx',c[0]);marker.setAttribute('cy',c[1]);
  }
  select.addEventListener('change',function(){choose(this.value)});
  document.querySelectorAll('.map-canvas .area').forEach(function(p){p.addEventListener('click',function(){choose(this.dataset.name)})});
  document.querySelectorAll('[data-area]').forEach(function(b){b.addEventListener('click',function(){choose(this.dataset.area)})});choose(select.value);
  var chart=document.getElementById('scatter'),NS='http://www.w3.org/2000/svg';
  function draw(){
    var w=chart.clientWidth,h=chart.clientHeight,left=44,right=12,top=40,bottom=60,svg=document.createElementNS(NS,'svg');
    svg.setAttribute('viewBox','0 0 '+w+' '+h);svg.setAttribute('aria-hidden','true');
    function el(tag,attrs,text){var e=document.createElementNS(NS,tag);Object.keys(attrs).forEach(function(k){e.setAttribute(k,attrs[k])});if(text!=null)e.textContent=text;svg.appendChild(e);return e}
    var x=function(v){return left+(v-400)/2100*(w-left-right)},y=function(v){return top+(70-v)/50*(h-top-bottom)};
    [20,30,40,50,60].forEach(function(v){el('line',{x1:left,x2:w-right,y1:y(v),y2:y(v),'stroke-dasharray':v===30?'3 4':'0'});el('text',{x:left-10,y:y(v)+4,'text-anchor':'end'},v+'%')});
    [500,1000,1500,2000].forEach(function(v){el('text',{x:x(v),y:h-34,'text-anchor':'middle'},'$'+v.toLocaleString('en-CA'))});
    el('text',{x:left,y:14},'Renters above the 30% threshold');el('text',{x:(w+left)/2,y:h-6,'text-anchor':'middle'},'Average monthly rental housing cost');
    var featured=['Newtonbrook West','Kingsway South'];
    data.filter(function(d){return featured.indexOf(d.name)<0}).forEach(function(d){var p=el('circle',{cx:x(d.rent),cy:y(d.pressure),r:w<400?3:4});var t=document.createElementNS(NS,'title');t.textContent=d.name+': $'+d.rent+' / month; '+d.pressure+'%';p.appendChild(t)});
    featured.forEach(function(name,i){var d=data.find(function(d){return d.name===name}),cx=x(d.rent),cy=y(d.pressure);el('circle',{cx:cx,cy:cy,r:15,'class':'point-halo'});el('circle',{cx:cx,cy:cy,r:10,'class':'highlight'});el('text',{x:cx,y:cy+3.5,'text-anchor':'middle','class':'point-digit'},i+1);if(w>540){el('text',{x:cx+18,y:cy+4,'class':'point-label'},name)}});
    chart.replaceChildren(svg);
  }
  new ResizeObserver(draw).observe(chart);draw();
  document.querySelectorAll('.tbtn').forEach(function(b){b.addEventListener('click',function(){jdTheme.set(jdTheme.get()==='dark'?'light':'dark')})});
  var links=[].slice.call(document.querySelectorAll('.side li a'));
  var observer=new IntersectionObserver(function(entries){entries.forEach(function(e){if(e.isIntersecting)links.forEach(function(a){a.classList.toggle('on',a.hash==='#'+e.target.id)})})},{rootMargin:'-10% 0px -65% 0px'});
  document.querySelectorAll('main section[id],main header[id]').forEach(function(s){observer.observe(s)});
  var motion=new IntersectionObserver(function(es){es.forEach(function(e){e.target.classList.toggle('running',e.isIntersecting)})});
  document.querySelectorAll('.housing-media').forEach(function(e){motion.observe(e)});
  var control=document.querySelector('.motion-control');control.addEventListener('click',function(){var paused=this.parentElement.classList.toggle('paused');this.textContent=paused?'Play':'Pause';this.setAttribute('aria-label',paused?'Play the comparison animation':'Pause the comparison animation')});
  if('scrollRestoration' in history)history.scrollRestoration='manual';if(!location.hash)window.scrollTo(0,0);
})();
