uno=document.getElementById('chest');
dos=document.getElementById('front');
enviar=document.getElementById('enviar');
tres=document.getElementById('across');
error=document.getElementById('error');

uno.addEventListener('click', function () {
    uno.value="";
    document.getElementById('error').innerHTML=""
    document.getElementById('error2').innerHTML=""
    document.getElementById('error3').innerHTML=""

})
dos.addEventListener('click', function () {
    dos.value="";
    document.getElementById('error').innerHTML=""
    document.getElementById('error2').innerHTML=""
    document.getElementById('error3').innerHTML=""

})
tres.addEventListener('click', function () {
    tres.value="";
    document.getElementById('error').innerHTML=""
    document.getElementById('error2').innerHTML=""
    document.getElementById('error3').innerHTML=""

})
enviar.addEventListener('click', function () {
    if(uno.value<91 || uno.value>138){
        document.getElementById('error').innerHTML="Datos de Chest fuera de rango"
    }else{
        document.getElementById('error').innerHTML=""
    }
    if(dos.value<67 || dos.value>102){
        document.getElementById('error2').innerHTML="Datos de Front Length fuera de rango"
    }else{
        document.getElementById('error2').innerHTML=""
    }
    if(tres.value<40 || tres.value>56){
        document.getElementById('error3').innerHTML="Datos de Across Shoulder fuera de rango"
    }else{
        document.getElementById('error3').innerHTML=""
    }
})
