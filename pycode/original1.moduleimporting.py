from pack.newfunction import fact
num = input("Enter a number to find the factorial")
type(num)
intnum = int(num)
# newfunction.check_num(intnum)
print(fact(intnum))

# another import example  -- as an object
import newfunction as f

f.check_num(intnum)


