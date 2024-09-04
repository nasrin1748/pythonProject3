from pyscript import display, HTML, when, document
import io


def click_handler1():
    display(HTML('''<br/><h1>Example18</h1><p>Example to change terminal font.</p>
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
    &lt;style&gt;
    .xterm-rows {
        font-family: "gohu" !important;
    }
    &lt;/style&gt;
    &lt;script type="py" config="./pyscript.toml" terminal&gt;
        print("hello")
    &lt;/script&gt;
&lt;/body&gt;
&lt;/html&gt;
</code>
</pre>
    '''), append=False)
