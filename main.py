import openai
import os

# 设置OpenAI API
openai.api_key = 'you-key'
    
# 读取提示文件
filename = './zhanyiming.txt'
with open(filename, encoding='utf-8') as f:
    content = f.read()

# 按行分割内容
content_list = content.split("\n")

# 生成prompt序列
prompts = []
for i in range(len(content_list)):
    if i % 20 == 0 and i != 0:
        prompt = '\n'.join(content_list[i-20:i])
        prompts.append(prompt)

# 读取问题文件
filename = './question.txt'
with open(filename, encoding='utf-8') as f:
    questions = f.readlines()

# 生成答案文件
answers = []
for prompt, question in zip(prompts, questions):
    # 处理问题格式
    question = question.replace('\n', '')
    question = question.replace('?', '')
    
    response = openai.Completion.create(
      engine="text-davinci-003",
      prompt=prompt + "\n" + question + "\n",
      temperature=0.5,
      max_tokens=1024,
      n=1,
      stop=None,
      timeout=20,
    )

    # 解析OpenAI API响应结果，获取文本答案
    answer = response.choices[0].text
    answer = answer.strip()

    # 将答案保存到answers中
    answers.append(answer)

# 将答案写入文件
with open('pre.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(answers))
