import urllib.request

def dlimg(url,file_path,file_name):
	full_path=file_path+file_name+".mp4"
	urllib.request.urlretrieve(url,full_path)
url=input("enter the URL to download:")
file_name=input("enter the name of the image:")
if __name__ == '__main__':
	dlimg(url,'',file_name)	
