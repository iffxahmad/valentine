import streamlit as st
import streamlit.components.v1 as components

# Make page wide
st.set_page_config(layout="wide")

# Remove Streamlit padding/margins
st.markdown("""
    <style>
        .block-container {
            padding: 0rem;
        }
        iframe {
            height: 100vh !important;
        }
    </style>
""", unsafe_allow_html=True)

html_code = """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>

html, body {
    margin: 0;
    padding: 0;
    width: 100%;
    height: 100%;
    overflow: hidden;
    background: linear-gradient(135deg, #ff9a9e, #fad0c4);
    font-family: Arial, sans-serif;
}

.container {
    position: relative;
    height: 100vh;
    width: 100vw;
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
}

button {
    padding: 14px 30px;
    font-size: 20px;
    border-radius: 10px;
    border: none;
    cursor: pointer;
    transition: 0.3s;
}

#yesBtn {
    background-color: #ff4b5c;
    color: white;
    margin: 20px;
}

#noBtn {
    background-color: #333;
    color: white;
    position: absolute;
}

</style>
</head>

<body>

<div class="container">
    <h1>💖 Muhammad Hussain! Will you be my Valentine? 💖</h1>
    <button id="yesBtn" onclick="yesClicked()">Yes 💕</button>
    <button id="noBtn">No 😢</button>
</div>

<script>

function yesClicked() {
    document.body.innerHTML =
        "<h1 style='color:white; text-align:center; margin-top:40vh;'>Yayyyy!!! ❤️</h1> <p>Distance may keep us apart, but it can never reduce the love I feel for you. Every mile between us only makes my heart grow fonder. You are my peace, my dua and my forever.</p><p>On this Valentine's Day I just want you to know that no matter how far you are, you live in my heart every single second.</p>";
}

const noBtn = document.getElementById("noBtn");
let scale = 1;

noBtn.addEventListener("mouseover", function() {
    const maxX = window.innerWidth - noBtn.offsetWidth;
    const maxY = window.innerHeight - noBtn.offsetHeight;

    const randomX = Math.random() * maxX;
    const randomY = Math.random() * maxY;

    noBtn.style.left = randomX + "px";
    noBtn.style.top = randomY + "px";

    scale -= 0.1;
    if (scale > 0.2) {
        noBtn.style.transform = "scale(" + scale + ")";
    }
});

</script>

</body>
</html>
"""

components.html(html_code, height=800, scrolling=False)
