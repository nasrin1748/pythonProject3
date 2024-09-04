from pyscript import display,HTML,when,document
import io
def click_handler1():
    display(HTML('''<br/><h1>Example16</h1><p>Example to show function with parameter.</p>
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
    &lt;py-config&gt;
        [[fetch]]
        files = ["./main.py"]
    &lt;/py-config&gt;
     &lt;script type="py" terminal&gt;
        from main import fun
        from pyscript import display 
        fun(1,2)
    &lt;/script&gt;
&lt;/body&gt;
&lt;/html&gt;
</code>
</pre>
<h5>main.py</h5>
<pre style="background-color:#f1f1f1;">
<code onmousedown="return false" onselectstart="return false">
def fun(x,y):
    c = f"{int(x)+int(y)}"
    print(c)
    print(x)
    print(y)
</pre>
</code>
    '''),append=False)
