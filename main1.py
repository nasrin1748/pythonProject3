from pyscript import display,HTML,window
import time
def click_handler1():
    display(HTML('''<br/><h1>Example2</h1><p>Taking user inputs.Non worker terminal is dependent on windows prompt for user inputs.</p>
    <h5>Example for non worker terminal</h5>
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
    &lt;script type="py"&gt;
        from pyscript import window,display
        import time  
        a = window.prompt()
        display("You entered", a)
        time.sleep(1)  
        b = window.prompt()
        display("You entered", b)
        time.sleep(1)
    &lt;/script&gt;
&lt;/body&gt;
&lt;/html&gt;
</pre>
</code>
<h5>output</h5>
    '''),append=False)
    a = window.prompt()
    display("You entered", a)
    time.sleep(1)
    b = window.prompt()
    display("You entered", b)
    time.sleep(1)

