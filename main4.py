from pyscript import display,HTML,when,document
from datetime import datetime
now = datetime.now()
import random
def click_handler1():
    display(HTML('''<br/><h1>Example5</h1><p>Example for Calling function on button click using @when decorator.</p>
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
&lt;button id="ex" onclick='Example2'&gt;Example2&lt;/button&gt;
&lt;script type="py"&gt;
from pyscript import when,display  
from datetime import datetime 
now = datetime.now()        
@when("click", "#ex")             
def fun(event):
    display(now.strftime("%m/%d/%Y, %H:%M:%S"))
&lt;/script&gt;
&lt;/body&gt;
&lt;/html&gt;
</pre>
</code>
<p>The following example displays date and time on  DOM on button click.</p>
<div id="div-01">
<h6>Output</h6>
<button id="add">Date&Time</button>
<p></p></div>
    '''),append=False)
    @when("click", "#add")
    def add(event):
            display(now.strftime("%m/%d/%Y, %H:%M:%S"),append=True)