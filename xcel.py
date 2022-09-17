import pandas as pd

excel_header = ['Student Name','Course','year','Department','QR','resume']
data = ['a','bt','1','Electrical','QR','file.txt']

df = pd.DataFrame(data,columns=excel_header)
writer = pd.ExcelWriter('file1.xlsx',engine='xlsxwriter')

df.to_excel(writer,sheet_name="event")

writer.save()