// Bounded Scroll World integration. Upstream MIT copyright 2026 cyw.
// See SCROLL-WORLD-LICENSE. Additional integration: Scroll Site Studio contributors.
const clamp=n=>Math.max(0,Math.min(1,n));
const smooth=n=>{const p=clamp(n);return p*p*(3-2*p)};

export function mountHeroFlight(root){
  for(const img of root.querySelectorAll('.flight-media [data-src]'))img.src=img.dataset.src;
  for(const source of root.querySelectorAll('.flight-media [data-srcset]'))source.srcset=source.dataset.srcset;
  const orientation=matchMedia('(orientation: portrait)');
  let release=mount(root,orientation.matches);
  const change=()=>{release();release=mount(root,orientation.matches)};
  orientation.addEventListener('change',change);
  return()=>{orientation.removeEventListener('change',change);release()};
}

function mount(root,portrait){
  const motion=matchMedia('(prefers-reduced-motion: reduce)');
  const controller=new AbortController(); const signal=controller.signal;
  const stage=root.querySelector('.hero-stage'),copy=root.querySelector('.hero-content'),hint=root.querySelector('.hero-scroll'),tail=root.querySelector('.flight-tail');
  const scenes=[...root.querySelectorAll('video[data-flight-src]')].map(video=>({video,layer:video.parentElement,url:portrait?video.dataset.flightMobileSrc:video.dataset.flightSrc,ready:false,loading:false,current:0,target:0,seekAt:0,priming:false,primed:false}));
  let enabled=false,dead=false,frame=0,progress=0; const timers=new Set();
  const later=(fn,delay)=>{const id=setTimeout(()=>{timers.delete(id);if(!dead)fn()},delay);timers.add(id);return id};
  const reset=()=>{root.classList.remove('flight-active');root.style.removeProperty('--flight-copy');copy.inert=false;hint.style.removeProperty('opacity');hint.style.removeProperty('visibility');tail.style.opacity='0'};
  const fail=()=>{enabled=false;root.dataset.flightFailed='true';reset()};
  const prime=s=>{
    if(dead||s.priming||s.primed||s.video.readyState<2)return;
    s.priming=true; const timeout=later(()=>{s.priming=false},1500);
    s.video.play().then(()=>{if(dead)return;s.video.pause();s.primed=true;s.priming=false;clearTimeout(timeout);timers.delete(timeout)}).catch(()=>{s.priming=false;clearTimeout(timeout);timers.delete(timeout)});
  };
  const load=async s=>{
    if(s.loading||s.ready||!enabled)return;s.loading=true;
    try{
      const response=await fetch(s.url,{signal});if(!response.ok)throw Error('Media unavailable');
      const blob=await response.blob();if(dead)return;
      s.blob=URL.createObjectURL(blob);s.video.src=s.blob;s.video.load();
    }catch{if(!dead&&!signal.aborted)fail()}
  };
  const read=()=>{
    if(!enabled||dead)return;
    const p=clamp(-root.getBoundingClientRect().top/Math.max(1,root.offsetHeight-stage.offsetHeight));progress=p;root.dataset.flightProgress=p.toFixed(3);
    const travel=clamp((p-.06)/.80);
    scenes.forEach((s,i)=>{s.target=clamp(travel*scenes.length-i);if(i===0||travel*scenes.length>i-.6)void load(s);s.layer.style.opacity=String(i===0?1:smooth((travel*scenes.length-i+.03)/.06))});
    const opacity=Math.max(1-smooth(p/.11),smooth((p-.83)/.10));root.style.setProperty('--flight-copy',String(opacity));copy.inert=opacity<.06&&!copy.contains(document.activeElement);
    hint.style.opacity=String(1-smooth(p/.06));hint.style.visibility=p>.06?'hidden':'visible';tail.style.opacity=String(smooth((p-.86)/.035));
    if(!frame)frame=requestAnimationFrame(tick);
  };
  const tick=()=>{
    frame=0;if(!enabled||dead||!root.isConnected)return;let moving=false;
    for(const s of scenes){
      if(!s.ready)continue;
      if(s.video.seeking){
        moving=true;
        if(s.seekAt&&performance.now()-s.seekAt>2500){fail();return}
        continue;
      }
      s.current+=(s.target-s.current)*.22;
      const duration=s.video.duration;if(!Number.isFinite(duration))continue;
      const time=Math.min(s.current*duration,Math.max(0,duration-1/24));
      if(Math.abs(s.video.currentTime-time)>(portrait?.025:.012)){s.seekAt=performance.now();s.video.currentTime=time;moving=true}
      if(Math.abs(s.target-s.current)>.002)moving=true;
    }
    if(moving&&progress>=0&&progress<=1)frame=requestAnimationFrame(tick);
  };
  for(const s of scenes){
    s.layer.classList.remove('has-frame');
    // Resolve hidden posters only when motion is enabled, not in the empty starter.
    const picture=s.layer.querySelector('picture');
    for(const img of picture.querySelectorAll('[data-src]'))img.src=img.dataset.src;
    for(const source of picture.querySelectorAll('[data-srcset]'))source.srcset=source.dataset.srcset;
    s.video.addEventListener('loadedmetadata',()=>{s.ready=true;read()},{signal});
    s.video.addEventListener('loadeddata',()=>{s.video.pause();prime(s)},{signal});
    s.video.addEventListener('seeked',()=>{if(dead)return;s.seekAt=0;s.layer.classList.add('has-frame');read()},{signal});
    s.video.addEventListener('error',fail,{signal});
  }
  const activate=()=>{enabled=scenes.length>0&&!motion.matches&&!navigator.connection?.saveData&&!root.dataset.flightFailed;if(enabled){root.classList.add('flight-active');read()}else reset()};
  const gesture=()=>{if(enabled)scenes.forEach(prime)};
  window.addEventListener('scroll',read,{passive:true,signal});window.addEventListener('resize',read,{passive:true,signal});motion.addEventListener('change',activate,{signal});
  for(const event of ['pointerdown','touchstart','touchend','click'])window.addEventListener(event,gesture,{passive:true,signal});
  activate();
  return()=>{dead=true;controller.abort();cancelAnimationFrame(frame);timers.forEach(clearTimeout);scenes.forEach(s=>{s.video.pause();s.video.removeAttribute('src');s.video.load();if(s.blob)URL.revokeObjectURL(s.blob)});reset()};
}
