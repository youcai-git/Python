import sys  # first, we import the module

args = sys.argv  # we get the list of arguments
print(f"这个{args[0]}用来说明py脚本命令行参数的传入")
first_num = float(args[1])
second_num = float(args[2])

product = first_num * second_num

print(f"The produce of {args[1]} times {args[2]} equals {str(product)}")
