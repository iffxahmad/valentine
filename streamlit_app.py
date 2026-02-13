html_code = """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>

html, body {
    margin: 0;
    padding: 0;
    height: 100%;
    width: 100%;
    overflow: hidden;
    font-family: 'Poppins', sans-serif;
    background: linear-gradient(135deg, #ff758c, #ff7eb3);
    color: white;
}

/* Center everything perfectly */
.container {
    height: 100vh;
    width: 100vw;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
    padding: 20px;
}

h1 {
    font-size: 42px;
    margin-bottom: 30px;
    text-shadow: 0px 4px 15px rgba(0,0,0,0.3);
}

p {
    font-size: 20px;
    max-width: 700px;
    line-height: 1.6;
    margin-top: 15px;
}

/* Buttons */
button {
    padding: 14px 35px;
    font-size: 20px;
    border-radius: 50px;
    border: none;
    cursor: pointer;
    transition: 0.3s ease;
    margin: 10px;
}

#yesBtn {
    background: white;
    color: #ff4b5c;
    font-weight: bold;
    box-shadow: 0px 5px 20px rgba(0,0,0,0.3);
}

#yesBtn:hover {
    transform: scale(1.1);
}

#noBtn {
    background: rgba(0,0,0,0.6);
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
    document.body.innerHTML = `
    <div class="container">
        <h1>Yayyyy!!! ❤️</h1>
        <p>
        Distance may keep us apart, but it can never reduce the love I feel for you.
        Every mile between us only makes my heart grow fonder.
        You are my peace, my dua and my forever.
        </p>
        <p>
        On this Valentine's Day I just want you to know that
        no matter how far you are, you live in my heart every single second.
        </p>
    </div>
    `;
}

/* Moving + shrinking No button */
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
