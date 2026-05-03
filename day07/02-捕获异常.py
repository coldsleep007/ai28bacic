try:
    #print(name)                      # NameError
    # src_f = open('1.txt', 'r')       # FileNotFoundError
    #print(10 // 0)
except Exception as e:
    # print('哎呀, 程序出问题了!')
    # e就是异常对象, 代表着: 异常信息.  可以直接把它输出到控制台.
    print(e)

print('看看我执行了吗?')