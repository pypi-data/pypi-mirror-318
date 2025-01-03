from ecdsa import SigningKey, SECP256k1
from ecdsa.ellipticcurve import Point

# 키 생성 함수
def keygen(curve=SECP256k1):
    private_key = SigningKey.generate(curve=curve).privkey.secret_multiplier
    public_key = private_key * curve.generator
    return private_key, public_key

# 1. 텍스트를 CP949로 인코딩 후 문자별로 타원곡선 점으로 변환
def encoding(text, curve=SECP256k1):
    G = curve.generator  # 기본 생성점
    order = G.order()    # 곡선의 차수
    encoded_points = []
    
    # CP949로 인코딩하여 바이트 배열로 변환
    byte_data = text.encode('cp949')  
    
    for byte in byte_data:
        if byte >= order:
            raise ValueError(f"Byte value {byte} exceeds curve order limit.")
        encoded_point = byte * G  # 바이트 값을 점으로 매핑
        encoded_points.append(encoded_point)
    
    return encoded_points

# 2. EC-Elgamal 암호화 함수
def Enc(public_key, plaintext_points, curve=SECP256k1):
    G = curve.generator
    ciphertexts = []
    for point in plaintext_points:
        k = SigningKey.generate(curve=curve).privkey.secret_multiplier  # 무작위 비밀값
        C1 = k * G
        C2 = point + k * public_key
        ciphertexts.append((C1, C2))
    return ciphertexts

# 3. 암호화 상태에서 덧셈 연산 수행
def Add(ciphertexts1, ciphertexts2):
    added_ciphertexts = []
    for c1, c2 in zip(ciphertexts1, ciphertexts2):
        C1_add = c1[0] + c2[0]
        C2_add = c1[1] + c2[1]
        added_ciphertexts.append((C1_add, C2_add))
    return added_ciphertexts

# 4. 복호화 함수
def Dec(private_key, ciphertexts):
    plaintext_points = []
    for C1, C2 in ciphertexts:
        shared_secret = C1 * private_key
        plaintext_point = C2 + (-shared_secret)
        plaintext_points.append(plaintext_point)
    return plaintext_points

# 5. 점을 CP949 문자로 디코딩
def discrete_log(point, curve=SECP256k1):
    # 이산 로그를 계산하는 간단한 방법은 주어진 점을 G의 거듭제곱으로 표현하는 것입니다.
    G = curve.generator
    order = G.order()

    for k in range(order):
        if point == k * G:  # 이산 로그를 찾은 경우
            return k
    return None  # 로그를 찾지 못한 경우

def decoding(points, curve=SECP256k1):
    G = curve.generator
    order = G.order()
    byte_data = bytearray()

    for point in points:
        # 이산 로그를 사용해 비밀 키 계산
        secret_key = discrete_log(point, curve)
        
        if secret_key is None:
            raise ValueError("이산 로그를 계산할 수 없습니다.")
        
        # 비밀 키를 바탕으로 복호화된 바이트 값을 계산
        # 예시로, 비밀 키를 해시하여 바이트로 변환
        decoded_value = secret_key % 256  # 바이트 값으로 제한 (0-255)

        byte_data.append(decoded_value)
    
    # CP949로 디코딩하여 원래 텍스트 복원
    text = byte_data.decode('cp949', errors='replace')
    return text
