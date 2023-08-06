function onload(){
    if (!navigator.canShare) {
        document.getElementById("share").style.display = "none";
    }
    if (!navigator.clipboard) {
        document.getElementById("share").style.display = "none";
    }
}

function short(){
    var out = document.getElementById("out");
    var error = document.getElementById("error");
    var text = document.getElementById("link").value;
    var xhr = new XMLHttpRequest();
    xhr.open('GET', '/api/create/?q=' + text, true);
    xhr.send();
    xhr.onload = function() {
        if (xhr.status == 200) {
            var url = window.location.href + xhr.response;
            out.innerHTML = url;
            out.href = url;
            document.getElementById("res").style.display = "block";
            error.style.display = "none";
        } else {
            document.getElementById("res").style.display = "none";
            error.style.display = "block";
        }
    };
}


function share(){
    navigator.share({
        text: document.getElementById("out").innerHTML
    })
}


function copy(){
    var blob = new Blob([document.getElementById("out").innerHTML], {type: 'text/plain'});
    var item = new ClipboardItem({'text/plain': blob});
    navigator.clipboard.write([item])
}
