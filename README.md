# CS-117-Lab-3
1. Assembly Reflections
Using Assembly felt very different from regular coding. We noticed that everything depends on registers, and you have to be super specific with each instruction. It’s like giving step-by-step directions to the computer with no shortcuts. Compared to Python, Assembly is way more low-level and harder to follow. Even simple tasks take more effort and lines of code.

2. Python Reflections
Python made the same calculator project much easier. It’s faster to write, and you don’t have to worry about memory or hardware stuff. Things like variables, loops, and functions help keep the code clean and organized. You can do more with less code, and it’s easier to test and fix mistakes too.

3.Comparison Table:
| Feature | Assembly Example | Python Example | Notes |
| :--- | :--- | :--- | :--- |
| **Variable storage** | Register (EAX) | `x = 5` | Assembly stores data primarily in hardware registers (like EAX) or memory. Python uses named variables as abstract containers. |
| **Printing output** | `INT 21h` | `print()` | Assembly requires a system call (`INT 21h` in DOS/x86) to interact directly with the OS. Python uses a high-level function that handles the system calls implicitly. |
| **Arithmetic** | `ADD AX, BX` | `x + y` | Assembly uses mnemonics (`ADD`) on registers (AX, BX). Python uses standard mathematical operators (`+`) on named variables. |
