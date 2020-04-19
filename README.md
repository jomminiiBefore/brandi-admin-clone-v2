# Backend Part Introduction

Fasion startup admin page building. 

+ Project Period  : 4 weeks

+ Members         : (back) Jongmin Lee, Soheon Lee, Heechul Yoon (front) Yeji Choi, Seoungjun Kim
         
# Demo
Click below image to see our demo.


[![Brandi admin demo]()

# Features
+ [GET] Displaying existing seller list under the master authorization (Heechul Yoon).
+ [GET] Searching seller with keywords (Heechul Yoon).
+ [GET] Downloading seller list as excel file (Heechul Yoon).
+ [PUT] Changing seller status under the master authorization (Heechul Yoon).
+ [POST] Image resizing and uploading to S3 responsing back with URL (Heechul Yoon).
+ [POST] Registering promotional event under the master authorization (Heechul Yoon, Jongmin Lee).
+ [GET] Displaying existing event detail datas on editting page (Heechul Yoon, Jongmin Lee).
+ [PUT] Updating new information on existing event (Heechul Yoon, Jongmin Lee). 
+ [POST] Login authentication and ID/password validation (Yeji Choi).
+ [GET] Displaying detail information of a product (Soheon Lee).
+ [GET] Listing down product categories and subcategories according to the seller type (Soheon Lee).
+ [GET] Listing product color categories (Soheon Lee).
+ [POST] Registering new product by both master account and seller accounts (Soheon Lee).
+ [PUT] Updating product's detail information (Soheon Lee).
+ [GET] Listing existing product discount events and their related products with searching options (Soheon Lee).


# Technologies(Backend)
+ Python 3.8.0 : language
+ Flask 1.1.2  : web framework
+ Git          : cooperation and version management tool
+ Pymysql      : database connector
+ Pillow       : image file resizing
+ Pandas       : excel file generating
+ Boto3        : image uploading
+ Bcrypt       : password hashing
+ JWT          : token generating
+ AWS RDS      : database server
+ AWS S3       : image file repository
+ HTTP headers : Cross-Origin Resource Sharing (CORS)
+ MySQL 8.0.19 : Database

# API Documentation(Backend)
+ [seller, product, event](https://documenter.getpostman.com/view/10892890/Szf6WTQ3?version=latest)

# Database Modeling
![Brandi ERD](https://brandi-intern.s3.ap-northeast-2.amazonaws.com/242bbc15-dd4e-492c-8ec5-fb01d00c33f3)

# Participations
##### Heechul Yoon <a href="https://github.com/valentin1235">github</a>
##### Jongmin Lee <a href="https://github.com/jomminii">github</a>
##### Seungjune Kim <a href="https://github.com/DanSJKim">github</a> 
##### Soheon Lee <a href="https://github.com/soheon-lee">github</a>
##### Yeji Choi <a href="https://github.com/yeji0120">github</a>