# TODO: Something
def find_string(haystack, needle):
    if not haystack or not needle:
        return []

    n, m = len(haystack), len(needle)
    if m > n:
        return []

    # ASCII
    base = 256      
    # limiter  
    mod = 10**9 + 7 

    needle_hash = 0
    window_hash = 0
    h = 1  

    for i in range(m - 1):
        h = (h * base) % mod

    for i in range(m):
        needle_hash = (base * needle_hash + ord(needle[i])) % mod
        window_hash = (base * window_hash + ord(haystack[i])) % mod

    result = []
    for i in range(n - m + 1):
        if needle_hash == window_hash:
            # for collision
            if haystack[i:i + m] == needle:
                result.append(i)

        # update hash
        if i < n - m:
            window_hash = (base * (window_hash - ord(haystack[i]) * h) + ord(haystack[i + m])) % mod

            if window_hash < 0:
                window_hash += mod

    return result

# TODO: Something

def find_todo_lines(file_path):
    todo_lines = []
    file = open(file_path, 'r', encoding='utf-8')
    line_number = 1
    while True:
        line = file.readline()
        if not line:
            break
        if find_string(line, "TODO"):
            todo_lines.append(line_number)
        line_number += 1
    file.close()
    return todo_lines

# TODO: Something
def find_string(haystack, needle):
    if not haystack or not needle:
        return []

    n, m = len(haystack), len(needle)
    if m > n:
        return []

    # ASCII
    base = 256      
    # limiter  
    mod = 10**9 + 7 

    needle_hash = 0
    window_hash = 0
    h = 1  

    for i in range(m - 1):
        h = (h * base) % mod

    for i in range(m):
        needle_hash = (base * needle_hash + ord(needle[i])) % mod
        window_hash = (base * window_hash + ord(haystack[i])) % mod

    result = []
    for i in range(n - m + 1):
        if needle_hash == window_hash:
            # for collision
            if haystack[i:i + m] == needle:
                result.append(i)

        # update hash
        if i < n - m:
            window_hash = (base * (window_hash - ord(haystack[i]) * h) + ord(haystack[i + m])) % mod

            if window_hash < 0:
                window_hash += mod

    return result

# TODO: Something

def find_todo_lines(file_path):
    todo_lines = []
    file = open(file_path, 'r', encoding='utf-8')
    line_number = 1
    while True:
        line = file.readline()
        if not line:
            break
        if find_string(line, "TODO"):
            todo_lines.append(line_number)
        line_number += 1
    file.close()
    return todo_lines

# TODO: Something
def find_string(haystack, needle):
    if not haystack or not needle:
        return []

    n, m = len(haystack), len(needle)
    if m > n:
        return []

    # ASCII
    base = 256      
    # limiter  
    mod = 10**9 + 7 

    needle_hash = 0
    window_hash = 0
    h = 1  

    for i in range(m - 1):
        h = (h * base) % mod

    for i in range(m):
        needle_hash = (base * needle_hash + ord(needle[i])) % mod
        window_hash = (base * window_hash + ord(haystack[i])) % mod

    result = []
    for i in range(n - m + 1):
        if needle_hash == window_hash:
            # for collision
            if haystack[i:i + m] == needle:
                result.append(i)

        # update hash
        if i < n - m:
            window_hash = (base * (window_hash - ord(haystack[i]) * h) + ord(haystack[i + m])) % mod

            if window_hash < 0:
                window_hash += mod

    return result

# TODO: Something

def find_todo_lines(file_path):
    todo_lines = []
    file = open(file_path, 'r', encoding='utf-8')
    line_number = 1
    while True:
        line = file.readline()
        if not line:
            break
        if find_string(line, "TODO"):
            todo_lines.append(line_number)
        line_number += 1
    file.close()
    return todo_lines

# TODO: Something
def find_string(haystack, needle):
    if not haystack or not needle:
        return []

    n, m = len(haystack), len(needle)
    if m > n:
        return []

    # ASCII
    base = 256      
    # limiter  
    mod = 10**9 + 7 

    needle_hash = 0
    window_hash = 0
    h = 1  

    for i in range(m - 1):
        h = (h * base) % mod

    for i in range(m):
        needle_hash = (base * needle_hash + ord(needle[i])) % mod
        window_hash = (base * window_hash + ord(haystack[i])) % mod

    result = []
    for i in range(n - m + 1):
        if needle_hash == window_hash:
            # for collision
            if haystack[i:i + m] == needle:
                result.append(i)

        # update hash
        if i < n - m:
            window_hash = (base * (window_hash - ord(haystack[i]) * h) + ord(haystack[i + m])) % mod

            if window_hash < 0:
                window_hash += mod

    return result

# TODO: Something

def find_todo_lines(file_path):
    todo_lines = []
    file = open(file_path, 'r', encoding='utf-8')
    line_number = 1
    while True:
        line = file.readline()
        if not line:
            break
        if find_string(line, "TODO"):
            todo_lines.append(line_number)
        line_number += 1
    file.close()
    return todo_lines

# TODO: Something
def find_string(haystack, needle):
    if not haystack or not needle:
        return []

    n, m = len(haystack), len(needle)
    if m > n:
        return []

    # ASCII
    base = 256      
    # limiter  
    mod = 10**9 + 7 

    needle_hash = 0
    window_hash = 0
    h = 1  

    for i in range(m - 1):
        h = (h * base) % mod

    for i in range(m):
        needle_hash = (base * needle_hash + ord(needle[i])) % mod
        window_hash = (base * window_hash + ord(haystack[i])) % mod

    result = []
    for i in range(n - m + 1):
        if needle_hash == window_hash:
            # for collision
            if haystack[i:i + m] == needle:
                result.append(i)

        # update hash
        if i < n - m:
            window_hash = (base * (window_hash - ord(haystack[i]) * h) + ord(haystack[i + m])) % mod

            if window_hash < 0:
                window_hash += mod

    return result

# TODO: Something

def find_todo_lines(file_path):
    todo_lines = []
    file = open(file_path, 'r', encoding='utf-8')
    line_number = 1
    while True:
        line = file.readline()
        if not line:
            break
        if find_string(line, "TODO"):
            todo_lines.append(line_number)
        line_number += 1
    file.close()
    return todo_lines

# TODO: Something
def find_string(haystack, needle):
    if not haystack or not needle:
        return []

    n, m = len(haystack), len(needle)
    if m > n:
        return []

    # ASCII
    base = 256      
    # limiter  
    mod = 10**9 + 7 

    needle_hash = 0
    window_hash = 0
    h = 1  

    for i in range(m - 1):
        h = (h * base) % mod

    for i in range(m):
        needle_hash = (base * needle_hash + ord(needle[i])) % mod
        window_hash = (base * window_hash + ord(haystack[i])) % mod

    result = []
    for i in range(n - m + 1):
        if needle_hash == window_hash:
            # for collision
            if haystack[i:i + m] == needle:
                result.append(i)

        # update hash
        if i < n - m:
            window_hash = (base * (window_hash - ord(haystack[i]) * h) + ord(haystack[i + m])) % mod

            if window_hash < 0:
                window_hash += mod

    return result

# TODO: Something

def find_todo_lines(file_path):
    todo_lines = []
    file = open(file_path, 'r', encoding='utf-8')
    line_number = 1
    while True:
        line = file.readline()
        if not line:
            break
        if find_string(line, "TODO"):
            todo_lines.append(line_number)
        line_number += 1
    file.close()
    return todo_lines

# TODO: Something
def find_string(haystack, needle):
    if not haystack or not needle:
        return []

    n, m = len(haystack), len(needle)
    if m > n:
        return []

    # ASCII
    base = 256      
    # limiter  
    mod = 10**9 + 7 

    needle_hash = 0
    window_hash = 0
    h = 1  

    for i in range(m - 1):
        h = (h * base) % mod

    for i in range(m):
        needle_hash = (base * needle_hash + ord(needle[i])) % mod
        window_hash = (base * window_hash + ord(haystack[i])) % mod

    result = []
    for i in range(n - m + 1):
        if needle_hash == window_hash:
            # for collision
            if haystack[i:i + m] == needle:
                result.append(i)

        # update hash
        if i < n - m:
            window_hash = (base * (window_hash - ord(haystack[i]) * h) + ord(haystack[i + m])) % mod

            if window_hash < 0:
                window_hash += mod

    return result

# TODO: Something

def find_todo_lines(file_path):
    todo_lines = []
    file = open(file_path, 'r', encoding='utf-8')
    line_number = 1
    while True:
        line = file.readline()
        if not line:
            break
        if find_string(line, "TODO"):
            todo_lines.append(line_number)
        line_number += 1
    file.close()
    return todo_lines

# TODO: Something
def find_string(haystack, needle):
    if not haystack or not needle:
        return []

    n, m = len(haystack), len(needle)
    if m > n:
        return []

    # ASCII
    base = 256      
    # limiter  
    mod = 10**9 + 7 

    needle_hash = 0
    window_hash = 0
    h = 1  

    for i in range(m - 1):
        h = (h * base) % mod

    for i in range(m):
        needle_hash = (base * needle_hash + ord(needle[i])) % mod
        window_hash = (base * window_hash + ord(haystack[i])) % mod

    result = []
    for i in range(n - m + 1):
        if needle_hash == window_hash:
            # for collision
            if haystack[i:i + m] == needle:
                result.append(i)

        # update hash
        if i < n - m:
            window_hash = (base * (window_hash - ord(haystack[i]) * h) + ord(haystack[i + m])) % mod

            if window_hash < 0:
                window_hash += mod

    return result

# TODO: Something

def find_todo_lines(file_path):
    todo_lines = []
    file = open(file_path, 'r', encoding='utf-8')
    line_number = 1
    while True:
        line = file.readline()
        if not line:
            break
        if find_string(line, "TODO"):
            todo_lines.append(line_number)
        line_number += 1
    file.close()
    return todo_lines

# TODO: Something
def find_string(haystack, needle):
    if not haystack or not needle:
        return []

    n, m = len(haystack), len(needle)
    if m > n:
        return []

    # ASCII
    base = 256      
    # limiter  
    mod = 10**9 + 7 

    needle_hash = 0
    window_hash = 0
    h = 1  

    for i in range(m - 1):
        h = (h * base) % mod

    for i in range(m):
        needle_hash = (base * needle_hash + ord(needle[i])) % mod
        window_hash = (base * window_hash + ord(haystack[i])) % mod

    result = []
    for i in range(n - m + 1):
        if needle_hash == window_hash:
            # for collision
            if haystack[i:i + m] == needle:
                result.append(i)

        # update hash
        if i < n - m:
            window_hash = (base * (window_hash - ord(haystack[i]) * h) + ord(haystack[i + m])) % mod

            if window_hash < 0:
                window_hash += mod

    return result

# TODO: Something

def find_todo_lines(file_path):
    todo_lines = []
    file = open(file_path, 'r', encoding='utf-8')
    line_number = 1
    while True:
        line = file.readline()
        if not line:
            break
        if find_string(line, "TODO"):
            todo_lines.append(line_number)
        line_number += 1
    file.close()
    return todo_lines

# TODO: Something
def find_string(haystack, needle):
    if not haystack or not needle:
        return []

    n, m = len(haystack), len(needle)
    if m > n:
        return []

    # ASCII
    base = 256      
    # limiter  
    mod = 10**9 + 7 

    needle_hash = 0
    window_hash = 0
    h = 1  

    for i in range(m - 1):
        h = (h * base) % mod

    for i in range(m):
        needle_hash = (base * needle_hash + ord(needle[i])) % mod
        window_hash = (base * window_hash + ord(haystack[i])) % mod

    result = []
    for i in range(n - m + 1):
        if needle_hash == window_hash:
            # for collision
            if haystack[i:i + m] == needle:
                result.append(i)

        # update hash
        if i < n - m:
            window_hash = (base * (window_hash - ord(haystack[i]) * h) + ord(haystack[i + m])) % mod

            if window_hash < 0:
                window_hash += mod

    return result

# TODO: Something

def find_todo_lines(file_path):
    todo_lines = []
    file = open(file_path, 'r', encoding='utf-8')
    line_number = 1
    while True:
        line = file.readline()
        if not line:
            break
        if find_string(line, "TODO"):
            todo_lines.append(line_number)
        line_number += 1
    file.close()
    return todo_lines

# TODO: Something
def find_string(haystack, needle):
    if not haystack or not needle:
        return []

    n, m = len(haystack), len(needle)
    if m > n:
        return []

    # ASCII
    base = 256      
    # limiter  
    mod = 10**9 + 7 

    needle_hash = 0
    window_hash = 0
    h = 1  

    for i in range(m - 1):
        h = (h * base) % mod

    for i in range(m):
        needle_hash = (base * needle_hash + ord(needle[i])) % mod
        window_hash = (base * window_hash + ord(haystack[i])) % mod

    result = []
    for i in range(n - m + 1):
        if needle_hash == window_hash:
            # for collision
            if haystack[i:i + m] == needle:
                result.append(i)

        # update hash
        if i < n - m:
            window_hash = (base * (window_hash - ord(haystack[i]) * h) + ord(haystack[i + m])) % mod

            if window_hash < 0:
                window_hash += mod

    return result

# TODO: Something

def find_todo_lines(file_path):
    todo_lines = []
    file = open(file_path, 'r', encoding='utf-8')
    line_number = 1
    while True:
        line = file.readline()
        if not line:
            break
        if find_string(line, "TODO"):
            todo_lines.append(line_number)
        line_number += 1
    file.close()
    return todo_lines

# TODO: Something
def find_string(haystack, needle):
    if not haystack or not needle:
        return []

    n, m = len(haystack), len(needle)
    if m > n:
        return []

    # ASCII
    base = 256      
    # limiter  
    mod = 10**9 + 7 

    needle_hash = 0
    window_hash = 0
    h = 1  

    for i in range(m - 1):
        h = (h * base) % mod

    for i in range(m):
        needle_hash = (base * needle_hash + ord(needle[i])) % mod
        window_hash = (base * window_hash + ord(haystack[i])) % mod

    result = []
    for i in range(n - m + 1):
        if needle_hash == window_hash:
            # for collision
            if haystack[i:i + m] == needle:
                result.append(i)

        # update hash
        if i < n - m:
            window_hash = (base * (window_hash - ord(haystack[i]) * h) + ord(haystack[i + m])) % mod

            if window_hash < 0:
                window_hash += mod

    return result

# TODO: Something

def find_todo_lines(file_path):
    todo_lines = []
    file = open(file_path, 'r', encoding='utf-8')
    line_number = 1
    while True:
        line = file.readline()
        if not line:
            break
        if find_string(line, "TODO"):
            todo_lines.append(line_number)
        line_number += 1
    file.close()
    return todo_lines

# TODO: Something
def find_string(haystack, needle):
    if not haystack or not needle:
        return []

    n, m = len(haystack), len(needle)
    if m > n:
        return []

    # ASCII
    base = 256      
    # limiter  
    mod = 10**9 + 7 

    needle_hash = 0
    window_hash = 0
    h = 1  

    for i in range(m - 1):
        h = (h * base) % mod

    for i in range(m):
        needle_hash = (base * needle_hash + ord(needle[i])) % mod
        window_hash = (base * window_hash + ord(haystack[i])) % mod

    result = []
    for i in range(n - m + 1):
        if needle_hash == window_hash:
            # for collision
            if haystack[i:i + m] == needle:
                result.append(i)

        # update hash
        if i < n - m:
            window_hash = (base * (window_hash - ord(haystack[i]) * h) + ord(haystack[i + m])) % mod

            if window_hash < 0:
                window_hash += mod

    return result

# TODO: Something

def find_todo_lines(file_path):
    todo_lines = []
    file = open(file_path, 'r', encoding='utf-8')
    line_number = 1
    while True:
        line = file.readline()
        if not line:
            break
        if find_string(line, "TODO"):
            todo_lines.append(line_number)
        line_number += 1
    file.close()
    return todo_lines

# TODO: Something
def find_string(haystack, needle):
    if not haystack or not needle:
        return []

    n, m = len(haystack), len(needle)
    if m > n:
        return []

    # ASCII
    base = 256      
    # limiter  
    mod = 10**9 + 7 

    needle_hash = 0
    window_hash = 0
    h = 1  

    for i in range(m - 1):
        h = (h * base) % mod

    for i in range(m):
        needle_hash = (base * needle_hash + ord(needle[i])) % mod
        window_hash = (base * window_hash + ord(haystack[i])) % mod

    result = []
    for i in range(n - m + 1):
        if needle_hash == window_hash:
            # for collision
            if haystack[i:i + m] == needle:
                result.append(i)

        # update hash
        if i < n - m:
            window_hash = (base * (window_hash - ord(haystack[i]) * h) + ord(haystack[i + m])) % mod

            if window_hash < 0:
                window_hash += mod

    return result

# TODO: Something

def find_todo_lines(file_path):
    todo_lines = []
    file = open(file_path, 'r', encoding='utf-8')
    line_number = 1
    while True:
        line = file.readline()
        if not line:
            break
        if find_string(line, "TODO"):
            todo_lines.append(line_number)
        line_number += 1
    file.close()
    return todo_lines

# TODO: Something
def find_string(haystack, needle):
    if not haystack or not needle:
        return []

    n, m = len(haystack), len(needle)
    if m > n:
        return []

    # ASCII
    base = 256      
    # limiter  
    mod = 10**9 + 7 

    needle_hash = 0
    window_hash = 0
    h = 1  

    for i in range(m - 1):
        h = (h * base) % mod

    for i in range(m):
        needle_hash = (base * needle_hash + ord(needle[i])) % mod
        window_hash = (base * window_hash + ord(haystack[i])) % mod

    result = []
    for i in range(n - m + 1):
        if needle_hash == window_hash:
            # for collision
            if haystack[i:i + m] == needle:
                result.append(i)

        # update hash
        if i < n - m:
            window_hash = (base * (window_hash - ord(haystack[i]) * h) + ord(haystack[i + m])) % mod

            if window_hash < 0:
                window_hash += mod

    return result

# TODO: Something

def find_todo_lines(file_path):
    todo_lines = []
    file = open(file_path, 'r', encoding='utf-8')
    line_number = 1
    while True:
        line = file.readline()
        if not line:
            break
        if find_string(line, "TODO"):
            todo_lines.append(line_number)
        line_number += 1
    file.close()
    return todo_lines

# TODO: Something
def find_string(haystack, needle):
    if not haystack or not needle:
        return []

    n, m = len(haystack), len(needle)
    if m > n:
        return []

    # ASCII
    base = 256      
    # limiter  
    mod = 10**9 + 7 

    needle_hash = 0
    window_hash = 0
    h = 1  

    for i in range(m - 1):
        h = (h * base) % mod

    for i in range(m):
        needle_hash = (base * needle_hash + ord(needle[i])) % mod
        window_hash = (base * window_hash + ord(haystack[i])) % mod

    result = []
    for i in range(n - m + 1):
        if needle_hash == window_hash:
            # for collision
            if haystack[i:i + m] == needle:
                result.append(i)

        # update hash
        if i < n - m:
            window_hash = (base * (window_hash - ord(haystack[i]) * h) + ord(haystack[i + m])) % mod

            if window_hash < 0:
                window_hash += mod

    return result

# TODO: Something

def find_todo_lines(file_path):
    todo_lines = []
    file = open(file_path, 'r', encoding='utf-8')
    line_number = 1
    while True:
        line = file.readline()
        if not line:
            break
        if find_string(line, "TODO"):
            todo_lines.append(line_number)
        line_number += 1
    file.close()
    return todo_lines

# TODO: Something
def find_string(haystack, needle):
    if not haystack or not needle:
        return []

    n, m = len(haystack), len(needle)
    if m > n:
        return []

    # ASCII
    base = 256      
    # limiter  
    mod = 10**9 + 7 

    needle_hash = 0
    window_hash = 0
    h = 1  

    for i in range(m - 1):
        h = (h * base) % mod

    for i in range(m):
        needle_hash = (base * needle_hash + ord(needle[i])) % mod
        window_hash = (base * window_hash + ord(haystack[i])) % mod

    result = []
    for i in range(n - m + 1):
        if needle_hash == window_hash:
            # for collision
            if haystack[i:i + m] == needle:
                result.append(i)

        # update hash
        if i < n - m:
            window_hash = (base * (window_hash - ord(haystack[i]) * h) + ord(haystack[i + m])) % mod

            if window_hash < 0:
                window_hash += mod

    return result

# TODO: Something

def find_todo_lines(file_path):
    todo_lines = []
    file = open(file_path, 'r', encoding='utf-8')
    line_number = 1
    while True:
        line = file.readline()
        if not line:
            break
        if find_string(line, "TODO"):
            todo_lines.append(line_number)
        line_number += 1
    file.close()
    return todo_lines

# TODO: Something
def find_string(haystack, needle):
    if not haystack or not needle:
        return []

    n, m = len(haystack), len(needle)
    if m > n:
        return []

    # ASCII
    base = 256      
    # limiter  
    mod = 10**9 + 7 

    needle_hash = 0
    window_hash = 0
    h = 1  

    for i in range(m - 1):
        h = (h * base) % mod

    for i in range(m):
        needle_hash = (base * needle_hash + ord(needle[i])) % mod
        window_hash = (base * window_hash + ord(haystack[i])) % mod

    result = []
    for i in range(n - m + 1):
        if needle_hash == window_hash:
            # for collision
            if haystack[i:i + m] == needle:
                result.append(i)

        # update hash
        if i < n - m:
            window_hash = (base * (window_hash - ord(haystack[i]) * h) + ord(haystack[i + m])) % mod

            if window_hash < 0:
                window_hash += mod

    return result

# TODO: Something

def find_todo_lines(file_path):
    todo_lines = []
    file = open(file_path, 'r', encoding='utf-8')
    line_number = 1
    while True:
        line = file.readline()
        if not line:
            break
        if find_string(line, "TODO"):
            todo_lines.append(line_number)
        line_number += 1
    file.close()
    return todo_lines

# TODO: Something
def find_string(haystack, needle):
    if not haystack or not needle:
        return []

    n, m = len(haystack), len(needle)
    if m > n:
        return []

    # ASCII
    base = 256      
    # limiter  
    mod = 10**9 + 7 

    needle_hash = 0
    window_hash = 0
    h = 1  

    for i in range(m - 1):
        h = (h * base) % mod

    for i in range(m):
        needle_hash = (base * needle_hash + ord(needle[i])) % mod
        window_hash = (base * window_hash + ord(haystack[i])) % mod

    result = []
    for i in range(n - m + 1):
        if needle_hash == window_hash:
            # for collision
            if haystack[i:i + m] == needle:
                result.append(i)

        # update hash
        if i < n - m:
            window_hash = (base * (window_hash - ord(haystack[i]) * h) + ord(haystack[i + m])) % mod

            if window_hash < 0:
                window_hash += mod

    return result

# TODO: Something

def find_todo_lines(file_path):
    todo_lines = []
    file = open(file_path, 'r', encoding='utf-8')
    line_number = 1
    while True:
        line = file.readline()
        if not line:
            break
        if find_string(line, "TODO"):
            todo_lines.append(line_number)
        line_number += 1
    file.close()
    return todo_lines