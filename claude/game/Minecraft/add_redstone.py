#!/usr/bin/env python3
"""Adds redstone to Blockcraft.   Usage: python add_redstone.py index.html   (writes index.html, keeps index.html.bak)"""
import sys, shutil
fn = sys.argv[1] if len(sys.argv) > 1 else 'index.html'
s = open(fn, encoding='utf-8').read()
if 'RSID' in s: sys.exit('Redstone already applied.')
shutil.copy(fn, fn + '.bak')

def rep(a, b):
    global s
    if s.count(a) != 1: sys.exit('Patch anchor not found exactly once:\n' + a[:80])
    s = s.replace(a, b)

rep("ATLAS_TILES=32;", "ATLAS_TILES=48;")
rep("18:{n:'Gravel',t:[19,19,19]}", r"""18:{n:'Gravel',t:[19,19,19]},
  19:{n:'Redstone Ore',t:[20,20,20]}, 46:{n:'Redstone Dust',t:[21,21,21]}, 47:{n:'Redstone Block',t:[23,23,23]},
  48:{n:'Redstone Torch',t:[24,24,24],l:25}, 49:{n:'Lever',t:[26,26,26]}, 50:{n:'Lever',t:[27,27,27]},
  51:{n:'Button',t:[28,28,28]}, 61:{n:'Button',t:[44,44,44]}, 52:{n:'Pressure Plate',t:[29,29,29],l:45},
  53:{n:'Repeater',t:[30,30,30],l:31}, 54:{n:'Piston',t:[32,32,32],d:[33,32]}, 55:{n:'Sticky Piston',t:[32,32,32],d:[34,32]},
  56:{n:'Piston Head',t:[35,35,35]}, 57:{n:'Observer',t:[38,38,38],d:[36,37]}, 58:{n:'Redstone Lamp',t:[39,39,39],l:40},
  59:{n:'TNT',t:[42,41,42]}, 60:{n:'Note Block',t:[43,43,43]}""")
rep("var CREATIVE=[1,2,3,4,5,6,7,8,9,15,16,17,18,11,12,13,14], MAXID=18;",
    "var CREATIVE=[1,2,3,4,5,6,7,8,9,15,16,17,18,11,12,13,14,19,46,47,48,49,51,52,53,54,55,57,58,59,60], MAXID=63;")
rep("function nameOf(id){ return id<20?BLOCKS[id].n:ITEMS[id].n }", "function nameOf(id){ return BLOCKS[id]?BLOCKS[id].n:ITEMS[id].n }")
rep("var HARD={1:.6,", "var HARD={19:4.5,1:.6,")
rep("var CLS={1:2,", "var CLS={19:0,1:2,")
rep("var MINT={3:0,", "var MINT={19:2,3:0,")
rep("{o:17,n:1,i:{21:1,6:2}}];", r"""{o:17,n:1,i:{21:1,6:2}},
  {o:49,n:1,i:{20:1,15:1}},{o:51,n:1,i:{3:1}},{o:52,n:1,i:{3:2}},{o:48,n:1,i:{20:1,46:1}},{o:47,n:1,i:{46:9}},{o:46,n:9,i:{47:1}},
  {o:53,n:1,i:{3:3,48:2,46:1}},{o:54,n:1,i:{6:3,15:4,22:1,46:1}},{o:55,n:1,i:{54:1,4:2}},{o:57,n:1,i:{15:6,46:2,22:1}},
  {o:58,n:1,i:{46:4,6:1}},{o:59,n:1,i:{46:5,4:4}},{o:60,n:1,i:{6:8,46:1}}];""")
rep("if(y<16&&r<.0025) return 13;", "if(y<18&&r>.4&&r<.412) return 19;\n    if(y<16&&r<.0025) return 13;")
rep("y>=1&&y<H&&t>=0&&t<=MAXID;", "y>=1&&y<H&&t>=0&&t<=255&&(t===0||!!BLOCKS[t&63]);")

# ---- textures
rep("fill(19,[132,126,122],.5);", r"""fill(19,[132,126,122],.5);
  function rect(t,c,x0,y0,w,h){for(var yy=y0;yy<y0+h;yy++)for(var xx=x0;xx<x0+w;xx++)px(t,xx,yy,col(c,1+(rnd()-.5)*.12))}
  var ST=[126,126,130], PL=[176,138,84], OB=[100,100,106], ii;
  ore(20,[215,35,35]); fill(21,[110,12,12],.4); rect(21,[225,45,45],7,0,2,16); rect(21,[225,45,45],0,7,16,2); fill(23,[190,22,22],.3);
  fill(24,[58,46,34],.2); rect(24,[120,92,56],6,3,4,11); rect(24,[90,40,30],6,1,4,3);
  fill(25,[58,46,34],.2); rect(25,[120,92,56],6,5,4,9); rect(25,[255,60,30],5,1,6,5); rect(25,[255,190,90],6,2,4,2);
  fill(26,ST,.2); fill(27,ST,.2); for(ii=0;ii<9;ii++){ rect(26,[140,100,50],3+ii,12-ii,2,2); rect(27,[255,200,60],11-ii,12-ii,2,2) }
  fill(28,ST,.2); rect(28,[170,170,176],5,5,6,6); fill(44,ST,.2); rect(44,[210,190,90],5,5,6,6);
  fill(29,[140,140,146],.15); rect(29,[110,110,116],2,2,12,12); fill(45,[140,140,146],.15); rect(45,[190,70,60],2,2,12,12);
  fill(30,[150,150,155],.12); fill(31,[150,150,155],.12);
  [[100,30,30,30],[255,60,40,31]].forEach(function(a){ var c=[a[0],a[1],a[2]]; rect(a[3],c,4,3,2,2); rect(a[3],c,10,3,2,2); rect(a[3],c,7,10,2,3) });
  fill(32,PL,.12); rect(32,[110,110,114],0,0,16,3);
  fill(33,PL,.12); fill(34,[90,170,80],.2);
  [33,34].forEach(function(t){ rect(t,[120,120,124],0,0,16,2); rect(t,[120,120,124],0,14,16,2); rect(t,[120,120,124],0,0,2,16); rect(t,[120,120,124],14,0,2,16) });
  fill(35,PL,.12); rect(35,[110,110,114],5,5,6,6);
  fill(36,OB,.2); rect(36,[30,30,34],3,5,4,4); rect(36,[30,30,34],9,5,4,4); fill(37,OB,.2); rect(37,[200,40,40],6,6,4,4); fill(38,OB,.2);
  fill(39,[120,86,50],.2); rect(39,[80,56,34],3,3,10,10); fill(40,[255,210,120],.12); rect(40,[255,245,190],3,3,10,10);
  fill(41,[205,50,40],.15); rect(41,[235,235,230],0,6,16,4); fill(42,[215,195,150],.1); rect(42,[60,50,40],7,7,2,2);
  fill(43,[170,128,76],.12); rect(43,[100,66,38],4,4,8,8); rect(43,[170,128,76],6,6,4,4);""")

# ---- mesher
rep("var id=world[ix(x,y,z)]; if(!id) continue;", "var wi=ix(x,y,z), raw=world[wi], id=raw&63; if(!id) continue;")
rep("var jit=.94+.06*hash2(x+y*131,z,3);", "var jit=.94+.06*hash2(x+y*131,z,3), lit=pw[wi]>0, dm=id===46?.4+.6*pw[wi]/15:1;")
rep("var tile=blk.t[F.kind], u0=tile/ATLAS_TILES+.0004, u1=(tile+1)/ATLAS_TILES-.0004;",
    r"""var tile=blk.t[F.kind];
      if(blk.d&&F.kind===1){ var dv=DIRS[raw>>6]; if(F.n[0]===dv[0]&&F.n[2]===dv[1]) tile=blk.d[0]; else if(F.n[0]===-dv[0]&&F.n[2]===-dv[1]) tile=blk.d[1] }
      if(lit&&blk.l!==undefined) tile=blk.l;
      var u0=tile/ATLAS_TILES+.0004, u1=(tile+1)/ATLAS_TILES-.0004;""")
rep("var b=F.sh*AO[ao[k]]*jit; if(id===17) b=1;", "var b=F.sh*AO[ao[k]]*jit*dm; if(id===17||(lit&&(id===58||id===48))) b=1;")
rep("if(world[i]===t) return false;", "if(world[i]===t) return false; setRS(i,t,x,y,z);")

# ---- save / load / gameplay hooks
rep("loadGraves(save.g);", "loadGraves(save.g); RD=save.rd||{}; NP=save.np||{}; buildRS();")
rep("save.m=mode; save.inv=inv;", "save.rd=RD; save.np=NP; save.m=mode; save.inv=inv;")
rep("var id=get(brk.x,brk.y,brk.z); if(!id)", "var id=get(brk.x,brk.y,brk.z)&63; if(!id)")
rep("var d=DROPS[id]||id;", "if(id===19){ addItem(46,4); buildHotbar(); scheduleSave(); return } if(id===56) return; if(id===50) id=49; if(id===61) id=51; var d=DROPS[id]||id;")
rep("if(id>=20) drawItem(g,id); else g.drawImage", "if(!BLOCKS[id]) drawItem(g,id); else g.drawImage")
rep("if(id<20&&BLOCKS[id].t[0]", "if(BLOCKS[id]&&BLOCKS[id].t[0]")
rep("if(!bid||bid>=20) return;", "if(!bid||!BLOCKS[bid]) return;")
rep("localEdit(x,y,z,bid); if(mode==='s') buildHotbar();",
    "localEdit(x,y,z,DIRB[bid]?(bid|((((Math.round(P.yaw/(Math.PI/2))%4)+4)%4)<<6)):bid); if(mode==='s') buildHotbar();")
rep("if((e.button===0||e.button===2)&&tryGrave()) return;", "if(e.button===2&&interact()) return;\n    if((e.button===0||e.button===2)&&tryGrave()) return;")
rep("var np=mode==='c'?2:", "var np=mode==='c'?Math.ceil(CREATIVE.length/9):")
rep("physics(dt); survivalTick(now); mineTick(dt);",
    "physics(dt); survivalTick(now); mineTick(dt); simAcc+=dt; for(var sn=0;simAcc>=.1&&sn<3;sn++){ simAcc-=.1; simTick() } if(simAcc>.3) simAcc=0;")
rep("Arrow keys also turn the camera.", "Arrow keys also turn the camera. <b>Right click</b> a lever, button, repeater (delay) or note block to use it.")

# ---- the redstone engine
rep("var REACH=6;", r"""var REACH=6;

/* ================= REDSTONE =================
   Block byte = id (low 6 bits) | facing (top 2 bits). Power lives in pw[], simulated every 0.1s (one redstone tick).
   Every client simulates deterministically; only player edits are networked. */
var RSID={}; [46,47,48,49,50,51,52,53,54,55,57,58,59,60,61].forEach(function(i){RSID[i]=1});
var DIRB={53:1,54:1,55:1,57:1};
var DIRS=[[0,-1],[-1,0],[0,1],[1,0]], FI=[5,1,4,0];
var NB=[[1,0,0],[-1,0,0],[0,1,0],[0,-1,0],[0,0,1],[0,0,-1]];
var DN=NB.slice(); DIRS.forEach(function(d){ DN.push([d[0],1,d[1]],[d[0],-1,d[1]]) });
var RS=new Set(), pw=new Uint8Array(W*D*H), RC={}, OBT={}, BT={}, TF={}, RD={}, NP={}, simAcc=0, AC=null;
function xyz(i){ var y=(i/(W*D))|0, r=i-y*W*D, z=(r/W)|0; return [r-z*W,y,z] }
function inB(x,y,z){ return x>=0&&x<W&&z>=0&&z<D&&y>=1&&y<H }
function buildRS(){
  RS.clear(); pw.fill(0); RC={}; OBT={}; BT={}; TF={};
  for(var i=0;i<world.length;i++){ var v=world[i]; if(v&&RSID[v&63]){ RS.add(i); if((v&63)===48) pw[i]=1; if((v&63)===61) BT[i]=10 } }
}
function setRS(i,t,x,y,z){ pw[i]=(t&63)===48?1:0; if(t&&RSID[t&63]) RS.add(i); else RS.delete(i); delete RC[i]; ping(x,y,z) }
function simEdit(x,y,z,t){ if(setBlock(x,y,z,t)){ save.e[x+','+y+','+z]=t; scheduleSave() } }
function ping(x,y,z){
  if(y<1||y>=H) return;
  for(var k=0;k<4;k++){
    var ox=x-DIRS[k][0], oz=z-DIRS[k][1]; if(ox<0||ox>=W||oz<0||oz>=D) continue;
    var q=ix(ox,y,oz), r=world[q];
    if((r&63)===57&&(r>>6)===k&&!(OBT[q]>0)&&!pw[q]) OBT[q]=2;
  }
}
function strongIn(x,y,z){
  var m=0;
  for(var n=0;n<6;n++){
    var a=NB[n], nx=x+a[0], ny=y+a[1], nz=z+a[2], id=get(nx,ny,nz)&63;
    if(id===47||id===50||id===61||id===52||id===53||id===57||(id===48&&ny===y-1)) m=Math.max(m,outTo(nx,ny,nz,x,y,z));
  }
  return m;
}
/* power that the block at (x,y,z) gives to the neighbour at (tx,ty,tz) */
function outTo(x,y,z,tx,ty,tz){
  if(!inB(x,y,z)) return 0;
  var i=ix(x,y,z), raw=world[i]; if(!raw) return 0;
  var id=raw&63, v=pw[i], dv;
  switch(id){
    case 46: return v;
    case 47: case 50: case 61: return 15;
    case 52: return v?15:0;
    case 48: return v&&ty>=y?15:0;
    case 53: dv=DIRS[raw>>6]; return v&&ty===y&&tx===x+dv[0]&&tz===z+dv[1]?15:0;
    case 57: dv=DIRS[raw>>6]; return v&&ty===y&&tx===x-dv[0]&&tz===z-dv[1]?15:0;
    case 49: case 51: case 54: case 55: case 58: case 59: case 60: return 0;
    default: return strongIn(x,y,z);
  }
}
function inP(x,y,z,skip,weakDust){
  var m=0;
  for(var n=0;n<6;n++){
    if(n===skip) continue;
    var a=NB[n], nx=x+a[0], ny=y+a[1], nz=z+a[2];
    m=Math.max(m,outTo(nx,ny,nz,x,y,z));
    if(weakDust&&inB(nx,ny,nz)&&(world[ix(nx,ny,nz)]&63)===46) m=Math.max(m,pw[ix(nx,ny,nz)]);
  }
  return m;
}
function occupied(x,y,z){
  function on(px,py,pz){ return Math.floor(px)===x&&Math.floor(pz)===z&&Math.floor(py+.01)===y+1 }
  if(on(P.x,P.y,P.z)) return true;
  var f=false; remotes.forEach(function(r){ if(on(r.x,r.y,r.z)) f=true }); return f;
}
function pushable(X,Y,Z){
  if(!inB(X,Y,Z)) return false;
  var id=get(X,Y,Z)&63;
  return id!==10&&id!==16&&id!==56&&!((id===54||id===55)&&pw[ix(X,Y,Z)]);
}
function pistonExt(x,y,z,raw){
  var d=DIRS[raw>>6], n=0, X=x+d[0], Z=z+d[1];
  while(get(X,y,Z)){ if(!pushable(X,y,Z)||++n>12) return false; X+=d[0]; Z+=d[1] }
  for(var j=n;j>=1;j--){ var fx=x+d[0]*j, fz=z+d[1]*j; simEdit(fx+d[0],y,fz+d[1],get(fx,y,fz)) }
  simEdit(x+d[0],y,z+d[1],56|((raw>>6)<<6));
  return true;
}
function pistonRet(x,y,z,raw){
  var d=DIRS[raw>>6], fx=x+d[0], fz=z+d[1];
  if((get(fx,y,fz)&63)!==56) return;
  simEdit(fx,y,fz,0);
  if((raw&63)===55){
    var bx=fx+d[0], bz=fz+d[1];
    if(get(bx,y,bz)&&pushable(bx,y,bz)){ simEdit(fx,y,fz,get(bx,y,bz)); simEdit(bx,y,bz,0) }
  }
}
function explode(x,y,z){
  simEdit(x,y,z,0);
  for(var dy=-3;dy<=3;dy++) for(var dz=-3;dz<=3;dz++) for(var dx=-3;dx<=3;dx++){
    if(dx*dx+dy*dy+dz*dz>10) continue;
    var X=x+dx, Y=y+dy, Z=z+dz; if(!inB(X,Y,Z)) continue;
    var id=get(X,Y,Z)&63; if(!id||id===10||id===16) continue;
    if(id===59) TF[ix(X,Y,Z)]=2; else simEdit(X,Y,Z,0);
  }
  var dd=Math.hypot(P.x-x-.5,P.y+1-y,P.z-z-.5); if(dd<6) hurt(Math.ceil((6-dd)*2.5));
}
function playNote(n){
  try{
    AC=AC||new (window.AudioContext||window.webkitAudioContext)();
    var o=AC.createOscillator(), g=AC.createGain(), t=AC.currentTime;
    o.type='triangle'; o.frequency.value=130.81*Math.pow(2,n/12);
    g.gain.setValueAtTime(.2,t); g.gain.exponentialRampToValueAtTime(.001,t+.5);
    o.connect(g); g.connect(AC.destination); o.start(); o.stop(t+.5);
  }catch(e){}
}
function interact(){
  if(!target) return false;
  var x=target.x, y=target.y, z=target.z, raw=get(x,y,z), id=raw&63, f=raw&192, i=ix(x,y,z);
  if(id===49||id===50){ localEdit(x,y,z,f|(id===49?50:49)); return true }
  if(id===51){ localEdit(x,y,z,f|61); BT[i]=10; return true }
  if(id===53){ RD[i]=((RD[i]||1)%4)+1; toast('Repeater delay: '+RD[i]+' tick'+(RD[i]>1?'s':'')); scheduleSave(); return true }
  if(id===60){ NP[i]=((NP[i]||0)+1)%25; playNote(NP[i]); scheduleSave(); return true }
  return false;
}
function setPw(i,v,x,y,z){ if(pw[i]===v) return; pw[i]=v; markDirty(x>>4,z>>4); ping(x,y,z) }
function simTick(){
  var list=Array.from(RS), upd=[], dust=[], nl={}, k, i, p;
  for(i in BT){ if(--BT[i]<=0){ var bi=+i; delete BT[i]; var br=world[bi]; if((br&63)===61){ p=xyz(bi); localEdit(p[0],p[1],p[2],(br&192)|51) } } }
  for(k=0;k<list.length;k++) if((world[list[k]]&63)===46) dust.push(list[k]);
  dust.forEach(function(i){
    var p=xyz(i), m=0;
    for(var n=0;n<6;n++){ var a=NB[n], nx=p[0]+a[0], ny=p[1]+a[1], nz=p[2]+a[2]; if((get(nx,ny,nz)&63)!==46) m=Math.max(m,outTo(nx,ny,nz,p[0],p[1],p[2])) }
    nl[i]=m;
  });
  var ch=true, pass=0;
  while(ch&&pass++<16){
    ch=false;
    dust.forEach(function(i){
      var p=xyz(i), m=nl[i];
      for(var n=0;n<DN.length;n++){
        var a=DN[n], nx=p[0]+a[0], ny=p[1]+a[1], nz=p[2]+a[2];
        if(!inB(nx,ny,nz)) continue;
        var j=ix(nx,ny,nz); if((world[j]&63)===46&&nl[j]!==undefined&&nl[j]-1>m) m=nl[j]-1;
      }
      if(m!==nl[i]){ nl[i]=m; ch=true }
    });
  }
  dust.forEach(function(i){ var p=xyz(i); setPw(i,nl[i],p[0],p[1],p[2]) });
  list.forEach(function(i){
    var raw=world[i], id=raw&63, v=pw[i]; if(!id||id===46) return;
    var p=xyz(i), x=p[0], y=p[1], z=p[2];
    switch(id){
      case 48: { var by=get(x,y-1,z)&63, inn=(by&&!RSID[by])?inP(x,y-1,z,2,true):outTo(x,y-1,z,x,y,z); upd.push([i,inn>0?0:1]) } break;
      case 53: { var dv=DIRS[raw>>6], want=outTo(x-dv[0],y,z-dv[1],x,y,z)>0;
        if(want!==(v>0)){ RC[i]=(RC[i]||0)+1; if(RC[i]>=(RD[i]||1)){ upd.push([i,want?1:0]); RC[i]=0 } } else RC[i]=0 } break;
      case 52: upd.push([i,occupied(x,y,z)?1:0]); break;
      case 58: upd.push([i,inP(x,y,z,-1)>0?1:0]); break;
      case 60: { var onN=inP(x,y,z,-1)>0; if(onN&&!v) playNote(NP[i]||0); upd.push([i,onN?1:0]) } break;
      case 59: if(inP(x,y,z,-1)>0&&!TF[i]) TF[i]=4; break;
      case 54: case 55: { var onP=inP(x,y,z,FI[raw>>6])>0;
        if(onP&&!v){ if(pistonExt(x,y,z,raw)) upd.push([i,1]) } else if(!onP&&v){ pistonRet(x,y,z,raw); upd.push([i,0]) } } break;
      case 57: if(OBT[i]>0){ OBT[i]--; upd.push([i,1]) } else upd.push([i,0]); break;
    }
  });
  for(i in TF){ if(--TF[i]<=0){ delete TF[i]; if((world[+i]&63)===59){ p=xyz(+i); explode(p[0],p[1],p[2]) } } }
  upd.forEach(function(u){ var q=xyz(u[0]); if(world[u[0]]) setPw(u[0],u[1],q[0],q[1],q[2]) });
}""")

open(fn, "w", encoding="utf-8").write(s)
print("Redstone added to", fn, "(backup:", fn + ".bak)")
