setTimeout(function(){
    window.location.replace("http://127.0.0.1:5000/restart")
}, 60000)
restartButton = document.getElementById('restart');
restartButton.addEventListener('click', function(){
    window.location.replace("http://127.0.0.1:5000/restart");
});
