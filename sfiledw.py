# author : alfianokt
# date   : 20/06/2019
# name   : sfiledw
# desc   : download file di sfile.mobi lewat cli
# git    : https://github.com/alfianokt/sfiledw


from requests import *
from http.cookiejar import LWPCookieJar as cj

s = Session()
s.cookies = cj('sfile.log')

# fungsi ini untuk mengambil nilai tengah
def spliter(va, vb, vc):
    vd = vc.split(va)[1]
    vd = vd.split(vb)[0]
    return vd


def sfileGrab(url):
    # setting custom headers
    headers = {
        'Host':'sfile.mobi',
        'User-Agent':'MohGila',
        'Referer': url,
        'Connection':'keep-alive',
        'Upgrade-Insecure-Requests':'1',
        'dnt':'1',
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Language':'id-ID,en-US;q=0.8',
        'X-Requested-With':'com.android.chrome'
        }
    page = s.get(url, headers=headers)
    s.cookies.save()
    href = spliter('id="download" href="', '" onclick', page.text)+'&k=6'
    title = sfileGrabTitle(href)
    s.cookies.load()
    file = s.get(href, headers=headers,stream=True)
    with open(title, 'wb') as fd:
        print('\rdownloading the file')
        for chunk in file.iter_content(chunk_size=50000):
            fd.write(chunk)
    return 'file save as ' + title

def sfileGrabTitle(url):
    title = url.split('/')[7]
    title = title.split('&is=')[0]
    return title

print('sfile.mobi downloader by alfianokt, \ntinggal massukin link aja gan...\n\n')

url = input('masukkan link url (sfile.mobi): ')
if(url != ''):
    print('getting data')
    print(sfileGrab(url))