# Lambda Calculus

## Useful things

y_comb = lambda f, x: f(f, x)

true = lambda a, b: a
false = lambda a, b: b

cons = lambda a, b: lambda m: m(a, b)
car = lambda pair: pair(true)
cdr = lambda pair: pair(false)

IF = lambda cond, a, b: cond(a, b) 
OR = lambda a, b: a(a, b)
AND = lambda a, b: a(b, a)
NOT = lambda x: x(false, true)
XOR = lambda a, b: a(NOT(b), b) 
EQ = lambda a, b: a(b, NOT(b))

## Zero and addition

zero = lambda f: lambda x: x

succ = lambda num: lambda f: lambda x: f(num(f)(x))

one = succ(zero)

add = lambda a, b: a(succ)(b)

## pred and subtraction

pred = lambda num: cdr(num(lambda pair: cons(succ(car(pair)), car(pair)))(cons(zero, zero)))

sub = lambda a, b: b(pred)(a)

## Multiplication

mul = lambda a, b: lambda f: lambda x: a(b(f))(x)

## Converting to regular integers and bools

church_to_int = lambda num: num(lambda n: n + 1)(0)

int_to_church = lambda n: zero if n == 0 else succ(int_to_church(n - 1))

lambda_to_bool = lambda b: b("true", "false")
