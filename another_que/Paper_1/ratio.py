value = "1:2"
a,b = (value.split(":"))
a,b = float(a),float(b)
total = a+b

percentage_a  = (float(a)/total)*100
percentage_b = (float(b)/total)*100

print(percentage_a,percentage_b)