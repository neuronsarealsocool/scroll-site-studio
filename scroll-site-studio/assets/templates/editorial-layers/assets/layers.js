// Original, local-only hero depth. No media provider or external dependencies.
(()=>{
  const hero=document.querySelector('.hero'),art=document.querySelector('.composition');
  const reduced=matchMedia('(prefers-reduced-motion: reduce)');let frame=0;
  const draw=()=>{frame=0;const box=hero.getBoundingClientRect();art.style.setProperty('--travel',reduced.matches?'0':String(Math.max(0,Math.min(1,-box.top/Math.max(1,box.height)))))};
  const request=()=>{if(!frame)frame=requestAnimationFrame(draw)};
  addEventListener('scroll',request,{passive:true});addEventListener('resize',request,{passive:true});reduced.addEventListener('change',request);draw();
})();
