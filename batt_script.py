def find_percentage():
    current = ""
    final = ""
    try: 
        with open("battery.txt",'r+') as file:
            percentage=(file.readline())
            percentage=percentage.strip()
            for i in percentage:
                try: 
                    int(i)
                    current += str(i)
                except ValueError:
                    pass
            for i in current:
                try:
                    int(i)
                    final += str(i)
                except SyntaxError:
                    pass
    except OSError as e:
        print(e)
    finally:
        file.close()
        return int(final)
final = find_percentage()
try:
    with open("battery.txt",'w+') as file:
        file.write(str(final))
except OSError as e:
    print(e)
finally:
    file.close()
