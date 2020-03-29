
use brandi_test

-- authorization_types Table Create SQL
CREATE TABLE seller_infos
(
    seller_info_no             INT              NOT NULL    AUTO_INCREMENT COMMENT 'id', 
    name_kr                    VARCHAR(45)      NOT NULL    COMMENT '셀러 한글명', 
    name_en                    VARCHAR(45)      NOT NULL    COMMENT '셀러 영문명', 
    brandi_user_id             INT              NULL        COMMENT '브랜디 앱 유저 아이디', 
    ceo_name                   VARCHAR(45)      NULL        COMMENT '대표자명', 
    company_name               VARCHAR(45)      NULL        COMMENT '사업자명', 
    business_number            VARCHAR(12)      NULL        COMMENT '사업자번호', 
    certificate_image_url      VARCHAR(200)     NULL        COMMENT '사업자등록증 이미지 url', 
    online_business_number     VARCHAR(45)      NULL        COMMENT '통신판매업번호(개수 확인)', 
    online_business_image_url  VARCHAR(200)     NULL        COMMENT '통신판매업신고필증 이미지 url', 
    background_image_url       VARCHAR(200)     NULL        COMMENT '셀러페이지 배경이미지 url', 
    short_description          VARCHAR(100)     NULL        COMMENT '셀러 한줄 소개', 
    site_url                   VARCHAR(1000)    NOT NULL    COMMENT '사이트 url', 
    kakao_id                   VARCHAR(45)      NULL        COMMENT '카카오톡 아이디', 
    insta_id                   VARCHAR(45)      NULL        COMMENT '인스타그램 아이디', 
    yello_id                   VARCHAR(45)      NULL        COMMENT '옐로우 아이디', 
    center_number              VARCHAR(14)      NOT NULL    COMMENT '고객센터 전화번호', 
    zip_code                   INT              NULL        COMMENT '우편번호', 
    address                    VARCHAR(100)     NULL        COMMENT '주소', 
    detail_address             VARCHAR(100)     NULL        COMMENT '상세주소', 
    weekday_start_time         TIME             NULL        COMMENT '고객센터 운영시간(주중)_시작', 
    weekday_end_time           TIME             NULL        COMMENT '고객센터 운영시간(주중)_종료', 
    weekend_start_time         TIME             NULL        COMMENT '고객센터 운영시간(주말)_시작', 
    weekend_end_time           TIME             NULL        COMMENT '고객센터 운영시간(주말)_종료', 
    bank_name                  VARCHAR(45)      NULL        COMMENT '정산은행명', 
    bank_holder_name           VARCHAR(45)      NULL        COMMENT '계좌주명', 
    account_number             VARCHAR(45)      NULL        COMMENT '계좌번호', 
    PRIMARY KEY (seller_info_no)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

ALTER TABLE seller_infos COMMENT '셀러 수정페이지 전체 / 셀러 정보 수정할때마다 새로운 row로 생성(변경이력 관리 용)';

-- authorization_types Table Create SQL
CREATE TABLE manager_infos
(
    manager_info_no  INT             NOT NULL    AUTO_INCREMENT COMMENT 'id', 
    contact_number   VARCHAR(14)     NOT NULL    COMMENT '담당자 번호', 
    seller_id        INT             NOT NULL    COMMENT '셀러 아이디', 
    is_deleted       TINYINT         NOT NULL    COMMENT '삭제여부', 
    PRIMARY KEY (manager_info_no)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

ALTER TABLE manager_infos COMMENT '셀러 담당자 정보';

ALTER TABLE manager_infos
    ADD CONSTRAINT FK_manager_infos_seller_id_seller_infos_seller_info_no FOREIGN KEY (seller_id)
        REFERENCES seller_infos (seller_info_no) ON DELETE RESTRICT ON UPDATE RESTRICT;
