days=("Monday","Tuesday","Wednesday","Thursday","Friday","Suturday","Sunday")
off=int(input("How much day-off you want?"))
if off<0 or off>7:
    print("Wrong number! It can be from 0 to 7 only")
else:
    wee=days[-off:]#срез кортежа
    print(f"Your weekends: {','.join(wee)}")#join объеденяет элементы списка через запятую
    work=days[:-off]
    print(f"Your working days: {','.join(work)}")

