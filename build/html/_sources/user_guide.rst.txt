
User Guide
==========

To use the Text Processing Tool, provide the path to the text file and use the following options:

Examples:
---------

1. Count the words in a file:
   ```bash
   python text_proc.py -f sample.txt -wc
   ```
.. image:: /_static/wc.png
   :alt: Word count example
   :width: 600px
2. Count the characters in a file:
   ```bash
   python text_proc.py -f sample.txt -cc
   ```
.. image:: /_static/cc.png
   :alt: Char count example
   :width: 600px

3. Find a specific word in a file:
   ```bash
   python text_proc.py -f sample.txt -find "example"
   ```
.. image:: /_static/occ.png
   :alt: Occuurence example
   :width: 600px

4. Replace a word in a file and save the output:
   ```bash
   python text_proc.py -f sample.txt -r "old" "new"
   ```
.. image:: /_static/replace.png
   :alt: Replace example
   :width: 600px
See Command-Line Tools for more details on all options.
