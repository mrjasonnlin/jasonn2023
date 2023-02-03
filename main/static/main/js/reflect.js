function f1(){
setInterval("mdiv.filters.wave.phase+=10",100);
}

if (document.all){
document.write('<img id=mdiv src="'+document.all.reflect.src+'" style="filter:wave(strength=3,freq=3,phase=0,lightstrength=30) blur() flipv()">')
window.onload=f1
}
