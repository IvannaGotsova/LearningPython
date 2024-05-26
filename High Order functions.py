def adds(number_add):
    def sums(number_sum):
        return (number_sum + number_sum) * number_add

    return sums


result = adds(10)
print(result(2))