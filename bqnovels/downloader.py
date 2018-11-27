from bs4 import BeautifulSoup
import requests, sys, pdb, re, os

SERVER = "https://www.biqukan.com"
class NovelsDownloader():
    def __init__(self, novel_name, novel_id):
        self.novel_id = novel_id
        self.server = SERVER
        self.charpters = {}
        self.novel_name = novel_name
    
    def fill_chapters(self):
        req = requests.get(url=self.server+"/"+self.novel_id+"/")
        while not req.ok:
            req = requests.get(url=self.server+"/"+self.novel_id+"/")
        html = req.text
        div_bf = BeautifulSoup(html,features="html.parser")
        div = div_bf.find_all('div', class_ = 'listmain')
        a_bf = BeautifulSoup(str(div[0]),features="html.parser")
        a = a_bf.find_all('a')
        for each in a:
            #pdb.set_trace()
            charpter_id = re.match('/\w+/([0-9]{1,})\.html',each.get('href')).group(1)
            self.charpters[charpter_id] = each.string

    def get_contents(self,chapter_id):
        req = requests.get(url=self.server+"/"+self.novel_id+"/"+chapter_id+".html")       
        html = req.text
        bf = BeautifulSoup(html,features="html.parser")
        texts = bf.find_all('div', class_='showtxt')
        #pdb.set_trace()
        while len(texts) == 0:
            req = requests.get(url=self.server+"/"+self.novel_id+"/"+chapter_id+".html")       
            html = req.text
            bf = BeautifulSoup(html,features="html.parser")
            texts = bf.find_all('div', class_='showtxt')
        text = texts[0].text.replace('\xa0'*8, '\n\n')
        return text

    def write(self, fl, name, text):
        fl.write(name + '\n')
        fl.writelines(text)
        fl.write('\n\n')
        fl.flush()

    def download_novel(self):
        self.fill_chapters()
        charpter_ids = list(map(int,list(self.charpters.keys())))
        #pdb.set_trace()
        charpter_ids.sort()
        path = os.path.expanduser('~')+'\\Downloads\\'+self.novel_name+".txt"
        fl = open(path, 'a', encoding='utf-8')
        #return urls
        for charpter_int_id in charpter_ids:         
            #pdb.set_trace()
            self.write(fl=fl,name=self.charpters[str(charpter_int_id)],text=self.get_contents(str(charpter_int_id)))
        fl.close()


if __name__ == "__main__":
    dl = NovelsDownloader("一念永恒","1_1094")
    dl.download_novel()
