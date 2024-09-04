from pyscript import display,HTML,when
from main10 import add,subtract
def click_handler1():
    display(HTML('''<br/><h1>Example10</h1><p>Example to import main.py file to main thread and make use of the functions.</p>
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
&lt;script type="py" config="./pyscript.toml"&gt;
    from pyscript import display    
    from main import add
    display(add(10,20))
    from main import subtract
    display(subtract(20,10))   
&lt;/script&gt;
&lt;/body&gt;
&lt;/html&gt;
</pre>
</code>
<h5>main.py</h5>
<pre style="background-color:#f1f1f1;">
<code onmousedown="return false" onselectstart="return false">
def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2
</pre>
</code>
</pre>
</code>
<h5>pyscript.toml</h5>
<pre style="background-color:#f1f1f1;">
<code onmousedown="return false" onselectstart="return false">
[[fetch]]
files = ["./main.py"]
</pre>
</code>
<h5>output</h5>
    '''),append=False)
    display(add(10,20))
    display(subtract(20,10))

