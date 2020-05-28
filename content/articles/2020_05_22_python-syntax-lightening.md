Title: An example for syntax highlight with Markdown
Date: 2019-10-20 11:20
Author: Jorge
Tags: python, tutorial
Slug: syntax-highlight-markdown
Summary: Syntax highlight

## Syntax highlight in Pelican

There are two ways to specify the identifier:

    :::python
        print("The triple-colon syntax will *not* show line numbers.")

To display line numbers, use a path-less shebang instead of colons:

    #!python
        print("The path-less shebang syntax *will* show line numbers.")
    
    
Syntax Highlight

    :::python
        import abc

 
<code class="stylecode">Take</code> a look about <code class="stylecode highlight">me</code>  and do not do anything    
       
Adding an image to text

![my_image](/images/screenshot.png "Image Title on mouse-over")


More highlight

    :::python
        #!/usr/bin/python3
        
        from engine import RunForrestRun
        
        """Test code for syntax highlighting!"""
        
        class Foo:
            def __init__(self, var):
                self.var = var
                self.run()
        
            def run(self):
                RunForrestRun()  # run along!