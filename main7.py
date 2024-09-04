from pyscript import display, HTML, when, document
from datetime import datetime

now = datetime.now()


def click_handler1():
    display(HTML('''<br/><h1>Example8</h1><p>Example for calculating pizza cost @when decorator.</p>
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
&lt;div align="center"&gt;
        &lt;h1&gt;Dave's Pizza Place&lt;/h1&gt;
&lt;/div&gt;
&lt;div&gt;
    &lt;label for="datetime"&gt;Date:&lt;/label&gt;
     &ensp; &ensp; &ensp; &ensp;&lt;input type="date" id="input1" name="user_date" /&gt;
&lt;/div&gt;
&lt;div&gt;
    &lt;label for="firstname"&gt;Firstname:&lt;/label&gt;
     &ensp;&lt;input type="text" pattern="[A-Za-z-']+" id="input2" name="firstname" placeholder="firstname" maxlength="20"/>
&lt;/div&gt;
&lt;div&gt;
    &lt;label for="lastname"&gt;Lastname:&lt;/label&gt;
     &ensp;&lt;input type="text" pattern="[A-Za-z-']+" id="input3" name="lastname" placeholder="Lastname" maxlength="20"/&gt;
&lt;/div&gt; 
&lt;div&gt;
    &lt;label for="mail"&gt;Address:&lt;/label&gt;
     &ensp; &ensp;&lt;input type="text" name="user_mail" id="input4" placeholder="Full  Address"/&gt;
&lt;/div&gt;
&lt;div&gt;
    &lt;label for="tel"&gt;Phone#:&lt;/label&gt;
     &ensp; &ensp;&lt;input type="tel" id="input5" pattern="[0-9]+"" name="user_phone" placeholder="(403)123-1234"/&gt;
&lt;/div&gt;
&lt;p&gt;&lt;/p&gt;    
&lt;form&gt;
  &lt;fieldset&gt;
    &lt;legend&gt;Choose Your Pizza Type:&lt;/legend&gt;
    &lt;div&gt;
      &lt;input type="radio" id="8" name="contact" value="8"  checked/&gt;
      &lt;label for="contactChoice1"&gt;Small ($8)&lt;/label&gt;

      &lt;input type="radio" id="contactChoice2" name="contact" value="10" /&gt;
      &lt;label for="contactChoice2">Medium ($10)&lt;/label&gt;

      &lt;input type="radio" id="contactChoice3" name="contact" value="15" /&gt;
      &lt;label for="contactChoice3"&gt;Large ($15)&lt;/label&gt;

      &lt;input type="radio" id="contactChoice4" name="contact" value="18" /&gt;
      &lt;label for="contactChoice3"&gt;ExtraLarge ($18)&lt;/label&gt;  
    &lt;/div&gt;
  &lt;/fieldset&gt;
&lt;/form&gt;
&lt;p&gt;&lt;/p&gt;    
&lt;form&gt;
  &lt;fieldset&gt;
    &lt;legend&gt;Specialities:&lt;/legend&gt;
    &lt;div&gt;
      &lt;input type="radio" id="contactChoice1" name="contact1" value="3"  checked/&gt;
      &lt;label for="contactChoice1"&gt;Super Cheesy ($3)&lt;/label&gt;

      &lt;input type="radio" id="contactChoice2" name="contact1" value="5" /&gt;
      &lt;label for="contactChoice2"&gt;Extra Meaty ($5)&lt;/label&gt;

      &lt;input type="radio" id="contactChoice3" name="contact1" value="2" /&gt;
      &lt;label for="contactChoice3"&gt;Really Veggie ($2)&lt;/label&gt;
    &lt;/div&gt;
  &lt;/fieldset&gt;
&lt;/form&gt;
&lt;p&gt;&lt;/p&gt;  
&lt;form&gt;
  &lt;fieldset&gt;
    &lt;legend&gt;Extra Toppings:&lt;/legend&gt;
    &lt;div&gt;
      &lt;input type="checkbox" id="contactChoice1" name="contact2" value="1.5"  checked/&gt;
      &lt;label for="contactChoice1"&gt;Extra Cheese ($1.50)&lt;/label&gt;

      &lt;input type="checkbox" id="contactChoice2" name="contact2" value="1.50" /&gt;
      &lt;label for="contactChoice2"&gt;Pepperoni ($1.50)&lt;/label&gt;

      &lt;input type="checkbox" id="contactChoice3" name="contact2" value="1.50" /&gt;
      &lt;label for="contactChoice3"&gt;Mushrooms ($1.50)&lt;/label&gt;

      &lt;input type="checkbox" id="contactChoice4" name="contact2" value="1.50" /&gt;
      &lt;label for="contactChoice4"&gt;Bacon ($1.50)&lt;/label&gt;

      &lt;input type="checkbox" id="contactChoice5" name="contact2" value="1.50" /&gt;
      &lt;label for="contactChoice5"&gt;Olives ($1.50)&lt;/label&gt;  
    &lt;/div&gt;
  &lt;/fieldset&gt;
&lt;/form&gt; 
&lt;p&gt;&lt;/p&gt; 
&lt;button id="add" onclick='myFunction'&gt;Price Your pizza&lt;/button&gt;           
&lt;script type="py" &gt;
from pyscript import display,when
from datetime import datetime
now = datetime.now() 
@when("click","#add")    
def myFunction(event): 
       from pyscript import document
       Date = document.getElementById("input1").value
       Firstname = document.getElementById("input2").value
       Lastname = document.getElementById("input3").value
       Address = document.getElementById("input4").value
       Phone = document.getElementById("input5").value
       t = now.strftime("%m/%d/%Y, %H:%M:%S")
       rate2=[]
       rate = document.querySelector('input[name="contact"]:checked').value
       rate1 = document.querySelector('input[name="contact1"]:checked').value
       checkboxes = document.querySelectorAll('input[type=checkbox]:checked')
       for i in range(checkboxes.length):
           rate2.append(checkboxes[i].value)
       display(f"Today is: {t}")
       display(f"Date: {Date}")
       display(f"Firstname: {Firstname}")
       display(f"Lastname: {Lastname}")
       display(f"Address: {Address}")
       display(f"Phone: {Phone}")
       s1 = list(map(float, rate2))
       s1 = (sum(s1))
       t = int(rate)+int(rate1)+int(s1)
       display(f"Total: {t}"+f"$")
&lt;/script&gt;
&lt;/body&gt;
&lt;/html&gt; 
</pre>
</code>
<p>The following example calculates pizza cost for you.</p>
<div id="div-01">
<div align="center">
        <h1>Dave's Pizza Place</h1>
</div>
<div>
    <label for="datetime">Date:</label>
     &ensp; &ensp; &ensp; &ensp;<input type="date" id="input1" name="user_date" />
</div>
<div>
    <label for="firstname">Firstname:</label>
     &ensp;<input type="text" pattern="[A-Za-z-']+" id="input2" name="firstname" placeholder="firstname" maxlength="20"/>
</div>
<div>
    <label for="lastname">Lastname:</label>
     &ensp;<input type="text" pattern="[A-Za-z-']+" id="input3" name="lastname" placeholder="Lastname" maxlength="20"/>
</div> 
<div>
    <label for="mail">Address:</label>
     &ensp; &ensp;<input type="text" name="user_mail" id="input4" placeholder="Full  Address"/>
</div>
<div>
    <label for="tel">Phone#:</label>
     &ensp; &ensp;<input type="tel" id="input5" pattern="[0-9]+"" name="user_phone" placeholder="(403)123-1234"/>
</div>
<p></p>    
<form>
  <fieldset>
    <legend>Choose Your Pizza Type:</legend>
    <div>
      <input type="radio" id="8" name="contact" value="8"  checked/>
      <label for="contactChoice1">Small ($8)</label>

      <input type="radio" id="contactChoice2" name="contact" value="10" />
      <label for="contactChoice2">Medium ($10)</label>

      <input type="radio" id="contactChoice3" name="contact" value="15" />
      <label for="contactChoice3">Large ($15)</label>

      <input type="radio" id="contactChoice4" name="contact" value="18" />
      <label for="contactChoice3">ExtraLarge ($18)</label>  
    </div>
  </fieldset>
</form>
<p></p>    
<form>
  <fieldset>
    <legend>Specialities:</legend>
    <div>
      <input type="radio" id="contactChoice1" name="contact1" value="3"  checked/>
      <label for="contactChoice1">Super Cheesy ($3)</label>

      <input type="radio" id="contactChoice2" name="contact1" value="5" />
      <label for="contactChoice2">Extra Meaty ($5)</label>

      <input type="radio" id="contactChoice3" name="contact1" value="2" />
      <label for="contactChoice3">Really Veggie ($2)</label>
    </div>
  </fieldset>
</form> 
<p></p>    
<form>
  <fieldset>
    <legend>Extra Toppings:</legend>
    <div>
      <input type="checkbox" id="contactChoice1" name="contact2" value="1.5"  checked/>
      <label for="contactChoice1">Extra Cheese ($1.50)</label>

      <input type="checkbox" id="contactChoice2" name="contact2" value="1.50" />
      <label for="contactChoice2">Pepperoni ($1.50)</label>

      <input type="checkbox" id="contactChoice3" name="contact2" value="1.50" />
      <label for="contactChoice3">Mushrooms ($1.50)</label>

      <input type="checkbox" id="contactChoice4" name="contact2" value="1.50" />
      <label for="contactChoice4">Bacon ($1.50)</label> 

      <input type="checkbox" id="contactChoice5" name="contact2" value="1.50" />
      <label for="contactChoice5">Olives ($1.50)</label>  
    </div>
  </fieldset>
</form> 
<p></p> 
<button id="add">Price Your pizza</button>
<p></p></div>
    '''), append=False)

    @when("click", "#add")
    def myFunction(event):
        Date = document.getElementById("input1").value
        Firstname = document.getElementById("input2").value
        Lastname = document.getElementById("input3").value
        Address = document.getElementById("input4").value
        Phone = document.getElementById("input5").value
        t = now.strftime("%m/%d/%Y, %H:%M:%S")
        rate2 = []
        rate = document.querySelector('input[name="contact"]:checked').value
        rate1 = document.querySelector('input[name="contact1"]:checked').value
        checkboxes = document.querySelectorAll('input[type=checkbox]:checked')
        for i in range(checkboxes.length):
            rate2.append(checkboxes[i].value)
        display(f"Today is: {t}")
        display(f"Date: {Date}")
        display(f"Firstname: {Firstname}")
        display(f"Lastname: {Lastname}")
        display(f"Address: {Address}")
        display(f"Phone: {Phone}")
        s1 = list(map(float, rate2))
        s1 = (sum(s1))
        t = int(rate) + int(rate1) + int(s1)
        display(f"Total: {t}" + f"$")
