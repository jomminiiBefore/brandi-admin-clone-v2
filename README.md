# Backend Part Introduction

Fasion startup admin page building. 

+ Project Period  : 4 weeks

+ Members         : (back) Jongmin Lee, Soheon Lee, Heechul Yoon (front) Yeji Choi, Seoungjun Kim
         
# Demo
Click below image to see our demo.


[![Brandi admin demo]()

# Features
+ [GET] displaying existing seller list under the master authorization(Heechul Yoon).
+ [GET] searching seller with keywords(Heechul Yoon).
+ [GET] downloading seller list as excel file(Heechul Yoon).
+ [PUT] changing seller status under the master authorization(Heechul Yoon).
+ [POST] image resizing and uploading to S3 responsing back with URL(Heechul Yoon).
+ [POST] registering promotional event under the master authorization(Heechul Yoon, Jongmin Lee).
+ [GET] displaying existing event detail datas on editting page(Heechul Yoon, Jongmin Lee).
+ [PUT] updating new informations on existing event(Heechul Yoon, Jongmin Lee). 


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

# API Documentation(Backend)
+ [seller, product, event]()

# Database Modeling
![Brandi ERD](https://brandi-intern.s3.ap-northeast-2.amazonaws.com/242bbc15-dd4e-492c-8ec5-fb01d00c33f3)
