while(True):
    print('入力する型を選んでください')
    type0=str(input('<'))
    if type0=='int':
        obj=int(input('int<'))
        break
    elif type0=='float':
        obj=float(input('float<'))
        break
    elif type0=='str':
        obj=str(input('str<'))
        break
    else:
        print('その型は登録されていません。')
while(True):
    print('変換先の型を入力してください。')
    type1=str(input('<'))
    if type1=='int' or type1=='float' or type1=='str':
        break
    else:
        print('その型は登録されていません。')
def change_type(obj, type1):
    try:
        if type1=='int':
            return int(obj)
        elif type1=='float':
            return float(obj)
        elif type1=='str':
            return str(obj)
    except :
        print('変換できませんでした。')
        return obj
print(change_type(obj, type1))
