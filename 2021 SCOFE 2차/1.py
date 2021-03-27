def main():
    input_list = input().split()

    n = int(input_list[0])
    all_time = "".join(input_list[1].split(":"))

    time_list = list()
    for _ in range(n):
        time = int(input().split(":"))
        time_list.append([time[:2], time[2:4]])

    all_time_hour = int(all_time[:2])
    all_time_min = int(all_time[2:4])
    all_time_second = int(all_time[4:])

if __name__ == "__main__":
	main()