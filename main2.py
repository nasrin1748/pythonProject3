from pyscript import display,HTML
import random
def click_handler1():
    display(HTML('''<br/><h1>Example3</h1><p>Worker terminal accepts user inputs.</p>
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
    &lt;script type="mpy" worker terminal&gt;
        import random
        words = ["tiger", "tree", "underground", "giraffe", "chair"]
        word = random.choice(words)
        display = ["_"] * len(word)
        lives = 6
        while "_" in display and lives > 0:
              guess = input("Guess a letter: ")
              if guess in word:
                 for i in range(len(word)):
                     if word[i] == guess:
                        display[i] = guess
                 print(" ".join(display))
              else:
                 lives -= 1
                 print("Incorrect. You have", lives, "lives remaining.")
              print("=============================================")

        if "_" not in display:
              print("Congratulations! You have correctly guessed the word.")
        else:
              print("Sorry, you ran out of lives. The word was", word + ".")
    &lt;/script&gt;
&lt;/body&gt;
&lt;/html&gt;
</pre>
</code>
    '''),append=False)