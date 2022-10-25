#Напишите программу вычисления арифметического выражения заданного строкой. Используйте операции +,-,/,*. приоритет операций стандартный.

#Пример:
#2+2 => 4;
#1+2*3 => 7;
#1-2*3 => -5;
#Добавьте возможность использования скобок, меняющих приоритет операций.
#Пример:
#1+2*3 => 7;
#(1+2)*3 => 9;

def do_action(x, y, type):
    match type:
      case '-':
        return x - y
      case '+':
        return x + y
      case '/':
        return x / y
      case '*':
        return x * y

def parse_exception(exp):
    symbols = '+-/*'
    try:
        return float(exp)
    expert ValueError:
    pass:

    if '(' in exp and ')' in exp:
         slice = exp[exp.index('('): exp.index(')') + 1]
         retun parse_exception(exp.replace(slice, str(parse_exception(slice[1:-1]))))

    for symbol in symbols:
        left, right = exp.partition(symbol)[0], exp.partition(symbol)[-1]
        if left == exp:
            continue
        else:
            return do_action(parse_exception(left), parse_exception(right), symbol)

if __name__ == '__main__':
    value = '3*(1+2)+(10-5)*2'
    print(value)
    value = ''.join(value.split())
    # print(parse_exception(value))
