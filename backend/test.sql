use brandi_test
-- authorization_types Table Create SQL
CREATE TABLE authorization_types
(
    `auth_type_no`  INT            NOT NULL    AUTO_INCREMENT COMMENT 'id', 
    `name`          VARCHAR(10)    NOT NULL    COMMENT '타입명', 
    `is_deleted`    TINYINT        NOT NULL    DEFAULT FALSE COMMENT '삭제여부', 
    PRIMARY KEY (auth_type_no)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT '권한 타입(마스터 or 셀러)' ;

INSERT INTO authorization_types (auth_type_no, name, is_deleted) VALUES (1, '마스터', 0);
INSERT INTO authorization_types (auth_type_no, name, is_deleted) VALUES (2, '셀러', 0);


-- accounts Table Create SQL
CREATE TABLE accounts
(
    `account_no`    INT            NOT NULL    AUTO_INCREMENT COMMENT 'id', 
    `auth_type_id`  INT            NOT NULL    COMMENT '권한 타입 외래키', 
    `login_id`      VARCHAR(45)    NOT NULL    UNIQUE COMMENT '로그인 아이디', 
    `password`      VARCHAR(80)    NOT NULL    COMMENT '비밀번호', 
    `is_deleted`    TINYINT        NOT NULL    DEFAULT FALSE COMMENT '삭제여부', 
    PRIMARY KEY (account_no)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT '계정 정보';

ALTER TABLE accounts
    ADD CONSTRAINT FK_auth_type_id FOREIGN KEY (auth_type_id)
        REFERENCES authorization_types (auth_type_no);

INSERT INTO accounts (account_no, auth_type_id, login_id, password, is_deleted) VAlUES (1, 1, 'master', '$2b$12$iJN2OxkW69HHb6cVLeRjPuAQoGYKIZY.nlCbwJVRzrWGUrvmJRypi', 0);
INSERT INTO accounts (account_no, auth_type_id, login_id, password, is_deleted) VAlUES (2, 2, 'seller', '$2b$12$iJN2OxkW69HHb6cVLeRjPuAQoGYKIZY.nlCbwJVRzrWGUrvmJRypi', 0);
INSERT INTO accounts (account_no, auth_type_id, login_id, password, is_deleted) VAlUES (3, 2, 'seller_shopping', '$2b$12$iJN2OxkW69HHb6cVLeRjPuAQoGYKIZY.nlCbwJVRzrWGUrvmJRypi', 0);
INSERT INTO accounts (account_no, auth_type_id, login_id, password, is_deleted) VAlUES (4, 2, 'seller_market', '$2b$12$iJN2OxkW69HHb6cVLeRjPuAQoGYKIZY.nlCbwJVRzrWGUrvmJRypi', 0);
INSERT INTO accounts (account_no, auth_type_id, login_id, password, is_deleted) VAlUES (5, 2, 'seller_loadshop', '$2b$12$iJN2OxkW69HHb6cVLeRjPuAQoGYKIZY.nlCbwJVRzrWGUrvmJRypi', 0);
INSERT INTO accounts (account_no, auth_type_id, login_id, password, is_deleted) VAlUES (6, 2, 'seller_designer', '$2b$12$iJN2OxkW69HHb6cVLeRjPuAQoGYKIZY.nlCbwJVRzrWGUrvmJRypi', 0);
INSERT INTO accounts (account_no, auth_type_id, login_id, password, is_deleted) VAlUES (7, 2, 'seller_general', '$2b$12$iJN2OxkW69HHb6cVLeRjPuAQoGYKIZY.nlCbwJVRzrWGUrvmJRypi', 0);
INSERT INTO accounts (account_no, auth_type_id, login_id, password, is_deleted) VAlUES (8, 2, 'seller_national', '$2b$12$iJN2OxkW69HHb6cVLeRjPuAQoGYKIZY.nlCbwJVRzrWGUrvmJRypi', 0);
INSERT INTO accounts (account_no, auth_type_id, login_id, password, is_deleted) VAlUES (9, 2, 'seller_beauty', '$2b$12$iJN2OxkW69HHb6cVLeRjPuAQoGYKIZY.nlCbwJVRzrWGUrvmJRypi', 0);


-- product_sorts Table Create SQL
CREATE TABLE product_sorts
(
    `product_sort_no`  INT            NOT NULL    AUTO_INCREMENT COMMENT 'id', 
    `name`             VARCHAR(10)    NOT NULL    UNIQUE COMMENT '분류명', 
    `is_deleted`       TINYINT        NOT NULL    DEFAULT FALSE COMMENT '삭제여부', 
    PRIMARY KEY (product_sort_no)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT '상품 분류(트렌드, 브랜드, 뷰티)';

INSERT INTO product_sorts (product_sort_no, name, is_deleted) VALUES (1, '트렌드', 0);
INSERT INTO product_sorts (product_sort_no, name, is_deleted) VALUES (2, '브랜드', 0);
INSERT INTO product_sorts (product_sort_no, name, is_deleted) VALUES (3, '뷰티', 0);


-- seller_accounts Table Create SQL
CREATE TABLE seller_accounts
(
    `seller_account_no`  INT         NOT NULL    AUTO_INCREMENT COMMENT 'id', 
    `account_id`         INT         NOT NULL    COMMENT '계정 정보 외래키', 
    `created_at`         DATETIME    NOT NULL    DEFAULT CURRENT_TIMESTAMP COMMENT '최초 등록일시', 
    `is_deleted`         TINYINT     NOT NULL    DEFAULT FALSE COMMENT '삭제여부', 
    PRIMARY KEY (seller_account_no)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT '셀러 계정';

ALTER TABLE seller_accounts
    ADD CONSTRAINT FK_account_id FOREIGN KEY (account_id)
        REFERENCES accounts (account_no);

INSERT INTO seller_accounts (seller_account_no, account_id) VALUES(1, 1);
INSERT INTO seller_accounts (seller_account_no, account_id) VALUES(2, 2);
INSERT INTO seller_accounts (seller_account_no, account_id) VALUES(3, 3);
INSERT INTO seller_accounts (seller_account_no, account_id) VALUES(4, 4);
INSERT INTO seller_accounts (seller_account_no, account_id) VALUES(5, 5);
INSERT INTO seller_accounts (seller_account_no, account_id) VALUES(6, 6);
INSERT INTO seller_accounts (seller_account_no, account_id) VALUES(7, 7);
INSERT INTO seller_accounts (seller_account_no, account_id) VALUES(8, 8);
INSERT INTO seller_accounts (seller_account_no, account_id) VALUES(9, 9);


-- seller_types Table Create SQL
CREATE TABLE seller_types
(
    `seller_type_no`   INT            NOT NULL    AUTO_INCREMENT COMMENT 'id', 
    `product_sort_id`  INT            NOT NULL    COMMENT '상품 분류 외래키', 
    `name`             VARCHAR(45)    NOT NULL    UNIQUE COMMENT '셀러 속성명', 
    `is_deleted`       TINYINT        NOT NULL    DEFAULT FALSE COMMENT '삭제여부', 
    PRIMARY KEY (seller_type_no)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT '셀러 속성(쇼핑몰, 마켓, 로드샵, 디자이너브랜드 ...)';

ALTER TABLE seller_types
    ADD CONSTRAINT FK_product_sort_id FOREIGN KEY (product_sort_id)
        REFERENCES product_sorts (product_sort_no);

INSERT INTO seller_types (seller_type_no, product_sort_id, name) VALUES (1, 1, '쇼핑몰');
INSERT INTO seller_types (seller_type_no, product_sort_id, name) VALUES (2, 1, '마켓');
INSERT INTO seller_types (seller_type_no, product_sort_id, name) VALUES (3, 1, '로드샵');
INSERT INTO seller_types (seller_type_no, product_sort_id, name) VALUES (4, 2, '디자이너브랜드');
INSERT INTO seller_types (seller_type_no, product_sort_id, name) VALUES (5, 2, '제너럴브랜드');
INSERT INTO seller_types (seller_type_no, product_sort_id, name) VALUES (6, 2, '내셔널브랜드');
INSERT INTO seller_types (seller_type_no, product_sort_id, name) VALUES (7, 3, '뷰티');


-- seller_statuses Table Create SQL
CREATE TABLE seller_statuses
(
    `status_no`   INT            NOT NULL    AUTO_INCREMENT, 
    `name`        VARCHAR(45)    NOT NULL    UNIQUE COMMENT '셀러 상태명', 
    `is_deleted`  TINYINT        NOT NULL    DEFAULT FALSE COMMENT '삭제여부', 
    PRIMARY KEY (status_no)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT '셀러 상태(입점, 입점대기, 퇴점, 퇴점대기, 휴점)';

INSERT INTO seller_statuses (status_no, name) VALUES (1, '입점대기');
INSERT INTO seller_statuses (status_no, name) VALUES (2, '입점');
INSERT INTO seller_statuses (status_no, name) VALUES (3, '퇴점대기');
INSERT INTO seller_statuses (status_no, name) VALUES (4, '퇴점');
INSERT INTO seller_statuses (status_no, name) VALUES (5, '휴점');


-- brandi_app_users Table Create SQL
CREATE TABLE brandi_app_users
(
    `app_user_no`  INT            NOT NULL    AUTO_INCREMENT COMMENT 'id', 
    `app_id`       VARCHAR(45)    NOT NULL    UNIQUE COMMENT '브랜디 앱 아이디', 
    `is_deleted`   TINYINT        NOT NULL    DEFAULT FALSE COMMENT '삭제여부', 
    PRIMARY KEY (app_user_no)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT '브랜디 앱 유저';

INSERT INTO brandi_app_users (app_user_no, app_id) VALUES (1, 'brandi01');
INSERT INTO brandi_app_users (app_user_no, app_id) VALUES (2, 'brandi02');
INSERT INTO brandi_app_users (app_user_no, app_id) VALUES (3, 'brandi03');
INSERT INTO brandi_app_users (app_user_no, app_id) VALUES (4, 'brandi04');
INSERT INTO brandi_app_users (app_user_no, app_id) VALUES (5, 'brandi05');


-- seller_infos Table Create SQL
CREATE TABLE seller_infos
(
    `seller_info_no`             INT              NOT NULL    AUTO_INCREMENT COMMENT 'id', 
    `seller_account_id`          INT              NOT NULL    COMMENT '셀러 계정 외래키', 
    `profile_image_url`          VARCHAR(200)     NULL        COMMENT '프로필 이미지 url', 
    `seller_status_id`           INT              NOT NULL    COMMENT '셀러 상태 외래키', 
    `seller_type_id`             INT              NOT NULL    COMMENT '셀러 속성 외래키', 
    `name_kr`                    VARCHAR(45)      NOT NULL    UNIQUE COMMENT '셀러 한글명', 
    `name_en`                    VARCHAR(45)      NOT NULL    UNIQUE COMMENT '셀러 영문명', 
    `brandi_app_user_id`         INT              NULL        COMMENT '브랜디 앱 유저 외래키', 
    `ceo_name`                   VARCHAR(45)      NULL        COMMENT '대표자명', 
    `company_name`               VARCHAR(45)      NULL        COMMENT '사업자명', 
    `business_number`            VARCHAR(12)      NULL        UNIQUE COMMENT '사업자번호', 
    `certificate_image_url`      VARCHAR(200)     NULL        COMMENT '사업자등록증 이미지 url', 
    `online_business_number`     VARCHAR(45)      NULL        UNIQUE COMMENT '통신판매업번호', 
    `online_business_image_url`  VARCHAR(200)     NULL        COMMENT '통신판매업신고필증 이미지 url', 
    `background_image_url`       VARCHAR(200)     NULL        COMMENT '셀러페이지 배경이미지 url', 
    `short_description`          VARCHAR(100)     NULL        COMMENT '셀러 한줄 소개', 
    `long_description`           VARCHAR(200)     NULL        COMMENT '셀러 상세 소개', 
    `site_url`                   VARCHAR(200)     NOT NULL    COMMENT '사이트 url', 
    `kakao_id`                   VARCHAR(45)      NULL        COMMENT '카카오톡 아이디', 
    `insta_id`                   VARCHAR(45)      NULL        COMMENT '인스타그램 아이디', 
    `yellow_id`                  VARCHAR(45)      NULL        COMMENT '옐로우 아이디', 
    `center_number`              VARCHAR(14)      NOT NULL    COMMENT '고객센터 전화번호', 
    `zip_code`                   INT              NULL        COMMENT '우편번호', 
    `address`                    VARCHAR(100)     NULL        COMMENT '주소', 
    `detail_address`             VARCHAR(100)     NULL        COMMENT '상세주소', 
    `weekday_start_time`         TIME             NULL        COMMENT '고객센터 운영시간(주중)_시작', 
    `weekday_end_time`           TIME             NULL        COMMENT '고객센터 운영시간(주중)_종료', 
    `weekend_start_time`         TIME             NULL        COMMENT '고객센터 운영시간(주말)_시작', 
    `weekend_end_time`           TIME             NULL        COMMENT '고객센터 운영시간(주말)_종료', 
    `bank_name`                  VARCHAR(45)      NULL        COMMENT '정산은행명', 
    `bank_holder_name`           VARCHAR(45)      NULL        COMMENT '계좌주명', 
    `account_number`             VARCHAR(45)      NULL        COMMENT '계좌번호', 
    `changing_seller_id`         INT              NOT NULL    COMMENT '변경실행자 셀러계정 외래키', 
    `updated_at`                 DATETIME         NULL        ON UPDATE CURRENT_TIMESTAMP COMMENT '수정일시', 
    `start_time`                 DATETIME         NOT NULL    DEFAULT CURRENT_TIMESTAMP COMMENT '시작일시', 
    `close_time`                 DATETIME         NOT NULL    DEFAULT '2037-12-31 23:59:59' COMMENT '종료일시', 
    `is_deleted`                 TINYINT          NOT NULL    DEFAULT FALSE COMMENT '삭제여부', 
    PRIMARY KEY (seller_info_no)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT '셀러 수정페이지 전체 / 셀러 정보 수정할때마다 새로운 row로 생성(변경이력 관리 용)';

ALTER TABLE seller_infos
    ADD CONSTRAINT FK_seller_type_id FOREIGN KEY (seller_type_id)
        REFERENCES seller_types (seller_type_no);

ALTER TABLE seller_infos
    ADD CONSTRAINT FK_seller_status_id FOREIGN KEY (seller_status_id)
        REFERENCES seller_statuses (status_no);

ALTER TABLE seller_infos
    ADD CONSTRAINT FK_brandi_app_user_id FOREIGN KEY (brandi_app_user_id)
        REFERENCES brandi_app_users (app_user_no);

ALTER TABLE seller_infos
    ADD CONSTRAINT FK_seller_account_id FOREIGN KEY (seller_account_id)
        REFERENCES seller_accounts (seller_account_no);

ALTER TABLE seller_infos
    ADD CONSTRAINT FK_changing_seller_id FOREIGN KEY (changing_seller_id)
        REFERENCES seller_accounts (seller_account_no);

INSERT INTO seller_infos 
(
    seller_info_no, 
    seller_account_id, 
    profile_image_url, 
    seller_status_id, 
    seller_type_id, 
    name_kr, 
    name_en, 
    brandi_app_user_id, 
    ceo_name, 
    company_name, 
    business_number, 
    certificate_image_url, 
    online_business_number, 
    online_business_image_url, 
    background_image_url, 
    short_description, 
    long_description, 
    site_url, 
    kakao_id, 
    insta_id, 
    yellow_id, 
    center_number, 
    zip_code, 
    address, 
    detail_address, 
    weekday_start_time, 
    weekday_end_time, 
    weekend_start_time, 
    weekend_end_time, 
    bank_name, 
    bank_holder_name, 
    account_number, 
    changing_seller_id
) VALUES (
    1,
    1, -- seller_account_id
    'https://image.brandi.me/seller/miu_blanc_profile_1541096303.jpeg', -- profile_image_url
    2, -- seller_status_id, 입점
    1, -- seller_type_id
    '마스터 한글명',
    'masteren',
    1, -- brandi_app_user_id
    '마스터_대표자명',
    '마스터_회사명',
    '111-11-11111', -- business_number
    'https://image.brandi.me/seller/miu_blanc_profile_1541096303.jpeg', -- certificate_image_url
    '111-11-11111', -- online_business_number
    'https://image.brandi.me/seller/miu_blanc_profile_1541096303.jpeg', -- online_business_image_url
    'https://image.brandi.me/seller/miu_blanc_background_1541096431.jpeg', -- background_image_url
    'on my way to meet you', -- short_description
    '상세설명입니다', -- long_description
    'https://www.brandi.co.kr/shop/miublanc', -- site_url
    'kakao', -- kakao_id
    'insta', -- insta_id
    'yellow', -- yellow_id
    '02-1234-5678', -- center_number
    '01234', -- zip_code
    '서울시 강남구 역삼동', -- address
    '청송빌딩', -- detail_address
    '10:00', -- weekday_start_time
    '24:00', -- weekday_end_time
    '10:00', -- weekend_start_time
    '24:00', -- weekend_end_time
    '하나은행', -- bank_name
    '브랜디', -- bank_holder_name
    '12-12345-12345123', -- account_number
    1 -- changing_seller_id
),
(
    2,
    2, -- seller_account_id
    'https://image.brandi.me/seller/miu_blanc_profile_1541096303.jpeg', -- profile_image_url
    1, -- seller_status_id, 입점대기
    2, -- seller_type
    '셀러투 한글명',
    'seller_two_en',
    2, -- brandi_app_user_id
    '셀러투_대표자명',
    '셀러투_회사명',
    '111-11-11112', -- business_number
    'https://image.brandi.me/seller/miu_blanc_profile_1541096303.jpeg', -- certificate_image_url
    '111-11-11112', -- online_business_number
    'https://image.brandi.me/seller/miu_blanc_profile_1541096303.jpeg', -- online_business_image_url
    'https://image.brandi.me/seller/miu_blanc_background_1541096431.jpeg', -- background_image_url
    'on my way to meet you', -- short_description
    '상세설명입니다', -- long_description
    'https://www.brandi.co.kr/shop/miublanc', -- site_url
    'kakao', -- kakao_id
    'insta', -- insta_id
    'yellow', -- yellow_id
    '02-1234-5678', -- center_number
    '01234', -- zip_code
    '서울시 강남구 역삼동', -- address
    '청송빌딩', -- detail_address
    '10:00', -- weekday_start_time
    '24:00', -- weekday_end_time
    '10:00', -- weekend_start_time
    '24:00', -- weekend_end_time
    '하나은행', -- bank_name
    '브랜디', -- bank_holder_name
    '12-12345-12345123', -- account_number
    2 -- changing_seller_id
),
(
    3,
    3, --  seller_account_id
    'https://image.brandi.me/seller/miu_blanc_profile_1541096303.jpeg', --  profile_image_url
    3, -- seller_status_id, 퇴점대기
    3, -- seller_type
    '셀러쓰리 한글명',
    'seller_three_en',
    3, -- brandi_app_user_id
    '셀러쓰리_대표자명',
    '셀러쓰리_회사명',
    '111-11-11113', -- business_number
    'https://image.brandi.me/seller/miu_blanc_profile_1541096303.jpeg', -- certificate_image_url
    '111-11-11113', -- online_business_number
    'https://image.brandi.me/seller/miu_blanc_profile_1541096303.jpeg', -- online_business_image_url
    'https://image.brandi.me/seller/miu_blanc_background_1541096431.jpeg', -- background_image_url
    'on my way to meet you', -- short_description
    '상세설명입니다', -- long_description
    'https://www.brandi.co.kr/shop/miublanc', -- site_url
    'kakao', -- kakao_id
    'insta', -- insta_id
    'yellow', -- yellow_id
    '02-1234-5678', -- center_number
    '01234', -- zip_code
    '서울시 강남구 역삼동', -- address
    '청송빌딩', -- detail_address
    '10:00', -- weekday_start_time
    '24:00', -- weekday_end_time
    '10:00', -- weekend_start_time
    '24:00', -- weekend_end_time
    '하나은행', -- bank_name
    '브랜디', -- bank_holder_name
    '12-12345-12345123', -- account_number
    3 -- changing_seller_id
),
(
    4,
    4, --  seller_account_id
    'https://image.brandi.me/seller/miu_blanc_profile_1541096303.jpeg', --  profile_image_url
    4, -- seller_status_id, 퇴점
    4, -- seller_type
    '셀러포 한글명',
    'seller_four_en',
    4, -- brandi_app_user_id
    '셀러포_대표자명',
    '셀러포_회사명',
    '111-11-11114', -- business_number
    'https://image.brandi.me/seller/miu_blanc_profile_1541096303.jpeg', -- certificate_image_url
    '111-11-11114', -- online_business_number
    'https://image.brandi.me/seller/miu_blanc_profile_1541096303.jpeg', -- online_business_image_url
    'https://image.brandi.me/seller/miu_blanc_background_1541096431.jpeg', -- background_image_url
    'on my way to meet you', -- short_description
    '상세설명입니다', -- long_description
    'https://www.brandi.co.kr/shop/miublanc', -- site_url
    'kakao', -- kakao_id
    'insta', -- insta_id
    'yellow', -- yellow_id
    '02-1234-5678', -- center_number
    '01234', -- zip_code
    '서울시 강남구 역삼동', -- address
    '청송빌딩', -- detail_address
    '10:00', -- weekday_start_time
    '24:00', -- weekday_end_time
    '10:00', -- weekend_start_time
    '24:00', -- weekend_end_time
    '하나은행', -- bank_name
    '브랜디', -- bank_holder_name
    '12-12345-12345123', -- account_number
    4 -- changing_seller_id
),
(
    5,
    5, --  seller_account_id
    'https://image.brandi.me/seller/miu_blanc_profile_1541096303.jpeg', --  profile_image_url
    5, -- seller_status_id, 휴점
    5, -- seller_type
    '셀러파이브 한글명',
    'seller_five_en',
    5, -- brandi_app_user_id
    '셀러파이브_대표자명',
    '셀러파이브_회사명',
    '111-11-11115', -- business_number
    'https://image.brandi.me/seller/miu_blanc_profile_1541096303.jpeg', -- certificate_image_url
    '111-11-11115', -- online_business_number
    'https://image.brandi.me/seller/miu_blanc_profile_1541096303.jpeg', -- online_business_image_url
    'https://image.brandi.me/seller/miu_blanc_background_1541096431.jpeg', -- background_image_url
    'on my way to meet you', -- short_description
    '상세설명입니다', -- long_description
    'https://www.brandi.co.kr/shop/miublanc', -- site_url
    'kakao', -- kakao_id
    'insta', -- insta_id
    'yellow', -- yellow_id
    '02-1234-5678', -- center_number
    '01234', -- zip_code
    '서울시 강남구 역삼동', -- address
    '청송빌딩', -- detail_address
    '10:00', -- weekday_start_time
    '24:00', -- weekday_end_time
    '10:00', -- weekend_start_time
    '24:00', -- weekend_end_time
    '하나은행', -- bank_name
    '브랜디', -- bank_holder_name
    '12-12345-12345123', -- account_number
    5 -- changing_seller_id
);


-- first_categories Table Create SQL
CREATE TABLE first_categories
(
    `first_category_no`  INT            NOT NULL    AUTO_INCREMENT COMMENT 'id', 
    `name`               VARCHAR(45)    NOT NULL    UNIQUE COMMENT '카테고리명', 
    `is_deleted`         TINYINT        NULL        DEFAULT FALSE COMMENT '삭제여부', 
    PRIMARY KEY (first_category_no)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT '1차 카테고리';

INSERT INTO first_categories (first_category_no, name) VALUES (1, '트랜드');
INSERT INTO first_categories (first_category_no, name) VALUES (2, '브랜드');
INSERT INTO first_categories (first_category_no, name) VALUES (3, '뷰티');



-- second_categories Table Create SQL
CREATE TABLE second_categories
(
    `second_category_no`  INT            NOT NULL    AUTO_INCREMENT COMMENT 'id', 
    `name`                VARCHAR(45)    NOT NULL    COMMENT '카테고리명', 
    `first_category_id`   INT            NOT NULL    COMMENT '1차 카테고리 아이디', 
    `is_deleted`          TINYINT        NOT NULL    DEFAULT FALSE COMMENT '삭제여부', 
    PRIMARY KEY (second_category_no)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT '2차 카테고리';

ALTER TABLE second_categories
    ADD CONSTRAINT FK_first_category_no FOREIGN KEY (first_category_id)
        REFERENCES first_categories (first_category_no);

INSERT INTO second_categories (second_category_no, name, first_category_id ) VALUES (1, '아우터', 1);
INSERT INTO second_categories (second_category_no, name, first_category_id ) VALUES (2, '상의', 1);
INSERT INTO second_categories (second_category_no, name, first_category_id ) VALUES (3, '스커트', 1);
INSERT INTO second_categories (second_category_no, name, first_category_id ) VALUES (4, '바지', 1);
INSERT INTO second_categories (second_category_no, name, first_category_id ) VALUES (5, '원피스', 1);
INSERT INTO second_categories (second_category_no, name, first_category_id ) VALUES (6, '신발', 1);
INSERT INTO second_categories (second_category_no, name, first_category_id ) VALUES (7, '가방', 1);
INSERT INTO second_categories (second_category_no, name, first_category_id ) VALUES (8, '잡화', 1);
INSERT INTO second_categories (second_category_no, name, first_category_id ) VALUES (9, '주얼리', 1);
INSERT INTO second_categories (second_category_no, name, first_category_id ) VALUES (10, '라이프웨어', 1);
INSERT INTO second_categories (second_category_no, name, first_category_id ) VALUES (11, '빅사이즈', 1);
INSERT INTO second_categories (second_category_no, name, first_category_id ) VALUES (12, '아우터', 2);
INSERT INTO second_categories (second_category_no, name, first_category_id ) VALUES (13, '상의', 2);
INSERT INTO second_categories (second_category_no, name, first_category_id ) VALUES (14, '원피스', 2);
INSERT INTO second_categories (second_category_no, name, first_category_id ) VALUES (15, '팬츠', 2);
INSERT INTO second_categories (second_category_no, name, first_category_id ) VALUES (16, '스커트', 2);
INSERT INTO second_categories (second_category_no, name, first_category_id ) VALUES (17, '슈즈', 2);
INSERT INTO second_categories (second_category_no, name, first_category_id ) VALUES (18, '가방', 2);
INSERT INTO second_categories (second_category_no, name, first_category_id ) VALUES (19, '악세서리', 2);
INSERT INTO second_categories (second_category_no, name, first_category_id ) VALUES (20, '스웜웨어', 2);
INSERT INTO second_categories (second_category_no, name, first_category_id ) VALUES (21, '언더웨어', 2);
INSERT INTO second_categories (second_category_no, name, first_category_id ) VALUES (22, '스킨케어', 3);
INSERT INTO second_categories (second_category_no, name, first_category_id ) VALUES (23, '메이크업', 3);
INSERT INTO second_categories (second_category_no, name, first_category_id ) VALUES (24, '바디/헤어', 3);
INSERT INTO second_categories (second_category_no, name, first_category_id ) VALUES (25, '네일', 3);
INSERT INTO second_categories (second_category_no, name, first_category_id ) VALUES (26, '이너뷰티', 3);
INSERT INTO second_categories (second_category_no, name, first_category_id ) VALUES (27, '애슬레저', 3);
INSERT INTO second_categories (second_category_no, name, first_category_id ) VALUES (28, '홈트레이닝', 3);
INSERT INTO second_categories (second_category_no, name, first_category_id ) VALUES (29, '푸드', 3);
INSERT INTO second_categories (second_category_no, name, first_category_id ) VALUES (30, '기타', 3);




-- color_filters Table Create SQL
CREATE TABLE color_filters
(
    `color_filter_no`  INT             NOT NULL    AUTO_INCREMENT COMMENT 'id', 
    `name_kr`          VARCHAR(10)     NOT NULL    UNIQUE COMMENT '필터 한글명', 
    `name_en`          VARCHAR(20)     NOT NULL    UNIQUE COMMENT '필터 영문명', 
    `image_url`        VARCHAR(200)    NOT NULL    UNIQUE COMMENT '이미지 url', 
    `is_deleted`       TINYINT         NOT NULL    DEFAULT FALSE COMMENT '삭제여부', 
    PRIMARY KEY (color_filter_no)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT '색상 필터';

INSERT INTO color_filters (color_filter_no, name_kr, name_en, image_url) VALUES (1, '빨강', 'Red', 'http://sadmin.brandi.co.kr/include/img/product/color/red.png');
INSERT INTO color_filters (color_filter_no, name_kr, name_en, image_url) VALUES (2, '주황', 'Orange', 'http://sadmin.brandi.co.kr/include/img/product/color/orange.png');
INSERT INTO color_filters (color_filter_no, name_kr, name_en, image_url) VALUES (3, '노랑', 'Yellow', 'http://sadmin.brandi.co.kr/include/img/product/color/yellow.png');
INSERT INTO color_filters (color_filter_no, name_kr, name_en, image_url) VALUES (4, '베이지', 'Beige', 'http://sadmin.brandi.co.kr/include/img/product/color/beige.png');
INSERT INTO color_filters (color_filter_no, name_kr, name_en, image_url) VALUES (5, '갈색', 'Brown', 'http://sadmin.brandi.co.kr/include/img/product/color/brown.png');
INSERT INTO color_filters (color_filter_no, name_kr, name_en, image_url) VALUES (6, '초록', 'Green', 'http://sadmin.brandi.co.kr/include/img/product/color/green.png');
INSERT INTO color_filters (color_filter_no, name_kr, name_en, image_url) VALUES (7, '민트', 'Mint', 'http://sadmin.brandi.co.kr/include/img/product/color/mint.png');
INSERT INTO color_filters (color_filter_no, name_kr, name_en, image_url) VALUES (8, '하늘', 'Skyblue', 'http://sadmin.brandi.co.kr/include/img/product/color/skyblue.png');
INSERT INTO color_filters (color_filter_no, name_kr, name_en, image_url) VALUES (9, '파랑', 'Blue', 'http://sadmin.brandi.co.kr/include/img/product/color/blue.png');
INSERT INTO color_filters (color_filter_no, name_kr, name_en, image_url) VALUES (10, '남색', 'Navy', 'http://sadmin.brandi.co.kr/include/img/product/color/navy.png');
INSERT INTO color_filters (color_filter_no, name_kr, name_en, image_url) VALUES (11, '보라', 'Violet', 'http://sadmin.brandi.co.kr/include/img/product/color/violet.png');
INSERT INTO color_filters (color_filter_no, name_kr, name_en, image_url) VALUES (12, '분홍', 'Pink', 'http://sadmin.brandi.co.kr/include/img/product/color/pink.png');
INSERT INTO color_filters (color_filter_no, name_kr, name_en, image_url) VALUES (13, '흰색', 'White', 'http://sadmin.brandi.co.kr/include/img/product/color/white.png');
INSERT INTO color_filters (color_filter_no, name_kr, name_en, image_url) VALUES (14, '회색', 'Gray', 'http://sadmin.brandi.co.kr/include/img/product/color/gray.png');
INSERT INTO color_filters (color_filter_no, name_kr, name_en, image_url) VALUES (15, '검정', 'Black', 'http://sadmin.brandi.co.kr/include/img/product/color/black.png');
INSERT INTO color_filters (color_filter_no, name_kr, name_en, image_url) VALUES (16, '골드', 'Gold', 'http://sadmin.brandi.co.kr/include/img/product/color/gold.png');
INSERT INTO color_filters (color_filter_no, name_kr, name_en, image_url) VALUES (17, '로즈골드', 'Rosegold', 'http://sadmin.brandi.co.kr/include/img/product/color/rosegold.png');
INSERT INTO color_filters (color_filter_no, name_kr, name_en, image_url) VALUES (18, '실버', 'Sliver', 'http://sadmin.brandi.co.kr/include/img/product/color/silver.png');
INSERT INTO color_filters (color_filter_no, name_kr, name_en, image_url) VALUES (19, '선택안함', '선택안함', '선택안함');


-- style_filters Table Create SQL
CREATE TABLE style_filters
(
    `style_filter_no`  INT            NOT NULL    AUTO_INCREMENT COMMENT 'id', 
    `name`             VARCHAR(45)    NOT NULL    UNIQUE COMMENT '필터명', 
    `is_deleted`       TINYINT        NOT NULL    DEFAULT FALSE COMMENT '삭제여부', 
    PRIMARY KEY (style_filter_no)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT '스타일필터';

INSERT INTO style_filters (style_filter_no, name) VALUES (1, '선택안함');
INSERT INTO style_filters (style_filter_no, name) VALUES (2, '심플베이직');
INSERT INTO style_filters (style_filter_no, name) VALUES (3, '러블리');
INSERT INTO style_filters (style_filter_no, name) VALUES (4, '페미닌');
INSERT INTO style_filters (style_filter_no, name) VALUES (5, '캐주얼');
INSERT INTO style_filters (style_filter_no, name) VALUES (6, '섹시글램');


-- products Table Create SQL
CREATE TABLE products
(
    `product_no`  INT         NOT NULL    AUTO_INCREMENT COMMENT 'id', 
    `created_at`  DATETIME    NOT NULL    DEFAULT CURRENT_TIMESTAMP COMMENT '최초 등록일시', 
    `is_deleted`  TINYINT     NOT NULL    DEFAULT FALSE COMMENT '삭제여부', 
    PRIMARY KEY (product_no)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT '상품 번호';

INSERT INTO products (product_no) VALUES (1);
INSERT INTO products (product_no) VALUES (2);
INSERT INTO products (product_no) VALUES (3);


-- product_infos Table Create SQL
CREATE TABLE product_infos
(
    `product_info_no`      INT              NOT NULL    AUTO_INCREMENT COMMENT 'id', 
    `seller_id`            INT              NOT NULL    COMMENT '셀러 아이디',
    `is_available`         TINYINT          NOT NULL    COMMENT '판매여부', 
    `is_on_display`        TINYINT          NOT NULL    COMMENT '진열여부', 
    `product_sort_id`      INT              NOT NULL    COMMENT '상품 분류 아이디', 
    `first_category_id`    INT              NOT NULL    COMMENT '1차 카테고리 아이디', 
    `second_category_id`   INT              NULL        COMMENT '2차 카테고리 아이디', 
    `name`                 VARCHAR(45)      NOT NULL    COMMENT '상품명', 
    `short_description`    VARCHAR(100)     NULL        COMMENT '한줄 상품 설명', 
    `color_filter_id`      INT              NOT NULL    COMMENT '색상 필터 아이디', 
    `style_filter_id`      INT              NOT NULL    COMMENT '스타일 필터 아이디', 
    `long_description`     BLOB             NOT NULL    COMMENT '상세 상품 정보(html)', 
    `youtube_url`          VARCHAR(100)     NULL        COMMENT '유튜브 url', 
    `stock`                INT              NOT NULL    COMMENT '재고수량', 
    `price`                INT              NOT NULL    COMMENT '판매가', 
    `discount_rate`        DECIMAL(2, 2)    NOT NULL    COMMENT '할인율', 
    `discount_start_time`  DATETIME         NULL        COMMENT '할인기간_시작', 
    `discount_end_time`    DATETIME         NULL        COMMENT '할인기간_종료', 
    `min_unit`             INT              NULL        COMMENT '최소판매수량', 
    `max_unit`             INT              NULL        COMMENT '최대판매수량', 
    `updated_at`           DATETIME         NULL        ON UPDATE CURRENT_TIMESTAMP COMMENT '수정일시', 
    `start_time`           DATETIME         NOT NULL    DEFAULT CURRENT_TIMESTAMP COMMENT '시작일시', 
    `close_time`           DATETIME         NOT NULL    DEFAULT '2037-12-31 23:59:59' COMMENT '종료일시', 
    `uploader`             INT              NOT NULL    COMMENT '등록자', 
    `modifier`             INT              NOT NULL    COMMENT '수정자', 
    `is_deleted`           TINYINT          NOT NULL    DEFAULT FALSE COMMENT '삭제여부', 
    `product_id`           INT              NOT NULL    COMMENT '상품 아이디', 
    PRIMARY KEY (product_info_no)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT '상품 정보';

ALTER TABLE product_infos
    ADD CONSTRAINT FK_first_category_id FOREIGN KEY (first_category_id)
        REFERENCES first_categories (first_category_no);

ALTER TABLE product_infos
    ADD CONSTRAINT FK_second_category_id FOREIGN KEY (second_category_id)
        REFERENCES second_categories (second_category_no);

ALTER TABLE product_infos
    ADD CONSTRAINT FK_color_filters_id FOREIGN KEY (color_filter_id)
        REFERENCES color_filters (color_filter_no);

ALTER TABLE product_infos
    ADD CONSTRAINT FK_style_filter_id FOREIGN KEY (style_filter_id)
        REFERENCES style_filters (style_filter_no);

ALTER TABLE product_infos
    ADD CONSTRAINT FK_product_sort_no FOREIGN KEY (product_sort_id)
        REFERENCES product_sorts (product_sort_no);

ALTER TABLE product_infos
    ADD CONSTRAINT FK_product_id FOREIGN KEY (product_id)
        REFERENCES products (product_no);

ALTER TABLE product_infos
    ADD CONSTRAINT FK_seller_id FOREIGN KEY (seller_id)
        REFERENCES seller_accounts (seller_account_no);

ALTER TABLE product_infos
    ADD CONSTRAINT FK_uploader FOREIGN KEY (uploader)
        REFERENCES accounts (account_no);

ALTER TABLE product_infos
    ADD CONSTRAINT FK_modifier FOREIGN KEY (modifier)
        REFERENCES accounts (account_no);


INSERT INTO product_infos 
(
    product_info_no,
    seller_id,
    is_available,
    is_on_display,
    product_sort_id,
    first_category_id,
    second_category_id,
    name,
    short_description,
    color_filter_id,
    style_filter_id,
    long_description,
    youtube_url,
    stock,
    price,
    discount_rate,
    discount_start_time,
    discount_end_time,
    min_unit,
    max_unit,
    uploader,
    modifier,
    product_id
) VALUES 
(
    1, -- product_info_no
    2, -- seller_id
    1, -- is_available
    1, -- is_on_display
    1, -- product_sort_id
    1, -- first_category_id
    1, -- second_category_id
    '상품1', -- name
    '브랜디 상품 입니다.', -- short_description
    1, -- color_filter_id
    1, -- style_filter_id
    '<p>브랜디 상품 입니다. 브랜디 상품 입니다.</p>', -- long_description
    'https://www.youtube.com/watch?v=twGpF2v_w-s', -- youtube_url
    -1, -- stock, 관리안함이면 -1
    12000, -- price
    0.3, -- discount_rate
    '2020-05-12 23:59:59', -- discount_start_time
    '2020-06-12 23:59:59', -- discount_end_time
    1, -- min_unit
    10, -- max_unit
    2, -- uploader, account_no
    1, -- modifier, account_no
    1 -- product_id
),
(
    2, -- product_info_no
    2, -- seller_id
    1, -- is_available
    2, -- is_on_display
    2, -- product_sort_id
    3, -- first_category_id
    1, -- second_category_id
    '상품2', -- name
    '브랜디 상품 입니다.', -- short_description
    1, -- color_filter_id
    1, -- style_filter_id
    '<h1>브랜디 상품 입니다. 브랜디 상품 입니다.</h1>', -- long_description
    'https://www.youtube.com/watch?v=twGpF2v_w-s', -- youtube_url
    10, -- stock, 관리안함이면 -1
    15000, -- price
    0.5, -- discount_rate
    '2020-05-12 23:59:59', -- discount_start_time
    '2020-06-12 23:59:59', -- discount_end_time
    1, -- min_unit
    10, -- max_unit
    2, -- uploader, account_no
    1, -- modifier, account_no
    2 -- product_id
),
(
    3, -- product_info_no
    2, -- seller_id
    1, -- is_available
    1, -- is_on_display
    1, -- product_sort_id
    1, -- first_category_id
    1, -- second_category_id
    '상품3', -- name
    '브랜디 상품 입니다.', -- short_description
    1, -- color_filter_id
    1, -- style_filter_id
    '<h1>브랜디 상품 입니다. 브랜디 상품 입니다.</h1>', -- long_description
    'https://www.youtube.com/watch?v=twGpF2v_w-s', -- youtube_url
    -1, -- stock, 관리안함이면 -1
    12000, -- price
    0.4, -- discount_rate
    '2020-05-12 23:59:59', -- discount_start_time
    '2020-06-12 23:59:59', -- discount_end_time
    1, -- min_unit
    10, -- max_unit
    2, -- uploader, account_no
    1, -- modifier, account_no
    3 -- product_id
);



-- event_types Table Create SQL
CREATE TABLE event_types
(
    `event_type_no`  INT            NOT NULL    AUTO_INCREMENT COMMENT 'id', 
    `name`           VARCHAR(45)    NOT NULL    UNIQUE COMMENT '타입명', 
    `is_deleted`     TINYINT        NOT NULL    DEFAULT FALSE COMMENT '삭제여부', 
    PRIMARY KEY (event_type_no)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT '기획전 타입(이벤트, 쿠폰, 상품(이미지,텍스트), 유튜브)';

INSERT INTO event_types (event_type_no, name) VALUES (1, '이벤트');
INSERT INTO event_types (event_type_no, name) VALUES (2, '쿠폰');
INSERT INTO event_types (event_type_no, name) VALUES (3, '상품(이미지)');
INSERT INTO event_types (event_type_no, name) VALUES (4, '상품(텍스트)');
INSERT INTO event_types (event_type_no, name) VALUES (5, '유튜브');


-- event_sorts Table Create SQL
CREATE TABLE event_sorts
(
    `event_sort_no`  INT            NOT NULL    AUTO_INCREMENT COMMENT 'id', 
    `name`           VARCHAR(45)    NOT NULL    COMMENT '종류명', 
    `event_type_id`  INT            NOT NULL    COMMENT '기획전 타입 아이디', 
    `is_deleted`     TINYINT        NOT NULL    DEFAULT FALSE COMMENT '삭제여부', 
    PRIMARY KEY (event_sort_no)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT '기획전 종류';


ALTER TABLE event_sorts
    ADD CONSTRAINT FK_event_type_id FOREIGN KEY (event_type_id)
        REFERENCES event_types (event_type_no);

INSERT INTO event_sorts (event_sort_no, name, event_type_id) VALUES (1, '댓글창 있음', 1);
INSERT INTO event_sorts (event_sort_no, name, event_type_id) VALUES (2, '댓글창 없음', 1);
INSERT INTO event_sorts (event_sort_no, name, event_type_id) VALUES (3, '브랜디배송상품(정률)', 2);
INSERT INTO event_sorts (event_sort_no, name, event_type_id) VALUES (4, '브랜디배송상품(정액)', 2);
INSERT INTO event_sorts (event_sort_no, name, event_type_id) VALUES (5, '셀러쿠폰(정률)-브레스', 2);
INSERT INTO event_sorts (event_sort_no, name, event_type_id) VALUES (6, '셀러쿠폰(정액)-브레스', 2);
INSERT INTO event_sorts (event_sort_no, name, event_type_id) VALUES (7, '전체상품(정률)', 2);
INSERT INTO event_sorts (event_sort_no, name, event_type_id) VALUES (8, '전체상품(정액)', 2);
INSERT INTO event_sorts (event_sort_no, name, event_type_id) VALUES (9, '상품', 3);
INSERT INTO event_sorts (event_sort_no, name, event_type_id) VALUES (10, '버튼', 3);
INSERT INTO event_sorts (event_sort_no, name, event_type_id) VALUES (11, '상품', 4);
INSERT INTO event_sorts (event_sort_no, name, event_type_id) VALUES (12, '버튼', 4);
INSERT INTO event_sorts (event_sort_no, name, event_type_id) VALUES (13, '상품', 5);
INSERT INTO event_sorts (event_sort_no, name, event_type_id) VALUES (14, '버튼', 5);


-- events Table Create SQL
CREATE TABLE events
(
    `event_no`    INT         NOT NULL    AUTO_INCREMENT COMMENT 'id', 
    `created_at`  DATETIME    NOT NULL    DEFAULT CURRENT_TIMESTAMP COMMENT '최초 등록일시', 
    `is_deleted`  TINYINT     NOT NULL    DEFAULT FALSE COMMENT '삭제여부', 
    PRIMARY KEY (event_no)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT '기획전';

INSERT INTO events (event_no) VALUES (1);
INSERT INTO events (event_no) VALUES (2);
INSERT INTO events (event_no) VALUES (3);
INSERT INTO events (event_no) VALUES (4);

-- -- event_infos Table Create SQL
-- CREATE TABLE event_infos
-- (
--     `event_info_no`      INT             NOT NULL    AUTO_INCREMENT COMMENT 'id', 
--     `name`               VARCHAR(45)     NOT NULL    COMMENT '기획전명', 
--     `is_on_main`         TINYINT         NOT NULL    COMMENT '메인노출여부', 
--     `is_on_event`        TINYINT         NOT NULL    COMMENT '기획전 진열여부', 
--     `short_description`  VARCHAR(45)     NULL        COMMENT '기획전 간략설명', 
--     `event_start_time`   DATETIME        NOT NULL    COMMENT '기획전 기간_시작', 
--     `event_end_time`     DATETIME        NOT NULL    COMMENT '기획전 기간_종료', 
--     `banner_image_url`   VARCHAR(200)    NULL        COMMENT '기획전 배너 이미지_url', 
--     `detail_image_url`   VARCHAR(200)    NULL        COMMENT '기획전 상세 이미지_url', 
--     `long_description`   BLOB            NULL        COMMENT '기획전 상세설명', 
--     `youtube_url`        VARCHAR(100)    NULL        COMMENT '유튜브 url', 
--     `event_type_id`      INT             NOT NULL    COMMENT '기획전 타입 아이디', 
--     `event_sort_id`      INT             NOT NULL    COMMENT '기획전 종류 아이디', 
--     `updated_at`         DATETIME        NULL        COMMENT '수정일시', 
--     `start_time`         DATETIME        NOT NULL    COMMENT '시작일시', 
--     `close_time`         DATETIME        NOT NULL    COMMENT '종료일시', 
--     `uploader`           INT             NOT NULL    COMMENT '등록자', 
--     `modifier`           INT             NOT NULL    COMMENT '수정자', 
--     `is_deleted`         TINYINT         NOT NULL    COMMENT '삭제여부', 
--     `event_id`           INT             NOT NULL    COMMENT '이벤트 아이디', 
--     PRIMARY KEY (event_info_no)
-- );

-- ALTER TABLE event_infos COMMENT '기획전 정보(한번 저장하면 타입 수정 불가)';

-- ALTER TABLE event_infos
--     ADD CONSTRAINT FK_event_infos_event_type_id_event_types_event_type_no FOREIGN KEY (event_type_id)
--         REFERENCES event_types (event_type_no);

-- ALTER TABLE event_infos
--     ADD CONSTRAINT FK_event_infos_event_sort_id_event_sorts_event_sort_no FOREIGN KEY (event_sort_id)
--         REFERENCES event_sorts (event_sort_no);

-- ALTER TABLE event_infos
--     ADD CONSTRAINT FK_event_infos_event_id_envents_event_no FOREIGN KEY (event_id)
--         REFERENCES envents (event_no);

-- ALTER TABLE event_infos
--     ADD CONSTRAINT FK_event_infos_uploader_seller_infos_seller_info_no FOREIGN KEY (uploader)
--         REFERENCES seller_infos (seller_info_no);

-- ALTER TABLE event_infos
--     ADD CONSTRAINT FK_event_infos_modifier_seller_infos_seller_info_no FOREIGN KEY (modifier)
--         REFERENCES seller_infos (seller_info_no);


-- image_sizes Table Create SQL
CREATE TABLE image_sizes
(
    `image_size_no`  INT           NOT NULL    AUTO_INCREMENT COMMENT 'id', 
    `name`           VARCHAR(10)    NOT NULL    UNIQUE COMMENT '사이즈 명', 
    `is_deleted`     TINYINT       NOT NULL    DEFAULT FALSE COMMENT '삭제여부', 
    `height`         INT           NULL        COMMENT '높이', 
    `width`          INT           NULL        COMMENT '세로', 
    PRIMARY KEY (image_size_no)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT '이미지 사이즈';
INSERT INTO image_sizes (image_size_no, name, height, width) VALUES (1, 'Big', 300, 300);
INSERT INTO image_sizes (image_size_no, name, height, width) VALUES (2, 'Medium', 200, 200);
INSERT INTO image_sizes (image_size_no, name, height, width) VALUES (3, 'Small', 100, 100);


-- -- event_button_link_types Table Create SQL
-- CREATE TABLE event_button_link_types
-- (
--     `event_button_link_type_no`  INT            NOT NULL    AUTO_INCREMENT COMMENT 'id', 
--     `name`                       VARCHAR(45)    NOT NULL    COMMENT '링크타입명', 
--     `is_deleted`                 TINYINT        NOT NULL    COMMENT '삭제여부', 
--     PRIMARY KEY (event_button_link_type_no)
-- );

-- ALTER TABLE event_button_link_types COMMENT '이벤트 버튼 링크 타입';


-- -- manager_infos Table Create SQL
-- CREATE TABLE manager_infos
-- (
--     `manager_info_no`  INT             NOT NULL    AUTO_INCREMENT COMMENT 'id', 
--     `name`             VARCHAR(45)     NULL        COMMENT '담당자명', 
--     `contact_number`   VARCHAR(14)     NOT NULL    COMMENT '담당자 번호', 
--     `email`            VARCHAR(500)    NULL        COMMENT '담당자 이메일', 
--     `seller_id`        INT             NOT NULL    COMMENT '셀러 아이디', 
--     `is_deleted`       TINYINT         NOT NULL    COMMENT '삭제여부', 
--     PRIMARY KEY (manager_info_no)
-- );

-- ALTER TABLE manager_infos COMMENT '셀러 담당자 정보';

-- ALTER TABLE manager_infos
--     ADD CONSTRAINT FK_manager_infos_seller_id_seller_infos_seller_info_no FOREIGN KEY (seller_id)
--         REFERENCES seller_infos (seller_info_no);


-- product_images Table Create SQL
CREATE TABLE product_images
(
    `product_image_no`  INT             NOT NULL    AUTO_INCREMENT COMMENT 'id', 
    `image_url`         VARCHAR(200)    NOT NULL    COMMENT '이미지 url', 
    `product_id`        INT             NOT NULL    COMMENT '상품 아이디', 
    `image_size_id`     INT             NOT NULL    COMMENT '이미지 사이즈 아이디', 
    `image_order`       INT             NOT NULL    COMMENT '이미지 순서', 
    `is_deleted`        TINYINT         NOT NULL    DEFAULT FALSE COMMENT '삭제여부', 
    PRIMARY KEY (product_image_no)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT '상품 이미지';

ALTER TABLE product_images
    ADD CONSTRAINT FK_product_images_product_id FOREIGN KEY (product_id)
        REFERENCES product_infos (product_info_no);

ALTER TABLE product_images
    ADD CONSTRAINT FK_image_size_id FOREIGN KEY (image_size_id)
        REFERENCES image_sizes (image_size_no);

INSERT INTO product_images (product_image_no, image_url, product_id, image_size_id, image_order) VALUES (1, 'https://image.brandi.me/cproduct/2020/03/20/14748562_1584631415_image1_M.jpg', 1, 3, 1);
INSERT INTO product_images (product_image_no, image_url, product_id, image_size_id, image_order) VALUES (2, 'https://image.brandi.me/cproduct/2020/02/10/13664328_1581264198_image1_M.jpg', 2, 3, 1);
INSERT INTO product_images (product_image_no, image_url, product_id, image_size_id, image_order) VALUES (3, 'https://image.brandi.me/cproductdetail/2020/02/10/051ab4b12c1dc3c3cdbed61944ae2799.jpeg', 2, 2, 2);
INSERT INTO product_images (product_image_no, image_url, product_id, image_size_id, image_order) VALUES (4, 'https://image.brandi.me/cproductdetail/2020/03/16/63a59a5211cb6f5b6e69313411684950.JPG', 3, 1, 1);

-- -- product_tags Table Create SQL
-- CREATE TABLE product_tags
-- (
--     `product_tag_no`  INT            NOT NULL    AUTO_INCREMENT COMMENT 'id', 
--     `name`            VARCHAR(20)    NOT NULL    COMMENT '태그명', 
--     `product_id`      INT            NOT NULL    COMMENT '상품 아이디', 
--     `is_deleted`      TINYINT        NOT NULL    COMMENT '삭제여부', 
--     PRIMARY KEY (product_tag_no)
-- );

-- ALTER TABLE product_tags COMMENT '상품 태그 관리';

-- ALTER TABLE product_tags
--     ADD CONSTRAINT FK_product_tags_product_id_product_infos_product_info_no FOREIGN KEY (product_id)
--         REFERENCES product_infos (product_info_no);


-- -- product_change_histories Table Create SQL
-- CREATE TABLE product_change_histories
-- (
--     `product_change_history_no`  INT              NOT NULL    AUTO_INCREMENT COMMENT 'id', 
--     `product_id`                 INT              NOT NULL    COMMENT '변경된 상품 아이디', 
--     `changing_seller_id`         INT              NOT NULL    COMMENT '수정자', 
--     `changed_time`               DATETIME         NOT NULL    COMMENT '수정 날짜', 
--     `is_sold_out`                TINYINT          NOT NULL    COMMENT '판매여부', 
--     `is_on_display`              TINYINT          NOT NULL    COMMENT '진열여부', 
--     `price`                      INT              NOT NULL    COMMENT '판매가격', 
--     `discount_rate`              DECIMAL(2, 2)    NOT NULL    COMMENT '할인율', 
--     `is_deleted`                 TINYINT          NOT NULL    COMMENT '삭제여부', 
--     PRIMARY KEY (product_change_history_no)
-- );

-- ALTER TABLE product_change_histories COMMENT '상품의 경우 전체 수량이 많아 이력 테이블 따로 관리';

-- ALTER TABLE product_change_histories
--     ADD CONSTRAINT FK_product_change_histories_product_id_product_infos_product_info_no FOREIGN KEY (product_id)
--         REFERENCES product_infos (product_info_no);

-- ALTER TABLE product_change_histories
--     ADD CONSTRAINT FK_product_change_histories_changing_seller_id_seller_accounts_seller_account_no FOREIGN KEY (changing_seller_id)
--         REFERENCES seller_accounts (seller_account_no);


-- -- event_detail_infos Table Create SQL
-- CREATE TABLE event_detail_infos
-- (
--     `event_detail_info_no`     INT            NOT NULL    AUTO_INCREMENT COMMENT 'id', 
--     `button_name`              VARCHAR(45)    NULL        COMMENT '이벤트 버튼이름', 
--     `button_link_type_id`      INT            NULL        COMMENT '이벤트 버튼 링크타입 아이디', 
--     `button_link_description`  VARCHAR(45)    NULL        COMMENT '이벤트 버튼 링크내용', 
--     `event_info_id`            INT            NOT NULL    COMMENT '기획전 정보 아이디', 
--     `is_deleted`               TINYINT        NOT NULL    COMMENT '삭제여부', 
--     PRIMARY KEY (event_detail_info_no)
-- );

-- ALTER TABLE event_detail_infos COMMENT '이벤트 상세정보';

-- ALTER TABLE event_detail_infos
--     ADD CONSTRAINT FK_event_detail_infos_button_link_type_id_event_button_link_types_event_button_link_type_no FOREIGN KEY (button_link_type_id)
--         REFERENCES event_button_link_types (event_button_link_type_no);

-- ALTER TABLE event_detail_infos
--     ADD CONSTRAINT FK_event_detail_infos_event_info_id_event_infos_event_info_no FOREIGN KEY (event_info_id)
--         REFERENCES event_infos (event_info_no);


-- -- event_detail_product_infos Table Create SQL
-- CREATE TABLE event_detail_product_infos
-- (
--     `event_detail_product_info_no`  INT        NOT NULL    AUTO_INCREMENT COMMENT 'id', 
--     `product_order_id`              INT        NOT NULL    COMMENT '진열순위', 
--     `product_id`                    INT        NOT NULL    COMMENT '상품 아이디', 
--     `event_info_id`                 INT        NOT NULL    COMMENT '기획전 정보 아이디', 
--     `is_deleted`                    TINYINT    NOT NULL    COMMENT '삭제여부', 
--     PRIMARY KEY (event_detail_product_info_no)
-- );

-- ALTER TABLE event_detail_product_infos COMMENT '이벤트 상세정보(매핑 상품)';

-- ALTER TABLE event_detail_product_infos
--     ADD CONSTRAINT FK_event_detail_product_infos_product_id_product_infos_product_info_no FOREIGN KEY (product_id)
--         REFERENCES product_infos (product_info_no);

-- ALTER TABLE event_detail_product_infos
--     ADD CONSTRAINT FK_event_detail_product_infos_event_info_id_event_infos_event_info_no FOREIGN KEY (event_info_id)
--         REFERENCES event_infos (event_info_no);



