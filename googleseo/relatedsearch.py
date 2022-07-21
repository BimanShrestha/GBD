# Related searches
df21 = df[df['attributes.class'].str.contains('gGQDvd iIWm4b') & (df['element'] == "DIV")]["text"]
print(df21)
df21.to_csv('Related searches title.csv', index=False)
df22 = df[df['attributes.class'].str.contains('Q71vJc') & (df['element'] == "A")]["attributes.href"]
print(df22)
df22.to_csv('Related searches link.csv', index=False)

def Relatedsearch()