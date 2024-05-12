// 导出 Lambda 函数处理程序
export const handler = function(event, context, callback) {
    // 打印接收到的事件对象，使用 JSON.stringify 进行格式化输出
    console.log('Received event:', JSON.stringify(event, null, 2));
    // 创建一个响应对象，初始状态码为 200，Content-Type 为任意类型
    var res ={
        "statusCode": 200,
        "headers": {
            "Content-Type": "*/*"
        }
    };
    // 默认的问候词为 'World'
    var greeter = 'World';
    // 检查是否在事件对象中包含了 greeter 属性，并且其值不为空
    if (event.greeter && event.greeter!== "") {
        greeter = event.greeter;
    } 
    // 如果事件对象中包含了 body 属性，并且其值不为空
    else if (event.body && event.body !== "") {
        // 解析事件对象的 body 属性为 JSON 对象
        var body = JSON.parse(event.body);
        // 如果 body 对象中包含了 greeter 属性，并且其值不为空
        if (body.greeter && body.greeter !== "") {
            greeter = body.greeter;
        }
    } 
    // 如果事件对象中包含了 queryStringParameters 属性，并且其中包含了 greeter 属性并且其值不为空
    else if (event.queryStringParameters && event.queryStringParameters.greeter && event.queryStringParameters.greeter !== "") {
        greeter = event.queryStringParameters.greeter;
    } 
    // 如果事件对象中包含了 multiValueHeaders 属性，并且其中包含了 greeter 属性并且其值不为空
    else if (event.multiValueHeaders && event.multiValueHeaders.greeter && event.multiValueHeaders.greeter != "") {
        // 将 multiValueHeaders 中的 greeter 属性的值使用 " and " 连接起来
        greeter = event.multiValueHeaders.greeter.join(" and ");
    } 
    // 如果事件对象中包含了 headers 属性，并且其中包含了 greeter 属性并且其值不为空
    else if (event.headers && event.headers.greeter && event.headers.greeter != "") {
        greeter = event.headers.greeter;
    } 
    // 设置响应对象的 body 属性为问候词加上 'Hello, ' 的字符串
    res.body = "Hello, " + greeter + "!";
    // 调用回调函数，返回响应对象和错误为 null
    callback(null, res);
};