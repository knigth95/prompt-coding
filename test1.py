import openai

# 设置OpenAI API的访问密钥
openai.api_key = "you-key"

# 读取文件
filename = './zhanyiming.txt'
with open(filename, encoding='utf-8') as f:
    content = f.read()

# 按行分割内容
content_list = content.split("\n")

# 生成Prompt序列
prompts = []
for i in range(len(content_list)):
    if i % 20 == 0 and i != 0:
        prompt = '\n'.join(content_list[i-20:i])
        prompts.append(prompt)

# 调用OpenAI API生成文本
responses = []
for prompt in prompts:
    response = openai.Completion.create(
        engine="text-davinci-005",
        prompt=prompt,
        max_tokens=2048,
        n=1,
        stop=None,
        temperature=0.5,
    )
    generated_text = response.choices[0].text
    responses.append(generated_text)

# 将生成的文本写入predict.txt文件
with open('predict.txt', 'w') as f:
    f.write(''.join(responses))