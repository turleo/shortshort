function onload(){
    if (!navigator.share) {
        document.getElementById("share").style.display = "none";
    }
    if (!navigator.clipboard) {
        document.getElementById("share").style.display = "none";
    }
}

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
        document.getElementById("res").style.display = "block";
    };

    console.log(text);
}


function share(){
    document.getElementById("out")
}


function copy(){
    var blob = new Blob([document.getElementById("out").innerHTML], {type: 'text/plain'});
    var item = new ClipboardItem({'text/plain': blob});
    navigator.clipboard.write([item])
}
