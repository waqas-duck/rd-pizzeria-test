package fees

// Discount takes pct percent off total, rounding the discount up.
func Discount(total int, pct int) int {
	if pct <= 0 || total <= 0 {
		return total
	}
	return total - (total*pct+99)/100
}

// PlatformFee is the fee on an order of total cents.
func PlatformFee(total int) int {
	if total <= 0 {
		return 0
	}
	return total * 4 / 100
}
