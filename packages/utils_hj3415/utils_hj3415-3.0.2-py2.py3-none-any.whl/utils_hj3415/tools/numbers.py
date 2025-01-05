import math
import re
from .. import mylogger

def format_large_number(number:int) -> str:
    """
    Formats a large integer into a Korean-style segmented number with units.

    This function takes an integer number and formats it by separating it into segments
    of Korean numbering units such as '조', '억', and '만'. For each unit, the appropriate
    quotient is calculated and appended to the result. Any remainder less than 10,000
    is included at the end. The formatted result is returned as a string.

    Parameters:
    number (int): The large integer to format.

    Returns:
    str: The formatted number as a string with Korean numbering units.
    """
    # 숫자를 분해할 단위와 이름
    units = [("조", 10 ** 12), ("억", 10 ** 8), ("만", 10 ** 4)]
    result = []

    # 숫자를 처리
    for unit_name, unit_value in units:
        if number >= unit_value:
            quotient, number = divmod(number, unit_value)
            if quotient > 0:
                result.append(f"{quotient}{unit_name}")

    # 남은 숫자가 있으면 포함
    if number > 0:
        result.append(str(number))

    return " ".join(result)


def format_with_commas(number):
    """
    숫자를 입력받아 천단위로 콤마를 붙인 문자열로 반환하는 함수.
    :param number: 숫자(int 또는 float)
    :return: 천단위 콤마가 포함된 문자열
    """
    try:
        # 정수형인지 실수형인지 확인하여 포맷팅
        if isinstance(number, int):
            return f"{number:,}"
        elif isinstance(number, float):
            return f"{number:,.2f}"  # 소수점 이하 2자리까지
        else:
            raise ValueError("숫자 타입이 아닙니다.")
    except ValueError as e:
        return f"오류: {e}"


def to_float(value) -> float:
    """
    문자열(예: '1432', '1,432', '23%', '(1,234.56)') 또는 숫자형(예: 1432)을
    float로 변환하여 반환.
    - 변환 불가 시 float('nan') 반환
    - 회계식 음수표기(ex: '(1,234.56)')는 음수로 처리
    """

    mylogger.debug(f"to_float : {value}")

    # 1) 이미 숫자형(int, float)이면 바로 float 변환
    if isinstance(value, (int, float)):
        return float(value)

    try:
        # 2) 문자열 전처리
        s = str(value).strip()

        # 2-1) 회계식 음수 표기 여부 확인: (....)
        negative = False
        if s.startswith('(') and s.endswith(')'):
            negative = True
            # 괄호 제거
            s = s[1:-1]

        # 2-2) 쉼표와 퍼센트 기호 제거
        s = s.replace(',', '').replace('%', '')

        # 3) float 변환
        result = float(s)

        # 4) 회계식 음수였으면 부호 반전
        if negative:
            result = -result

        return result

    except (ValueError, TypeError):
        # 변환 불가능하면 NaN 반환
        return float('nan')

def nan_to_zero(v) -> float:
    """
    입력값을 받아 NaN inf 또는 None인 경우 0.0을 반환.
    숫자가 아닌 값은 ValueError를 발생.
    """
    if v is None:
        return 0.0
    if not isinstance(v, (int, float)):
        raise ValueError(f"Invalid input: {v} is not a number.")
    return 0.0 if math.isnan(v) or math.isinf(v) else float(v)


def is_6digit(word: str) -> bool:
    """
    파일명이 숫자 6자리인지 검사하여 반환.
    """
    return bool(re.match(r'^\d{6}$', word))