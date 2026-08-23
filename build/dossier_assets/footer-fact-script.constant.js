
  (function(){
    var facts=[
      "Stone Cold Steve Austin won the Royal Rumble three times, in 1997, 1998 and 2001. No one has won more.",
      "At Vengeance 2001, Chris Jericho beat both The Rock and Steve Austin in one night to become the first Undisputed Champion.",
      "Kurt Angle won a 1996 Olympic gold medal in freestyle wrestling with a broken neck.",
      "The Undertaker won 21 straight WrestleMania matches before Brock Lesnar beat him in 2014.",
      "The nWo was born at Bash at the Beach 1996, when Hulk Hogan turned on WCW.",
      "In the 1997 Montreal Screwjob, Bret Hart lost a title he never agreed to drop.",
      "ECW's Barely Legal in 1997 was the promotion's first pay-per-view.",
      "Mankind fell off the top of the Hell in a Cell at King of the Ring 1998, then crashed through the roof.",
      "AEW ran its first show, Double or Nothing, in Las Vegas in 2019."
    ];
    var el=document.querySelector('[data-wl-fact]');
    if(!el){return;}
    var i=Math.floor(Math.random()*facts.length);
    el.textContent=facts[i];
    var btn=document.querySelector('[data-wl-fact-shuffle]');
    if(btn){btn.addEventListener('click',function(){i=(i+1+Math.floor(Math.random()*(facts.length-1)))%facts.length;el.textContent=facts[i];});}
  })();
  