window.addEventListener("scroll", function() {
    if(document.getElementById("article-container").scrollTop === 0) {
        var bg = document.getElementById("bg-overlay");
        var top = window.getComputedStyle(bg, null)["top"]
        bg.style.top = "" + (top - 1);
        console.log(top, document.getElementById("article-container").offsetTop);
    }
})