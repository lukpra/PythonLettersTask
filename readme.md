Python letters task:
About: Rewrite a given string with signs from the source file. Each sign from input string should have a corresponding
place / id from the source file. First sign has id 1, second 2 and so on. Each space can be replaced with id 0 which is
reserved for them, while every other sign should have a unique and rising ids. When rewriting letters, remember to keep them
in their form from the source. For eg. in -> "aAa" -> source "AbaA" will produce a string of "AaA".

If string is impossible to build, script should return error code 1.

Add unit tests, and try to optimise it for execution time first, then memory.

Requirements: Python 3. Python 2 has problems with ASCII encodings.
Usage: python task.py in.txt pant.txt
where: in.txt contains string that needs to be rewritten. pant.txt is a sample text, where script will look for letters to rewrite in.txt
Example: python task.py in.txt pant.txt
where:
in.txt -> Hello Github!

out.txt -> heLlo github!


[604, 27, 1, 47, 5, 0, 67, 2, 3, 814, 108, 58, 6]