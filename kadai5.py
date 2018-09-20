result={}
def contain2(target, *args):
        try:
            for i in range(len(args)):
                if type(args[i])!=str:
                    result.update([(args[i],'False')])
                    continue
                result.update([(args[i],str(target in args[i]))])
            return result
        except:
            return result
print(contain2('1',1,'222','12'))
