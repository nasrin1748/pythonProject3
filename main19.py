from pyscript import display,HTML,when,document
import io
def click_handler1():
    display(HTML('''<br/><h1>Example19</h1><p>Example writing and reading a file.</p>
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
        &lt;script type="py" src="./main.py" config="./pyscript.toml" &gt;&lt;/script&gt;
&lt;/body&gt;
&lt;/html&gt;
</code>
</pre>
<h5>main.py</h5>
<pre style="background-color:#f1f1f1;">
<code onmousedown="return false" onselectstart="return false">
from pyscript import display
L = ["This is Delhi. &#x5c;n", "This is Paris. &#x5c;n", "This is London. &#x5c;n"]
 
# Creating a file
with open("myfile.py", "w") as file1:
    # Writing data to a file
    file1.write("hello. &#x5c;n")
    file1.writelines(L)
    file1.close()  # to change file access modes
 
with open("myfile.py", "r+") as file1:
    # Reading from a file
    display(file1.read())
</pre>
</code>
<h5>output</h5>
    '''),append=False)
    L = ["This is Delhi. \n", "This is Paris. \n", "This is London. \n"]

    # Creating a file
    with open("myfile.py", "w") as file1:
        # Writing data to a file
        file1.write("hello. \n")
        file1.writelines(L)
        file1.close()  # to change file access modes

    with open("myfile.py", "r+") as file1:
        # Reading from a file
        display(file1.read())
        # print(file1.read())
