function request(){
    var prompt =document.forms.datos.prompt.value;
    
    var datos = {
        model: "tinyllama",
        prompt: prompt,
        stream: false};
    alert(prompt);

    const URL = "http://localhost:11434/api/generate";

    var request = new XMLHttpRequest();

    request.open('POST', URL, true);

    request.setRequestHeader("Accept", "application/json");
    request.setRequestHeader("Content-Type", "application/json");

    request.send(JSON.stringify(datos));

    request.onload = ( ) => {
        if(request.status == 200){
            alert("RESPONSE");
        }else{
            alert("Algo Fallo");
        }
    };
};