d1={"name":"gayu","age":20}
d2={"book":"python","coast":567}
d3={"item":"chocolate","brand":"dairymilk"}
d1.update(d2)
print(d1)
d4={**d1,**d2,**d3}
print(d4)
print(d3["brand"])
