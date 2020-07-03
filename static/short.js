function short(){
    var out = document.getElementById("out");
    var text = document.getElementById("link").value;
    var xhr = new XMLHttpRequest();
    xhr.open('GET', '/api/create/?q=' + text, true);
    xhr.send();
    xhr.onload = function() {
        var url = window.location.href + xhr.response;
        out.innerHTML = url;
        out.href = url;
    };

    console.log(text);
}