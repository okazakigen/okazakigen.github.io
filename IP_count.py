from flask import Flask, request, jsonify

app = Flask(__name__)

# 使用一個字典來存儲IP地址和來訪次數
visitor_count = {}

@app.route('/')
def home():
    # 獲取客戶端IP地址
    ip = request.remote_addr
    
    # 如果IP地址不在字典中，則添加它並初始化計數為1
    if ip not in visitor_count:
        visitor_count[ip] = 1
    else:
        # 如果IP地址已經存在，則增加計數
        visitor_count[ip] += 1
    
    # 取得特定IP的訪問次數
    count = visitor_count[ip]
    
    # 返回JSON數據
    return jsonify({'count': count})

@app.route('/update_visitor_count')
def update_visitor_count():
    # 獲取所有IP地址的訪問次數總和
    total_count = sum(visitor_count.values())
    
    # 返回JSON數據
    return jsonify({'count': total_count})

if __name__ == '__main__':
    app.run()
