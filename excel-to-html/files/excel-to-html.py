import pandas as pd
import math
import re

df = pd.read_excel("test.xlsx")

with open("table.html", "w", encoding="utf-8-sig") as fw:
  fw.write('<div class="table_wrap">\n')
  fw.write('  <table class="table">\n')

  fw.write('    <thead>\n')
  fw.write('      <tr>\n')
  for index in df.columns:
    fw.write('        <th>{0}</th>\n'.format(index))
  fw.write('      </tr>\n')
  fw.write('    </thead>\n')

  fw.write('    <tbody>\n')
  for i in range(len(df)):
    fw.write('      <tr class="clickable_row" data-href="">\n')
    fw.write('        <th class="">\n')
    fw.write('          <div class="">\n')
    fw.write('          </div>\n')
    fw.write('        </th>\n')

    for k in range(len(df.columns)):
      val = df.iloc[i, k]
      rowspan = 1
      if isinstance(val, str):
        val = re.sub("(\r\n)|(\n)", "<br>", val)
        l = 1
        while i+l < len(df):
          _val = df.iloc[i+l, k]
          if isinstance(_val, str):
            break
          l += 1
        rowspan = l
      fw.write('        <td>{1}</td>\n'.format(rowspan, val))
    fw.write('      </tr>\n')
  fw.write('    </body>\n')
  fw.write('  </table>\n')
  fw.write('</div><!-- table_wrap -->\n')
