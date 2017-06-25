import requests, os, bs4
url = 'http://www.smbc-comics.com';
os.makedirs('SMBC',exist_ok=True)
while True:
        print('Downloading from ' + str(url));
        res = requests.get(url);
        res.raise_for_status();
        soup = bs4.BeautifulSoup(res.text);
        comicElement = soup.select('#cc-comicbody img');
        if comicElement == []:
                print('Couldnt find comic image.');
        else:
                comicUrl = comicElement[0].get('src');
                print('Downloading image :' + str(comicUrl));
                res = requests.get(comicUrl);
                res.raise_for_status();
                imageFile = open(os.path.join('SMBC', os.path.basename(url)),'wb');
                for chunk in res.iter_content(100000):
                        imageFile.write(chunk);
                imageFile.close();
        prevLink = soup.select('a[rel="prev"]');
        if prevLink == []:
                break;
        else:
                url = prevLink[0].get('href');
print('Done');

               
