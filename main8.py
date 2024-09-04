from pyscript import display,HTML,when
import pandas as pd
def click_handler1():
    display(HTML('''<br/><h1>Example9</h1><p>Example for reading text file as CSV using pandas DataFrame.Even the CSV file and the .xlsx file can be read in the same way just instead of .txt file name mention your .csv file or the .xlsx file name.</p>
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
      import pandas as pd
      from pyscript import display   
      df = pd.read_csv("read.txt", sep=",")
      pd.set_option("display.max_rows", None)    
      pd.set_option("display.max_columns", None)
      display(df)  
&lt;/script&gt;
&lt;/body&gt;
&lt;/html&gt; 
</pre>
</code>
<h5>pyscript.toml</h5>
<pre style="background-color:#f1f1f1;">
<code onmousedown="return false" onselectstart="return false">
"packages" = ["pandas","Jinja2"]
[files]
"read.txt" = "read.txt"
</pre>
</code>
<h5>output</h5>
    '''),append=False)
    df = pd.read_csv("read.txt", sep=",")
    pd.set_option("display.max_rows", None)
    pd.set_option("display.max_columns", None)
    display(df)

