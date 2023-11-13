# math-expression-calculator
A math expression calculator made with python and using the LIFO nature of stack data structure

## Known issues
An expression containing consecutive exponentiation operators (** ^) is evaluated from left to right while the convention of it is to evaluate it from right to left

### Example
$2^{3^3} = 134217728 \rightarrow$ what it should be

$2^{3^3} = 512 \rightarrow$ what it gives in this program

This is because it evaluates $2^3$ first before it evaluates $3^3$

Hence the output would give out $8^3$ instead of $2^{27}$