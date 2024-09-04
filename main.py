from pyscript import display,HTML
def click_handler1():
    display(HTML('''<br/><h1>Example1</h1><p>Simple example showing &lt;script type="py" &gt;.
    &lt;script type="py" terminal&gt; has both print and display where as &lt;script type="py" &gt; has only display  </p>
    <h6>index.html</h6>
    <pre style="background-color:#f1f1f1;">
    <code onmousedown="return false" onselectstart="return false">
&lt;!DOCTYPE html&gt;
&lt;html lang="en"&gt;
&lt;head&gt;
&lt;title&gt;Yellow Cloud&lt;/title&gt;
    &lt;meta charset="UTF-8"&gt;
    &lt;meta name="viewport" content="width=device-width,initial-scale=1.0"&gt;
    &lt;link rel="stylesheet" href="https://pyscript.net/releases/2024.7.1/core.css"&gt;
    &lt;script type="module" src="https://pyscript.net/releases/2024.7.1/core.js"&gt;&lt;/script&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;script type="py"&gt;
        from pyscript import display
        import os
        display("Hello World!") # this goes to the DOM
        for x in range(10):
            display(x)
    &lt;/script&gt;
&lt;/body&gt;
&lt;/html&gt;
</pre>
</code>
<h6>output</h6>
    '''),append=False)
    display("Hello World!",append=True) # this goes to the DOM
    for x in range(10):
        display(x)

