import time

# 계산할 복소 평면 영역
x1, x2, y1, y2 = -1.8, 1.8, -1.8, 1.8
c_real, c_imag = -0.62772, -.42193

def calcuate_z_serial_purepython(maxiter: int, zs: list, cs: list) -> list:
    """줄리아 갱신 규칙을 사용해 output 리스트 계산

    Args:
        maxiter (int): 최대 반복 횟수
        zs (list): 복소수 z의 제곱에
        cs (list): c를 더함

    Returns:
        list: 결과
    """
    output = [0] * len(zs)  # zs 리스트와 같은 크기의 output 생성
    for i in range(len(zs)):
        n = 0
        z = zs[i]
        c = cs[i]
        
        while abs(z) < 2 and n < maxiter:  # 절댓값 2(상한선)를 넘지 않고, 최대 반복횟수까지
            z = z * z + c
            n += 1
        
        output[i] = n
    
    return output

def calc_pure_python(desired_width: int, max_iteration: int):
    """복소 좌표(zs)와 복소 인자(cs)를 리스트로 만들고,
       줄리아 집합 생성

    Args:
        desired_width (int): x_step과 y_step을 조절
        max_iteration (int): 최대 반복 횟수
    """
    x_step = (x2 - x1) / desired_width
    y_step = (y1 - y2) / desired_width
    x = []
    y = []
    
    ycoord = y2
    while ycoord > y1:
        y.append(ycoord)
        ycoord += y_step
    
    xcoord = x1
    while xcoord < x2:
        x.append(xcoord)
        xcoord += x_step
        
    # 좌표 리스트와 각 셀의 초기 조건 생성
    # 초기 조건은 상수, 쉽게 제거할 수 있음에 주목
    # 함수의 입력을 통해 실제 시나리오를 시뮬레이션할 수 있음
    zs = []
    cs = []
    for ycoord in y:
        for xcoord in x:
            zs.append(complex(xcoord, ycoord))
            cs.append(complex(c_real, c_imag))
    
    print(f"Length of x: {len(x)}")
    print(f"Total elements: {len(zs)}")
    
    start_time = time.time()
    output = calcuate_z_serial_purepython(max_iteration, zs, cs)
    end_time = time.time()
    secs = end_time - start_time
    print(f"{calcuate_z_serial_purepython.__name__} took {secs}seconds")
    
    # 다음 sum은 1000^2 gird에 반복 300번을 가정한 값으로,
    # 우리가 의도한 좌표로 변화하는지 확인
    assert sum(output) == 33219980  # 아무런 에러가 없음을 확인하려고 assert를 사용
    
if __name__ == "__main__":
    calc_pure_python(desired_width=1000, max_iteration=300)