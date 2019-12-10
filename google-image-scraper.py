from google_images_download import google_images_download   #importing the library


response = google_images_download.googleimagesdownload()   #class instantiation

arguments = {"keywords":"صورت ایرانی", "limit":100,
             "print_urls":True, "output_directory":"c://users/sahand/face extractor/datafol", "chromedriver":"chromedriver.exe"}

response.download(arguments) 
