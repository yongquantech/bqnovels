-------------------------------------------
            description
-------------------------------------------
Download novels from bq website  



--------------------------------------------
            instllation
--------------------------------------------            
1. install prequisites 
pip install requests
pip install bs4

2. install bqnovels
git clone https://github.com/yongquantech/bqnovels.git
cd bqnovels
python setup install


---------------------------------------------
            usage
---------------------------------------------
import bqnovels
dl = bqnovels.NovelsDownloader("novel_name","novel_link_id")
dl.download_novel()       