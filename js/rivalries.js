/* Rivalries hub: client-side filter + sort over already-rendered head-to-head cards.
   Progressive enhancement — with JS off, all 15 bouts render and link normally. No storage. */
(function(){
  var root=document.querySelector('.rvh');
  if(!root) return;
  var grid=root.querySelector('.rvh-grid');
  var cards=[].slice.call(root.querySelectorAll('.rvh-bout'));
  var countEl=root.querySelector('.rvh-count');
  var emptyEl=root.querySelector('.rvh-empty');
  var resetBtn=root.querySelector('.rvh-reset');
  var sortSel=root.querySelector('.rvh-sort__sel');
  if(!grid||!cards.length) return;

  var order=cards.slice();                 // original DOM order = "heat"
  var state={promo:new Set(),era:new Set(),type:new Set()};

  function matches(card){
    for(var dim in state){
      var sel=state[dim];
      if(!sel.size) continue;
      var vals=(card.getAttribute('data-'+dim)||'').split(/\s+/);
      var hit=false;
      sel.forEach(function(v){ if(vals.indexOf(v)>-1) hit=true; });
      if(!hit) return false;
    }
    return true;
  }

  function apply(){
    var shown=0;
    cards.forEach(function(c){
      var ok=matches(c);
      c.hidden=!ok;
      if(ok) shown++;
    });
    if(countEl) countEl.textContent=shown+(shown===1?' rivalry':' rivalries');
    if(emptyEl) emptyEl.hidden=shown!==0;
    var active=state.promo.size||state.era.size||state.type.size;
    if(resetBtn) resetBtn.hidden=!active;
  }

  function sortBy(mode){
    var arr;
    if(mode==='az') arr=order.slice().sort(function(a,b){return (a.getAttribute('data-name')||'').localeCompare(b.getAttribute('data-name')||'');});
    else if(mode==='new') arr=order.slice().sort(function(a,b){return (+b.getAttribute('data-yr'))-(+a.getAttribute('data-yr'));});
    else if(mode==='old') arr=order.slice().sort(function(a,b){return (+a.getAttribute('data-yr'))-(+b.getAttribute('data-yr'));});
    else arr=order;                        // heat = original order
    arr.forEach(function(c){grid.appendChild(c);});
  }

  root.querySelectorAll('.rvh-group').forEach(function(g){
    var dim=g.getAttribute('data-dim');
    g.querySelectorAll('.rvh-chip').forEach(function(chip){
      chip.addEventListener('click',function(){
        var v=chip.getAttribute('data-val');
        var on=chip.getAttribute('aria-pressed')==='true';
        chip.setAttribute('aria-pressed', on?'false':'true');
        if(on) state[dim].delete(v); else state[dim].add(v);
        apply();
      });
    });
  });

  if(sortSel) sortSel.addEventListener('change',function(){ sortBy(sortSel.value); });

  function resetAll(){
    ['promo','era','type'].forEach(function(d){state[d].clear();});
    root.querySelectorAll('.rvh-chip[aria-pressed="true"]').forEach(function(c){c.setAttribute('aria-pressed','false');});
    if(sortSel) sortSel.value='heat';
    sortBy('heat');
    apply();
  }
  if(resetBtn) resetBtn.addEventListener('click',resetAll);
  var er=root.querySelector('.rvh-emptyreset'); if(er) er.addEventListener('click',resetAll);

  apply();
})();
