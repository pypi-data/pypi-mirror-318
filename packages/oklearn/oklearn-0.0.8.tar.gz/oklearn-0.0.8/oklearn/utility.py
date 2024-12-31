import time
from functools import wraps
import warnings, logging
from io import BytesIO
from PIL import Image

warnings.filterwarnings('ignore')
logger = logging.getLogger(__name__)

def measure_execution_time(func):
    @wraps(func)  # 원래 함수의 메타데이터(예: 함수 이름, 문서 문자열 등)를 유지함
    def wrapper(*args, **kwargs):
        # 시작 시간 기록
        start_time = time.time()
        print(f"start {func.__name__}")
        # 함수 실행
        result = func(*args, **kwargs)
        print(f"end {func.__name__}")
        # 종료 시간 기록
        end_time = time.time()
        
        # 실행 시간 계산
        execution_time = end_time - start_time
        print(f"{func.__name__} executed in {execution_time:.1f} seconds")
        
        return result
    return wrapper


# float 형태의 데이터를 분:초(mm:ss) 형태로 변환
def float_to_time(time):
    minutes = int(time)
    seconds = (time - minutes) * 60
    seconds = round(seconds)
    formatted_time = f"{minutes}:{seconds:02}"
    return formatted_time


# 데이터프레임을 이미지로 저장
def dataframe_to_image(df, filename):
    fig, ax = plt.subplots(figsize=(len(df.columns), len(df) + 1))  # figsize(tuples)로 조정 가능
    ax.axis('off')  # 축 없애기
    ax.table(cellText=df.values, rowLabels=df.index, rowLoc='center', colLabels=df.columns, 
             cellLoc='center', loc='center')
    
    # BytesIO 객체에 플롯 저장
    buf = BytesIO()
    plt.savefig(buf, format='png', bbox_inches='tight', dpi=300)
    buf.seek(0)
    
    # PIL 이미지를 열고 저장
    image = Image.open(buf)
    image.save('./images/'+filename)
