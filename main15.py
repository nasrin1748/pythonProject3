from pyscript import display,HTML,when,document
import io
def click_handler1():
    display(HTML('''<br/><h1>Example15</h1><p>Example for html,css and javascript live code editor.</p>
    <h5>index.html</h5>
    <pre style="background-color:#f1f1f1;">
    <code onmousedown="return false" onselectstart="return false">
&lt;!DOCTYPE html&gt;
&lt;html lang="en"&gt;
&lt;head&gt;
    &lt;meta charset="UTF-8"&gt;
    &lt;title&gt;Title&lt;/title&gt;
  &lt;link rel="stylesheet" href="style.css"&gt;
  &lt;script src="https://pyscript.net/releases/2024.8.1/core.js"
          crossorigin="anonymous"&gt;&lt;/script&gt;
&lt;/head&gt;
&lt;body&gt;
&lt;div class="container"&gt;
  &lt;div class="left"&gt;
    &lt;label&gt;&lt;i&gt;&lt;/i&gt;HTML&lt;/label&gt;
    &lt;textarea id="html-code" onkeyup="run()"&gt;&lt;/textarea&gt;
    &lt;label&gt;&lt;i&gt;&lt;/i&gt;CSS&lt;/label&gt;
    &lt;textarea id="css-code" onkeyup="run()"&gt;&lt;/textarea&gt;
    &lt;label&gt;&lt;i&gt;&lt;/i&gt;JavaScript&lt;/label&gt;
    &lt;textarea id="js-code" onkeyup="run()"&gt;&lt;/textarea&gt;
  &lt;/div&gt;
  &lt;div&gt;
    &lt;div class="right"&gt;
      &lt;label&gt;&lt;i&gt;&lt;/i&gt;Output&lt;/label&gt;
        &lt;iframe id="output"&gt;&lt;/iframe&gt;
    &lt;/div&gt;

  &lt;/div&gt;
&lt;/div&gt;
&lt;script src="./main.js"&gt;

    &lt;/script&gt;
&lt;/body&gt;
&lt;/html&gt;
</code>
</pre>
<h5>main.js</h5>
<pre style="background-color:#f1f1f1;">
<code onmousedown="return false" onselectstart="return false">
function run(){
              let htmlCode = document.getElementById("html-code").value;
              let cssCode = document.getElementById("css-code").value;
              let jsCode = document.getElementById("js-code").value;
              let output = document.getElementById("output");

              output.contentDocument.body.innerHTML = htmlCode+ "<style>" +cssCode+ "</style>";
              output.contentWindow.eval(jsCode);
        }
</pre>
</code>
<h5>style.css</h5>
<pre style="background-color:#f1f1f1;">
<code onmousedown="return false" onselectstart="return false">
*{
    margin: 0;
    padding: 0;
    font-family: 'Poppins' , sans-serif;
    box-sizing: border-box;
}
body{
    background: #454545;
    color: #fff;
}
.container{
    width: 100%;
    height: 100vh;
    padding: 20px;
    display: flex;
}
.left, .right{
    flex-basis: 50%;
    padding: 10px;
}
textarea{
    width: 100%;
    height: 28%;
    background: #1f1f1f;
    color: #fff;
    padding: 10px 20px;
    border: 0;
    outline: 0;
    font-size:18px;
}
iframe{
    width: 100vh;
    height: 90vh;
    background: #fff;
    border: 1;
    outline: 0;
}
label i{
    margin-right: 10px;
    margin-left: 10px;
}
label{
    display: flex;
    align-items: center;
    background: #000;
    height: 30px;
}
</code>
</pre>
<h5>output</h5>
<head>
  <link rel="stylesheet" href="style.css">
</head>
<body>
<div class="container">
  <div class="left">
    <label><i></i>HTML</label>
    <textarea id="html-code" onkeyup="run()"></textarea>
    <label><i></i>CSS</label>
    <textarea id="css-code" onkeyup="run()"></textarea>
    <label><i></i>JavaScript</label>
    <textarea id="js-code" onkeyup="run()"></textarea>
  </div>
  <div>
    <div class="right">
      <label><i></i>Output</label>
        <iframe id="output"></iframe>
    </div>

  </div>
</div>
<script src="./main.js">

    </script>
</body>
    '''),append=False)
