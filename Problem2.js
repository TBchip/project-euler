let prev2 = 1
let prev1 = 1
let nextNum = 0

let sum = 0
while (nextNum < 4000000) {
	if (nextNum % 2 == 0)
		sum += nextNum

	prev2 = prev1
	prev1 = nextNum
	nextNum = prev1 + prev2
}

console.log(sum)