(function(){
  "use strict";
  var MS_DAY = 86400000, now = new Date();
  var MON = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"];
  function parse(s){ var p=s.split("-"); return new Date(+p[0],+p[1]-1,+p[2]); }
  function rel(d){
    var diff = Math.floor((now - d)/MS_DAY);
    if(diff<=0) return "Today";
    if(diff===1) return "Yesterday";
    if(diff<7) return diff+" days ago";
    if(diff<14) return "1 week ago";
    return MON[d.getMonth()]+" "+d.getDate();
  }
  var items = [].slice.call(document.querySelectorAll(".lf-item"));
  items.forEach(function(el){
    el.__promo = el.getAttribute("data-promo");
    el.__cat = el.getAttribute("data-cat");
    el.__text = (el.getAttribute("data-headline")+" "+el.textContent+" "+el.__promo+" "+el.__cat).toLowerCase();
    var w = el.querySelector(".lf-when"), ds = el.getAttribute("data-date");
    if(w && ds) w.textContent = rel(parse(ds));
  });

  var state = { promo:"all", cat:"all", q:"" };
  var countEl = document.getElementById("lf-count");

  function ok(el){
    if(state.promo!=="all"){
      if(state.promo==="tko"){ if(el.__promo!=="tko" && el.__promo!=="industry") return false; }
      else if(el.__promo!==state.promo) return false;
    }
    if(state.cat!=="all" && el.__cat!==state.cat) return false;
    if(state.q && el.__text.indexOf(state.q)===-1) return false;
    return true;
  }
  function apply(){
    var shown=0;
    items.forEach(function(el){ var m=ok(el); el.style.display=m?"":"none"; if(m) shown++; });
    // hide a lead/river/dept whose children all vanished
    document.querySelectorAll(".lf-lead,.lf-river").forEach(function(box){
      var any=[].slice.call(box.querySelectorAll(".lf-item")).some(function(e){return e.style.display!=="none";});
      box.style.display = any?"":"none";
    });
    var active = (state.promo!=="all"||state.cat!=="all"||state.q!=="");
    if(countEl) countEl.innerHTML = "<b>"+shown+"</b> "+(shown===1?"dispatch":"dispatches")+(active?" match your filters":" this week");
  }

  document.querySelectorAll(".lf-chiprow").forEach(function(row){
    var facet = row.getAttribute("data-facet");
    row.addEventListener("click", function(e){
      var b=e.target.closest(".lf-chip"); if(!b) return;
      row.querySelectorAll(".lf-chip").forEach(function(x){ x.setAttribute("aria-pressed", x===b?"true":"false"); });
      state[facet]=b.getAttribute("data-val"); apply();
    });
  });
  var q=document.getElementById("lf-q"), t;
  if(q) q.addEventListener("input", function(){ clearTimeout(t); t=setTimeout(function(){ state.q=q.value.trim().toLowerCase(); apply(); },120); });
  apply();
})();
