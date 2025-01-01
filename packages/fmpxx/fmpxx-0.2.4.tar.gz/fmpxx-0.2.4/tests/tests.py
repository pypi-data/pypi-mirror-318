import sys
import os

# 获取项目根目录的绝对路径
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
# 将项目根目录添加到 Python 模块搜索路径
sys.path.append(project_root)

# 然后再导入你的模块
from fmpxx import FMPClient

from fmpxx.financials import Financials
import os
import dotenv

dotenv.load_dotenv()

API_Key = os.getenv("FMP")



client = Financials(API_Key)
print(client.get_earnings_his('NVDA', period=1))