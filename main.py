Certainly! Here's an example of a Python script that checks if a given number is prime:

```python
def is_prime(n):
    if n <= 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

# Test the is_prime function
num = 17
if is_prime(num):
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")
```

And here's an example of a JavaScript code that checks if a given number is prime:

```javascript
function isPrime(n) {
    if (n <= 1) {
        return false;
    } else if (n === 2) {
        return true;
    } else if (n % 2 === 0) {
        return false;
    } else {
        for (let i = 3; i <= Math.sqrt(n); i += 2) {
            if (n % i === 0) {
                return false;
            }
        }
        return true;
    }
}

// Test the isPrime function
let num = 17;
if (isPrime(num)) {
    console.log(`${num} is a prime number`);
} else {
    console.log(`${num} is not a prime number`);
}
```

Both scripts define a function `is_prime` (Python) or `isPrime` (JavaScript) that checks if a number is prime or not. The scripts then test the function with the number `17` and print whether it is prime or not.
