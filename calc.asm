section .data
    msg1 db "Addition: 8", 10
    msg2 db "Multiplication: 8", 10

section .text
    global _start

_start:
    ; --- Addition ---
    mov eax, 5      ; First number
    mov ebx, 3      ; Second number
    add eax, ebx    ; Result = 8

    ; Print "Addition: 8"
    mov eax, 4
    mov ebx, 1
    mov ecx, msg1
    mov edx, 12     ; length of message
    int 0x80

    ; --- Multiplication ---
    mov eax, 4      ; First number
    mov ebx, 2      ; Second number
    imul eax, ebx   ; Result = 8

    ; Print "Multiplication: 8"
    mov eax, 4
    mov ebx, 1
    mov ecx, msg2
    mov edx, 18     ; length of message
    int 0x80

    ; Exit
    mov eax, 1
    xor ebx, ebx
    int 0x80