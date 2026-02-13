import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Valentine Proposal 💖", layout="centered")

html_code = """
<!DOCTYPE html>
<html>
<head>
<style>

body {
    margin: 0;
    overflow: hidden;
    text-align: center;
    font-family: 'Arial', sans-serif;
    background: linear-gradient(135deg, #ff9a9e, #fad0c4);
}

/* Floating hearts animation */
.heart {
    position: fixed;
    bottom: -20px;
    font-size: 24px;
    animation: floatUp 6s linear infinite;
}

@keyframes floatUp {
    0% {
        transform: translateY(0);
        opacity: 1;
    }
    100% {
        transform: translateY(-800px);
        opacity: 0;
    }
}

.container {
    position: relative;
    height: 400px;
    margin-top: 120px;
}

button {
    padding: 14px 30px;
    font-size: 20px;
    border-radius: 10px;
    border: none;
    cursor: pointer;
    transition: all 0.3s ease;
}

#yesBtn {
    background-color: #ff4b5c;
    color: white;
    margin-right: 30px;
}

#yesBtn:hover {
    transform: scale(1.1);
}

#noBtn {
    background-color: #444;
    color: white;
    position: absolute;
}

h1 {
    font-size: 36px;
    color: white;
    margin-top: 80px;
}

</style>
</head>

<body>

<h1>💖 Will you be my Valentine? 💖</h1>

<div class="container">
    <button id="yesBtn" onclick="yesClicked()">Yes 💕</button>
    <button id="noBtn">No 😢</button>
</div>

<script>

function yesClicked() {
    document.body.innerHTML = "<h1 style='color:white; margin-top:200px;'>Yayyyyy!!! 💍❤️ I knew it! 💖</h1>";
}

/* Moving + shrinking No button */
const noBtn = document.getElementById("noBtn");
let scale = 1;

noBtn.addEventListener("mouseover", function() {
    const container = document.querySelector(".container");
    const maxX = container.clientWidth - noBtn.offsetWidth;
    const maxY = container.clientHeight - noBtn.offsetHeight;

    const randomX = Math.floor(Math.random() * maxX);
    const randomY = Math.floor(Math.random() * maxY);

    noBtn.style.left = randomX + "px";
    noBtn.style.top = randomY + "px";

    scale -= 0.1;
    if (scale > 0.2) {
        noBtn.style.transform = "scale(" + scale + ")";
    }
});

/* Generate floating hearts */
function createHeart() {
    const heart = document.createElement("div");
    heart.classList.add("heart");
    heart.innerHTML = "💖";
    heart.style.left = Math.random() * 100 + "vw";
    heart.style.fontSize = (Math.random() * 20 + 20) + "px";
    heart.style.animationDuration = (Math.random() * 3 + 3) + "s";

    document.body.appendChild(heart);

    setTimeout(() => {
        heart.remove();
    }, 6000);
}

setInterval(createHeart, 300);

</script>

</body>
</html>
"""

components.html(html_code, height=600)
