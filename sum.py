def calculate_stats(number):
    total_sum=0
    for i in number:
        total_sum+=i


    average=total_sum/len(number)

    variance_sum=0
    for num in number:
        variance_sum+=(num-average)**2

    variance_sum=variance_sum/len(number)

    std_dev=variance_sum**0.5

    return total_sum,average,std_dev

def main():
    number=[]
    for i in range(5):
        num=int(input("Enter the number "))
        number.append(num)

    total_sum, average, std_dev=calculate_stats(number)

    print(total_sum)
    print(average)
    print(std_dev)

if __name__ == "__main__":
    main()