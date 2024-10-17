#딕셔너리 키-값


print("딕셔너리 생성===============================")


a={} # 생성방법


#추가

a["r38"] = "빅데이타반"
a["r32"] = "c언어"
a["r30"] = "진소영"

print(a)



# 생성방법

d = {"basketball": 5, "soccer": 11, "baseball": 9}
d["volleyball"] = 6

print(d)


# 값출력

print(d["basketball"])
print(d.get("basketball"))


print(a["r30"])
print(a.get("r30"))



# 값 삭제


d = {"basketball": 5, "soccer": 11, "baseball": 9}
del(d["basketball"])
print(d)


d = {"basketball": 5, "soccer": 11, "baseball": 9}
d ={}
print(d)


d = {"basketball": 5, "soccer": 11, "baseball": 9}
d.clear()
print(d)


# 찾기

d = {"basketball": 5, "soccer": 11, "baseball": 9}

print(type(d))
print(len(d))
print("soccer" in d)
print("volleyball" not in d)





print("딕셔너리의 키들을 리스트로 반환===============================")


d = {"basketball": 5, "soccer": 11, "baseball": 9}

keys = d.keys()
print(keys)
print(type(keys))

for key in keys:

    print("{0}:{1}".format(key, d[key]))



values = d.values()
print(values)
print(type(values))


items = d.items()
print(items)
print(type(items))












