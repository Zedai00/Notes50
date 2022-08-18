<main class="col-md">
 <h1 id="indoor-voice">
  Indoor Voice
 </h1>
 <p>
  WRITING IN ALL CAPS IS LIKE YELLING.
 </p>
 <p>
  Best to use your "indoor voice" sometimes, writing entirely in lowercase.
 </p>
 <p>
  In a file called
  <code class="language-plaintext highlighter-rouge">
   indoor.py
  </code>
  , implement a program in Python that prompts the user for input and then outputs that same input in lowercase. Punctuation and whitespace should be outputted unchanged. You’re welcome, but not required, to prompt the user explicitly, as by passing a
  <code class="language-plaintext highlighter-rouge">
   str
  </code>
  of your own as an argument to
  <code class="language-plaintext highlighter-rouge">
   input
  </code>
  .
 </p>
 <details>
  <summary>
   Hints
  </summary>
  <ul>
   <li data-marker="*">
    Recall that
    <code class="language-plaintext highlighter-rouge">
     input
    </code>
    returns a
    <code class="language-plaintext highlighter-rouge">
     str
    </code>
    , per
    <a href="https://docs.python.org/3/library/functions.html#input">
     docs.python.org/3/library/functions.html#input
    </a>
    .
   </li>
   <li data-marker="*">
    Recall that a
    <code class="language-plaintext highlighter-rouge">
     str
    </code>
    comes with quite a few methods, per
    <a href="https://docs.python.org/3/library/stdtypes.html#string-methods">
     docs.python.org/3/library/stdtypes.html#string-methods
    </a>
    .
   </li>
  </ul>
 </details>
 <h2 id="before-you-begin">
  Before You Begin
 </h2>
 <p>
  Execute
  <code class="language-plaintext highlighter-rouge">
   cd
  </code>
  by itself in your terminal window. You should find that your terminal window’s prompt resembles the below:
 </p>
 <div class="language-plaintext highlighter-rouge">
  <div class="highlight">
   <pre class="highlight"><code>$
</code></pre>
  </div>
 </div>
 <p>
  Next execute
 </p>
 <div class="language-plaintext highlighter-rouge">
  <div class="highlight">
   <pre class="highlight"><code>mkdir indoor
</code></pre>
  </div>
 </div>
 <p>
  to make a folder called
  <code class="language-plaintext highlighter-rouge">
   indoor
  </code>
  in your codespace.
 </p>
 <p>
  Then execute
 </p>
 <div class="language-plaintext highlighter-rouge">
  <div class="highlight">
   <pre class="highlight"><code>cd indoor
</code></pre>
  </div>
 </div>
 <p>
  to change directories into that folder. You should now see your terminal prompt as
  <code class="language-plaintext highlighter-rouge">
   indoor/ $
  </code>
  . You can now execute
 </p>
 <div class="language-plaintext highlighter-rouge">
  <div class="highlight">
   <pre class="highlight"><code>code indoor.py
</code></pre>
  </div>
 </div>
 <p>
  to make a file called
  <code class="language-plaintext highlighter-rouge">
   indoor.py
  </code>
  where you’ll write your program.
 </p>
 <h2 id="demo">
  Demo
 </h2>
 <script async="" data-autoplay="1" data-cols="80" data-loop="1" data-rows="12" id="asciicast-DiHcvM4AXgniW4bxnXRTfNdJm" src="https://asciinema.org/a/DiHcvM4AXgniW4bxnXRTfNdJm.js">
 </script>
 <h2 id="how-to-test">
  How to Test
 </h2>
 <p>
  Here’s how to test your code manually.  At the
  <code class="language-plaintext highlighter-rouge">
   indoor/ $
  </code>
  prompt in your terminal: :
 </p>
 <ul>
  <li data-marker="*">
   Run your program with
   <code class="language-plaintext highlighter-rouge">
    python indoor.py
   </code>
   . Type
   <code class="language-plaintext highlighter-rouge">
    HELLO
   </code>
   and press Enter. Your program should output
   <code class="language-plaintext highlighter-rouge">
    hello
   </code>
   .
  </li>
  <li data-marker="*">
   Run your program with
   <code class="language-plaintext highlighter-rouge">
    python indoor.py
   </code>
   . Type
   <code class="language-plaintext highlighter-rouge">
    THIS IS CS50
   </code>
   and press Enter. Your program should output
   <code class="language-plaintext highlighter-rouge">
    this is cs50
   </code>
   .
  </li>
  <li data-marker="*">
   Run your program with
   <code class="language-plaintext highlighter-rouge">
    python indoor.py
   </code>
   . Type
   <code class="language-plaintext highlighter-rouge">
    50
   </code>
   and press Enter. Your program should output
   <code class="language-plaintext highlighter-rouge">
    50
   </code>
   .
  </li>
 </ul>
 <p>
  If you run into an error saying your file cannot be opened, retrace your steps to be sure that you are inside your
  <code class="language-plaintext highlighter-rouge">
   indoor
  </code>
  folder and have saved your
  <code class="language-plaintext highlighter-rouge">
   indoor.py
  </code>
  file there.  Remember how?
 </p>
 <p>
  You can execute the below to check your code using
  <code class="language-plaintext highlighter-rouge">
   check50
  </code>
  , a program that CS50 will use to test your code when you submit. But be sure to test it yourself as well!
 </p>
 <div class="language-plaintext highlighter-rouge">
  <div class="highlight">
   <pre class="highlight"><code>check50 cs50/problems/2022/python/indoor
</code></pre>
  </div>
 </div>
 <p>
  Green smilies mean your program has passed a test! Red frownies will indicate your program output something unexpected. Visit the URL that
  <code class="language-plaintext highlighter-rouge">
   check50
  </code>
  outputs to see the input
  <code class="language-plaintext highlighter-rouge">
   check50
  </code>
  handed to your program, what output it expected, and what output your program actually gave.
 </p>
 <h2 id="how-to-submit">
  How to Submit
 </h2>
 <p>
  In your terminal, execute the below to submit your work.
 </p>
 <div class="language-plaintext highlighter-rouge">
  <div class="highlight">
   <pre class="highlight"><code>submit50 cs50/problems/2022/python/indoor
</code></pre>
  </div>
 </div>
</main>
