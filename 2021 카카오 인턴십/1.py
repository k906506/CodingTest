def solution(s):
    answer = ''
    temp = ''
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    e_numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'zero']

    for i in range(len(s)):
        if s[i] in numbers:
            answer += s[i]
        else:
            temp += s[i]
        if temp in e_numbers:
            temp = temp.replace('one', '1')
            temp = temp.replace('two', '2')
            temp = temp.replace('three', '3')
            temp = temp.replace('four', '4')
            temp = temp.replace('five', '5')
            temp = temp.replace('six', '6')
            temp = temp.replace('seven', '7')
            temp = temp.replace('eight', '8')
            temp = temp.replace('nine', '9')
            temp = temp.replace('zero', '0')
            answer += temp
            temp = ''

    return int(answer)
