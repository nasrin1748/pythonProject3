from pyscript import display, HTML, when, document


def click_handler1():
    display(HTML('''<br/><h1>Example7</h1><p>Example for Adding two numbers using @when decorator using main.py</p>
    <h5>main.py</h5>
    <pre style="background-color:#f1f1f1;">
    <code onmousedown="return false" onselectstart="return false">
from pyscript import display,HTML,when
display(HTML("""&lt;div id="div-01"&gt;&lt;h1&gt;Addition Calculator&lt;/h1&gt;
&lt;p&gt;input 1: &lt;input id="input1" size="5"/&gt;&lt;/p&gt;&lt;br&gt;
&lt;p&gt;input 2: &lt;input id="input2" size="5"/&gt;&lt;/p&gt;&lt;br&gt;
&lt;button id="add"&gt;Submit&lt;/button&gt;
&lt;p&gt;&lt;/p&gt;&lt;/div&gt;"""))
@when("click", "#add")    
def myFunction(event):
       from pyscript import document
       num1 = document.getElementById("input1").value
       num2 = document.getElementById("input2").value
       c = f"{int(num1)+int(num2)}"
       display(f"input 1: {num1}")
       display(f"input 2: {num2}")
       display(f"Answer: {c}")
</pre>
</code>
<p>The following example displays Addition of two numbers taken from input1 and input2.</p>
<div id="div-01">
<h6>Output</h6>
<p>input 1: <input id="input1" size="5"/></p><br>
<p>input 2: <input id="input2" size="5"/></p><br>
<button id="add">Submit</button>
<p></p></div>
    '''), append=False)

    @when("click", "#add")
    def add(event):
        num1 = document.getElementById("input1").value
        num2 = document.getElementById("input2").value
        c = f"{int(num1) + int(num2)}"
        display(f"input 1: {num1}", append=True)
        display(f"input 2: {num2}", append=True)
        display(f"Answer: {c}", append=True)
