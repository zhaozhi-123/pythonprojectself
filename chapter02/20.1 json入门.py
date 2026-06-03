import json

user={
    "name":"张三",
    "age":18,
    "sex":"男",
    "hobbies":["reading","swimming"]
}
with open("resources/user.json","w",encoding="utf-8") as f:
    # indent缩进，ensure_ascii=False 中文不显示乱码
    json.dump(user,f,ensure_ascii=False,indent=2)