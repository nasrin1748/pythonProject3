from pyscript import display,HTML,when
from main10 import add,subtract
import io
import pandas as pd
import html2text
def click_handler1():
    display(HTML('''<br/><h1>Example12</h1><p>Example for rendered HTML table to pandas dataframe.</p>
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
html_content = '&lt;tr&gt;&lt;th&gt;Data 1&lt;/th&gt;&lt;th&gt;Data 2
&lt;/th&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;Calcutta&lt;/td&gt;&lt;td&gt;
Orange&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;
Robots&lt;/td&gt;&lt;td&gt;Jazz&lt;/td&gt;&lt;/tr&gt;'
text_content = html2text.html2text(html_content) 
df = io.StringIO(text_content)
df = pd.read_csv(df, sep="|")

def highlight_col(x):
        r = 'color: red'
        df1 = pd.DataFrame('', index=x.index, columns=x.columns)
        df1.iloc[:, 0] = r
        return df1  
<pre>        
html = df.style.apply(highlight_col, axis=None) &#8726;	
         .set_table_attributes('border="5" class="dataframe table table-hover table-bordered"') &#8726;	
</pre>
display(html)
</pre>
</code>
</pre>
</code>
<h5>pyscript.toml</h5>
<pre style="background-color:#f1f1f1;">
<code onmousedown="return false" onselectstart="return false">
packages = [ "pandas", "html2text", "jinja2", "numpy"]
</pre>
</code>
<h5>output</h5>
    '''),append=False)
    html_content = '<tr><th>Data 1</th><th>Data 2</th></tr><tr><td>Calcutta</td><td>Orange</td></tr><tr><td>Robots</td><td>Jazz</td></tr>'
    text_content = html2text.html2text(html_content)
    df = io.StringIO(text_content)
    df = pd.read_csv(df, sep="|")
    def highlight_col(x):
        r = 'color: red'
        df1 = pd.DataFrame('', index=x.index, columns=x.columns)
        df1.iloc[:, 0] = r
        return df1
    html = df.style.apply(highlight_col, axis=None) \
             .set_table_attributes('border="5" class="dataframe table table-hover table-bordered"') \

    display(html)

