from pyscript import display,HTML,when,document
from main10 import subtract
from pyscript import display
import js
def click_handler1():
    display(HTML('''<br/><h1>Example14</h1><p>Example showing how to get python and javascript together.It's like reusablility of the code.For supposer one of the users in the team knows python and other know javascript how both can work on different modules and get their work together. </p>
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
      &lt;py-config&gt;
        [[fetch]]
        files = ["./main.py"]
      &lt;/py-config&gt;
&lt;script type="py" terminal&gt;
from main import subtract
from pyscript import display          
import js
x=subtract(8, 4)
display("from python",x)
result = js.square(4)
display("from js",result)
display("combined",x+result)
&lt;/script&gt;
&lt;script src="./main.js"&gt;

&lt;/script&gt;
</body>
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
<h5>main.js</h5>
<pre style="background-color:#f1f1f1;">
<code onmousedown="return false" onselectstart="return false">
function square(number) {
        return number * number;
}
</pre>
</code>
<h5>output</h5>
    <script src="./main.js">

    </script>
</body>
    '''),append=False)
    x = subtract(8, 4)
    display("from python", x)
    result = js.square(4)
    display("from js", result)
    display("combined", x + result)


