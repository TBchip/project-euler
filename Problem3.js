function* genPrimes() {
	let primes = [2]

	yield 2;

	i = 3;
	while (true) {
		let isPrime = true;
		primes.forEach(prime => {
			if (i % prime == 0)
				isPrime = false
		})

		if (isPrime) {
			primes.push(i);
			yield i
		}

		i++
	}
}

let primeGen = genPrimes()
let num = 600851475143
let highestPrimeFactor = 0

while (num != 1) {
	let nextPrime = primeGen.next().value

	if (num % nextPrime == 0) {
		num /= nextPrime
		highestPrimeFactor = nextPrime
	}
}

console.log(highestPrimeFactor)