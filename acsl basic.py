input("Enter the information")

vara = "PAIR"
varb = "THREE OF A KIND"
varc = "FULL HOUSE"
vard = "FOUR OF A KIND"

def Execute (org):
    for q in range(0,5):
        array_info = org
        a = 4
        b = 4
        original = [5] * a
        for i in range(a):
            original[i] = [5] * b

        array_info = array_info.split(",")
        for i in range(0,4):
            if len(array_info[i]) < 4:
                while len(array_info[i]) < 4:
                    array_info[i] = '0' + array_info[i]


        for i in range(0,4):
            x = array_info[i]
            for u in range(0,4):
                original[i][u] = x[u]



        a = input("Enter:")
        row = int(a[0]) - 1
        col =  int(a[2]) - 1
        count = 0
        m = original

        while count < 6:

            if m[row][col] == "0":
                m[row][col] = str(int(m[row][col]) + 1)
                if int(m[row][col]) > 3:
                    m[row][col] = "0"
                col = col + 1
                if col > 3:
                    col = 0
                count = count + 1

                continue
            vara = "PAIR"
     
            if m[row][col] == "1":
                m[row][col] = str(int(m[row][col]) + 1)
                if int(m[row][col]) > 3:
                    m[row][col] = "0"
                col = col - 1
                if col < 0:
                    col = 3

                count = count + 1
                continue
            varb = "THREE OF A KIND"

            
            if m[row][col] == "2":
                m[row][col] = str(int(m[row][col]) + 1)
                if int(m[row][col]) > 3:
                    m[row][col] = "0"
                row = row - 1
                if row < 0:
                    row = 3

                count = count + 1

                continue
            varc = "FULL HOUSE"
            if m[row][col] == "3":
                m[row][col] = str(int(m[row][col]) + 1)
                if int(m[row][col]) > 3:
                    m[row][col] = "0"
                row = row + 1
                if row > 3:
                    row = 0

                count = count + 1

                continue
            vard = "FOUR OF A KIND"

        

print('1. '+ vara)
print('2. '+ varb)
print('3. '+ varc)
print('4. '+ vard)







    
    
