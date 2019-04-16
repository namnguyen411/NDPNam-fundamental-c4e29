from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from collections import OrderedDict

#1. Open connection
url = "http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2018/0/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn"
conn = urlopen(url)
raw_data = conn.read()
html_content = raw_data.decode('utf8')

soup = BeautifulSoup(html_content, "html.parser")

div = soup.find("div",attrs={'style':'overflow:hidden;width:100%;border-bottom:solid 1px #cecece;'})
table = div.table
tr_list = table.find_all('tr')
list_index=[]
for tr in tr_list:
    td_list = tr.find('td', attrs={'<td style="width:32%;color:#014377;font-weight:bold;" class="b_r_c">

    })
    list_index.append(bctc)

pyexcel.save_as(records=list_index, dest_file_name="BCTC.xls")
