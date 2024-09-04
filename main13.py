from pyscript import display,HTML,when,document
from main10 import add,subtract
import io
import pandas as pd
import html2text
def click_handler1():
    display(HTML('''<br/><h1>Example13</h1><p>Example showing on click increment value by 1.</p>
    <h5>index.html</h5>
    <pre style="background-color:#f1f1f1;">
    <code onmousedown="return false" onselectstart="return false">
&lt;!DOCTYPE html&gt;
&lt;html lang="en"&gt;
&lt;head&gt;
&lt;title&gt;Yellow Cloud&lt;/title&gt;
    &lt;meta charset="UTF-8"&gt;
    &lt;meta name="viewport" content="width=device-width,initial-scale=1.0"&gt;
    &lt;link rel="stylesheet" href="https://pyscript.net/releases/2024.8.1/core.css"&gt;
    &lt;script type="module" src="https://pyscript.net/releases/2024.8.1/core.js"&gt;&lt;/script&gt;
&lt;/head&gt;
&lt;body&gt;
  &lt;h1&gt;Item test&lt;/h1&gt;
  &lt;p&gt;item&lt;/p&gt;
  &lt;p id="item"&gt;1&lt;/p&gt;
  &lt;button py-click="addval"&gt;+&lt;/button&gt;
  &lt;script type="py" src="./main.py"  config="./pyscript.toml"&gt;&lt;/script&gt;
&lt;/body&gt;
&lt;/html&gt;
</pre>
</code>
<h5>main.py</h5>
<pre style="background-color:#f1f1f1;">
<code onmousedown="return false" onselectstart="return false">
from pyscript import document

def addval(event):
    q = document.querySelector("#item")
    q.innerText = (int(q.innerText)) + 1
</pre>
</code>
<h5>output</h5>
<h1>Item test</h1>
<p>item</p>
<p id="item">1</p>
<button id="addval">+</button>
    '''),append=False)
    @when("click", "#addval")
    def fun(event):
        q = document.querySelector("#item")
        q.innerText = (int(q.innerText)) + 1

