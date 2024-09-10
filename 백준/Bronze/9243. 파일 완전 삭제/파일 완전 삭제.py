# 덮어 씌울 횟수
n = int(input())
# 비트 입력 - 문자열
before_bits = input()
after_bits = input()

# 비트를 변경할 리스트 생성
changebits = list(before_bits)  # before_bits를 리스트로 변환

def checkdelete(bits):
    if n % 2 != 0: # n이 홀수라면
        for i in range(len(bits)):
            if bits[i] == '1':
                bits[i] = '0'
            else:
                bits[i] = '1'
        return ''.join(bits) #리스트를 문자열로 반환
    else: #n이 짝수라면
        return ''.join(bits)

if checkdelete(changebits) == after_bits:
    print("Deletion succeeded")
else:
    print("Deletion failed")