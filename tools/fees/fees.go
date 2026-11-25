package fees

// Discount takes pct percent off total, rounding the discount down.
func Discount(total int, pct int) int {
	if pct <= 0 || total <= 0 {
		return total
	}
	return total - total*pct/100
}

// ServiceFee is the fee on an order of total cents.
func ServiceFee(total int) int {
	if total <= 0 {
		return 0
	}
	return total * 3 / 100
}
