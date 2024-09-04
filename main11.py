from pyscript import display,HTML,when
from main10 import add,subtract
import html2text
def click_handler1():
    display(HTML('''<br/><h1>Example11</h1><p>Example for rendered HTML to plain text using pyscript.</p>
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
&lt;script type="py" src="./main.py" config="./pyscript.toml"&gt;&lt;/script&gt;
&lt;/body&gt;
&lt;/html&gt;
</pre>
</code>
<h5>main.py</h5>
<pre style="background-color:#f1f1f1;">
<code onmousedown="return false" onselectstart="return false">
from pyscript import display,HTML
import html2text
html_content = '&lt;html&gt;hello&lt;/html&gt;' 
text_content = html2text.html2text(html_content) 
display(text_content)
</pre>
</code>
</pre>
</code>
<h5>pyscript.toml</h5>
<pre style="background-color:#f1f1f1;">
<code onmousedown="return false" onselectstart="return false">
packages = ["html2text"]
</pre>
</code>
<h5>output</h5>
    '''),append=False)
    html_content = '<html>hello</html>'
    text_content = html2text.html2text(html_content)
    display(text_content)

