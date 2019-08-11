from SStack import *
a = [[1], [2], [3]]
st = SStack()
st.push(a[0])
a[0][0] = 5
b = st.pop()
print(b)