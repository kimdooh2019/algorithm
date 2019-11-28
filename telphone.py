'''
문제 설명
전화번호부에 적힌 전화번호 중, 한 번호가 다른 번호의 접두어인 경우가 있는지 확인하려 합니다.
전화번호가 다음과 같을 경우, 구조대 전화번호는 영석이의 전화번호의 접두사입니다.

구조대 : 119
박준영 : 97 674 223
지영석 : 11 9552 4421
전화번호부에 적힌 전화번호를 담은 배열 phone_book 이 solution 함수의 매개변수로 주어질 때, 어떤 번호가 다른 번호의 접두어인 경우가 있으면 false를 그렇지 않으면 true를 return 하도록 solution 함수를 작성해주세요.

제한 사항
phone_book의 길이는 1 이상 1,000,000 이하입니다.
각 전화번호의 길이는 1 이상 20 이하입니다.
입출력 예제
phone_book	return
[119, 97674223, 1195524421]	false
[123,456,789]	true
[12,123,1235,567,88]	false
입출력 예 설명
입출력 예 #1
앞에서 설명한 예와 같습니다.

입출력 예 #2
한 번호가 다른 번호의 접두사인 경우가 없으므로, 답은 true입니다.

입출력 예 #3
첫 번째 전화번호, “12”가 두 번째 전화번호 “123”의 접두사입니다. 따라서 답은 false입니다.

알림

2019년 5월 13일, 테스트 케이스가 변경되었습니다. 이로 인해 이전에 통과하던 코드가 더 이상 통과하지 않을 수 있습니다.

출처'''


#접두어로 포함되면      False
#접두어가 되지 않는다면 True

phone1 = ['119', '97674223', '1195524421']
phone2 = ['123','456','789']함
phone3 = ['12','123','1235','567','88']
# 빼먹은 부분 접두어는 앞에서만 in 으로 체크하면 뒤에 포함된 것도 False로 반환
phone4 = ["124", "222222", "789", "5523", "4443124"]

phone = list()
phone.append(phone1)
phone.append(phone2)
phone.append(phone3)
#print(phone)

def solution(phone_book):
    for index, item in enumerate(phone_book):
        for num in range(len(phone_book)):
            if phone_book[num].startswith(item,0,len(item)):
                if num == phone_book.index(item):
                    continue    
                else:
                    answer = False
                    return answer
            else:
                answer = True
    return answer      



if '119' in '97674223':
  print('no')
else:
  print('yes')

print('ddddddddddd',phone1.index('119'))

# 내가 쓴 함수

# 문자열 함수 str.startswith( 'str', begin=0, end=len( 'str' ) )
# 리스트 함수 list.index( 'str' )


