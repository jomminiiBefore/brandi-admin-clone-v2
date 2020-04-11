drop database brandi;

create database brandi character set utf8mb4 collate utf8mb4_general_ci;
use brandi;

-- authorization_types Table Create SQL
CREATE TABLE authorization_types
(
    `auth_type_no`  INT            NOT NULL    AUTO_INCREMENT COMMENT 'id',
    `name`          VARCHAR(10)    NOT NULL    COMMENT '타입명',
    `is_deleted`    TINYINT        NOT NULL    DEFAULT FALSE COMMENT '삭제여부',
    PRIMARY KEY (auth_type_no)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci COMMENT '권한 타입(마스터 or 셀러)' ;

INSERT INTO authorization_types
(
	auth_type_no,
	name
) VALUES (
	1, -- no
	'마스터'
),(
	2, -- no
	'셀러'
);


-- accounts Table Create SQL
CREATE TABLE accounts
(
    `account_no`    INT            NOT NULL    AUTO_INCREMENT COMMENT 'id',
    `auth_type_id`  INT            NOT NULL    COMMENT '권한 타입 외래키',
    `login_id`      VARCHAR(45)    NOT NULL    UNIQUE COMMENT '로그인 아이디',
    `password`      VARCHAR(80)    NOT NULL    COMMENT '비밀번호',
    `is_deleted`    TINYINT        NOT NULL    DEFAULT FALSE COMMENT '삭제여부',
    PRIMARY KEY (account_no)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci COMMENT '계정 정보';

ALTER TABLE accounts
    ADD CONSTRAINT FK_auth_type_id FOREIGN KEY (auth_type_id)
        REFERENCES authorization_types (auth_type_no);

INSERT INTO accounts
(
	account_no,
	auth_type_id,
	login_id,
	password,
	is_deleted
) VAlUES (
	1, -- account_no
	1, -- auth_type_id
	'master',
	'$2b$12$iJN2OxkW69HHb6cVLeRjPuAQoGYKIZY.nlCbwJVRzrWGUrvmJRypi',
	0
),(
	2, -- account_no
	2, -- auth_type_id
	'seller',
	'$2b$12$iJN2OxkW69HHb6cVLeRjPuAQoGYKIZY.nlCbwJVRzrWGUrvmJRypi',
	0
),(
	3, -- account_no
	2, -- auth_type_id
	'seller_shopping',
	'$2b$12$iJN2OxkW69HHb6cVLeRjPuAQoGYKIZY.nlCbwJVRzrWGUrvmJRypi',
	1
),(
	4, -- account_no
	2, -- auth_type_id
	'seller_market',
	'$2b$12$iJN2OxkW69HHb6cVLeRjPuAQoGYKIZY.nlCbwJVRzrWGUrvmJRypi',
	0
),(
	5, -- account_no
	2, -- auth_type_id
	'seller_loadshop',
	'$2b$12$iJN2OxkW69HHb6cVLeRjPuAQoGYKIZY.nlCbwJVRzrWGUrvmJRypi,',
	0
),(
	6, -- account_no
	2, -- auth_type_id
	'seller_designer',
	'$2b$12$iJN2OxkW69HHb6cVLeRjPuAQoGYKIZY.nlCbwJVRzrWGUrvmJRypi',
	0
),(
	7, -- account_no
	2, -- auth_type_id
	'seller_general',
	'$2b$12$iJN2OxkW69HHb6cVLeRjPuAQoGYKIZY.nlCbwJVRzrWGUrvmJRypi',
	0
),(
	8, -- account_no
	2, -- auth_type_id
	'seller_national',
	'$2b$12$iJN2OxkW69HHb6cVLeRjPuAQoGYKIZY.nlCbwJVRzrWGUrvmJRypi',
	0
),(
	9, -- account_no
	2, -- auth_type_id
	'seller_beauty',
	'$2b$12$iJN2OxkW69HHb6cVLeRjPuAQoGYKIZY.nlCbwJVRzrWGUrvmJRypi',
	1
);


-- product_sorts Table Create SQL
CREATE TABLE product_sorts
(
    `product_sort_no`  INT            NOT NULL    AUTO_INCREMENT COMMENT 'id',
    `name`             VARCHAR(10)    NOT NULL    UNIQUE COMMENT '분류명',
    `is_deleted`       TINYINT        NOT NULL    DEFAULT FALSE COMMENT '삭제여부',
    PRIMARY KEY (product_sort_no)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci COMMENT '상품 분류(트렌드, 브랜드, 뷰티)';

INSERT INTO product_sorts
(
	product_sort_no,
	name
) VALUES (
	1,
	'트렌드'
),(
	2,
	'브랜드'
),(
	3,
	'뷰티'
);


-- seller_accounts Table Create SQL
CREATE TABLE seller_accounts
(
    `seller_account_no`  INT         NOT NULL    AUTO_INCREMENT COMMENT 'id',
    `account_id`         INT         NOT NULL    COMMENT '계정 정보 외래키',
    `created_at`         DATETIME    NOT NULL    DEFAULT CURRENT_TIMESTAMP COMMENT '최초 등록일시',
    `is_deleted`         TINYINT     NOT NULL    DEFAULT FALSE COMMENT '삭제여부',
    PRIMARY KEY (seller_account_no)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci COMMENT '셀러 계정';

ALTER TABLE seller_accounts
    ADD CONSTRAINT FK_account_id FOREIGN KEY (account_id)
        REFERENCES accounts (account_no);

INSERT INTO seller_accounts
(
	seller_account_no,
	account_id
) VALUES (
	1,
	1
),(
	2,
	2
),(
	3,
	3
),(
	4,
	4
),(
	5,
	5
);


-- seller_types Table Create SQL
CREATE TABLE seller_types
(
    `seller_type_no`   INT            NOT NULL    AUTO_INCREMENT COMMENT 'id',
    `product_sort_id`  INT            NOT NULL    COMMENT '상품 분류 외래키',
    `name`             VARCHAR(45)    NOT NULL    UNIQUE COMMENT '셀러 속성명',
    `is_deleted`       TINYINT        NOT NULL    DEFAULT FALSE COMMENT '삭제여부',
    PRIMARY KEY (seller_type_no)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci COMMENT '셀러 속성(쇼핑몰, 마켓, 로드샵, 디자이너브랜드 ...)';

ALTER TABLE seller_types
    ADD CONSTRAINT FK_product_sort_id FOREIGN KEY (product_sort_id)
        REFERENCES product_sorts (product_sort_no);

INSERT INTO seller_types
(
	seller_type_no,
	product_sort_id,
	name
) VALUES (
	1,
	1,
	'쇼핑몰'
),(
	2,
	1,
	'마켓'
),(
	3,
	1,
	'로드샵'
),(
	4,
	2,
	'디자이너브랜드'
),(
	5,
	2,
	'제너럴브랜드'
),(
	6,
	2,
	'내셔널브랜드'
),(
	7,
	3,
	'뷰티'
);


-- seller_statuses Table Create SQL
CREATE TABLE seller_statuses
(
    `status_no`   INT            NOT NULL    AUTO_INCREMENT,
    `name`        VARCHAR(45)    NOT NULL    UNIQUE COMMENT '셀러 상태명',
    `is_deleted`  TINYINT        NOT NULL    DEFAULT FALSE COMMENT '삭제여부',
    PRIMARY KEY (status_no)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci COMMENT '셀러 상태(입점, 입점대기, 퇴점, 퇴점대기, 휴점)';

INSERT INTO seller_statuses
(
	status_no,
	name
) VALUES (
	1,
	'입점대기'
),(
	2,
	'입점'
),(
	3,
	'퇴점대기'
),(
	4,
	'퇴점'
),(
	5,
	'휴점'
);


-- brandi_app_users Table Create SQL
CREATE TABLE brandi_app_users
(
    `app_user_no`  INT            NOT NULL    AUTO_INCREMENT COMMENT 'id',
    `app_id`       VARCHAR(45)    NOT NULL    UNIQUE COMMENT '브랜디 앱 아이디',
    `is_deleted`   TINYINT        NOT NULL    DEFAULT FALSE COMMENT '삭제여부',
    PRIMARY KEY (app_user_no)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci COMMENT '브랜디 앱 유저';

INSERT INTO brandi_app_users
(
	app_user_no,
	app_id
) VALUES (
	1,
	'brandi01'
),(
	2,
	'brandi02'
),(
	3,
	'brandi03'
),(
	4,
	'brandi04'
),(
	5,
	'brandi05'
);


-- seller_infos Table Create SQL
CREATE TABLE seller_infos
(
    `seller_info_no`             INT              NOT NULL    AUTO_INCREMENT COMMENT 'id',
    `seller_account_id`          INT              NOT NULL    COMMENT '셀러 계정 외래키',
    `profile_image_url`          VARCHAR(200)     NULL        COMMENT '프로필 이미지 url',
    `seller_status_id`           INT              NOT NULL    COMMENT '셀러 상태 외래키',
    `seller_type_id`             INT              NOT NULL    COMMENT '셀러 속성 외래키',
    `product_sort_id`            INT              NOT NULL    COMMENT '상품 분류 외래키',
    `name_kr`                    VARCHAR(45)      NOT NULL    COMMENT '셀러 한글명',
    `name_en`                    VARCHAR(45)      NOT NULL    COMMENT '셀러 영문명',
    `brandi_app_user_id`         INT              NULL        COMMENT '브랜디 앱 유저 외래키',
    `ceo_name`                   VARCHAR(45)      NULL        COMMENT '대표자명',
    `company_name`               VARCHAR(45)      NULL        COMMENT '사업자명',
    `business_number`            VARCHAR(12)      NULL        COMMENT '사업자번호',
    `certificate_image_url`      VARCHAR(200)     NULL        COMMENT '사업자등록증 이미지 url',
    `online_business_number`     VARCHAR(45)      NULL        COMMENT '통신판매업번호',
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
    `modifier`                   INT              NOT NULL    COMMENT '변경실행자 계정 외래키',
    `start_time`                 DATETIME         NOT NULL    DEFAULT CURRENT_TIMESTAMP COMMENT '시작일시',
    `close_time`                 DATETIME         NOT NULL    DEFAULT '2037-12-31 23:59:59' COMMENT '종료일시',
    `is_deleted`                 TINYINT          NOT NULL    DEFAULT FALSE COMMENT '삭제여부',
    PRIMARY KEY (seller_info_no)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci COMMENT '셀러 수정페이지 전체 / 셀러 정보 수정할때마다 새로운 row로 생성(변경이력 관리 용)';

ALTER TABLE seller_infos
    ADD CONSTRAINT FK_seller_type_id FOREIGN KEY (seller_type_id)
        REFERENCES seller_types (seller_type_no);

ALTER TABLE seller_infos
    ADD CONSTRAINT FK_seller_infos_product_sort_id FOREIGN KEY (product_sort_id)
        REFERENCES product_sorts (product_sort_no);

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
    ADD CONSTRAINT FK_seller_info_modifier FOREIGN KEY (modifier)
        REFERENCES accounts (account_no);

INSERT INTO seller_infos
(
    seller_info_no,
    seller_account_id,
    profile_image_url,
    seller_status_id,
    seller_type_id,
    product_sort_id,
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
    modifier,
    start_time,
    close_time
) VALUES (
    1,
    1, -- seller_account_id
    'https://image.brandi.me/seller/miu_blanc_profile_1541096303.jpeg', -- profile_image_url
    2, -- seller_status_id, 입점
    1, -- seller_type_id
    1, -- product_sort_id
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
    '23:59', -- weekday_end_time
    '10:00', -- weekend_start_time
    '23:59', -- weekend_end_time
    '하나은행', -- bank_name
    '브랜디', -- bank_holder_name
    '12-12345-12345123', -- account_number
    1, -- modifier
    '2020-04-05 23:59:59', -- start_time
    '2037-12-31 23:59:59' -- close_time
),
(
    2,
    2, -- seller_account_id
    'https://image.brandi.me/seller/miu_blanc_profile_1541096303.jpeg', -- profile_image_url
    1, -- seller_status_id, 입점대기
    2, -- seller_type_id
    1, -- product_sort_id
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
    '23:59', -- weekday_end_time
    '10:00', -- weekend_start_time
    '23:59', -- weekend_end_time
    '하나은행', -- bank_name
    '브랜디', -- bank_holder_name
    '12-12345-12345123', -- account_number
    2, -- modifier
    '2020-04-03 23:59:59', -- start_time
    '2020-04-05 23:59:59' -- close_time
),
(
    3,
    3, --  seller_account_id
    'https://image.brandi.me/seller/miu_blanc_profile_1541096303.jpeg', --  profile_image_url
    3, -- seller_status_id, 퇴점대기
    3, -- seller_type_id
    1, -- product_sort_id
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
    '23:59', -- weekday_end_time
    '10:00', -- weekend_start_time
    '23:59', -- weekend_end_time
    '하나은행', -- bank_name
    '브랜디', -- bank_holder_name
    '12-12345-12345123', -- account_number
    3, -- modifier
    '2020-04-05 23:59:59', -- start_time
    '2037-12-31 23:59:59' -- close_time
),
(
    4,
    4, --  seller_account_id
    'https://image.brandi.me/seller/miu_blanc_profile_1541096303.jpeg', --  profile_image_url
    4, -- seller_status_id, 퇴점
    4, -- seller_type_id,
    2, -- product_sort_id
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
    '23:59', -- weekday_end_time
    '10:00', -- weekend_start_time
    '23:59', -- weekend_end_time
    '하나은행', -- bank_name
    '브랜디', -- bank_holder_name
    '12-12345-12345123', -- account_number
    4, -- modifier
    '2020-04-05 23:59:59', -- start_time
    '2037-12-31 23:59:59' -- close_time
),
(
    5,
    5, --  seller_account_id
    'https://image.brandi.me/seller/miu_blanc_profile_1541096303.jpeg', --  profile_image_url
    5, -- seller_status_id, 휴점
    5, -- seller_type_id
    2, -- product_sort_id
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
    '23:59', -- weekday_end_time
    '10:00', -- weekend_start_time
    '23:59', -- weekend_end_time
    '하나은행', -- bank_name
    '브랜디', -- bank_holder_name
    '12-12345-12345123', -- account_number
    5, -- modifier
    '2020-04-03 23:59:59', -- start_time
    '2037-12-31 23:59:59' -- close_time
),
(
    6,
    2, -- seller_account_id
    'https://image.brandi.me/seller/miu_blanc_profile_1541096303.jpeg', -- profile_image_url
    2, -- seller_status_id, 입점
    2, -- seller_type_id
    1, -- product_sort_id
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
    '23:59', -- weekday_end_time
    '10:00', -- weekend_start_time
    '23:59', -- weekend_end_time
    '하나은행2', -- bank_name
    '브랜디2', -- bank_holder_name
    '12-12345-12345123', -- account_number
    2, -- modifier
    '2020-04-05 23:59:59', -- start_time
    '2037-12-31 23:59:59' -- close_time
);


-- first_categories Table Create SQL
CREATE TABLE first_categories
(
    `first_category_no`  INT            NOT NULL    AUTO_INCREMENT COMMENT 'id',
    `name`               VARCHAR(45)    NOT NULL    COMMENT '카테고리명',
    `is_deleted`         TINYINT        NULL        DEFAULT FALSE COMMENT '삭제여부',
    `product_sort_id`    INT            NOT NULL    COMMENT '상품 분류 외래키',
    PRIMARY KEY (first_category_no)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci COMMENT '1차 카테고리';

ALTER TABLE first_categories
    ADD CONSTRAINT FK_first_categories_product_sort_id FOREIGN KEY (product_sort_id)
        REFERENCES product_sorts (product_sort_no);

INSERT INTO first_categories
(
	first_category_no,
	name,
	product_sort_id
) VALUES (
	1,
	'아우터',
	1
),(
	2,
	'상의',
	1
),(
	3,
	'스커트',
	1
),(
	4,
	'바지',
	1
),(
	5,
	'원피스',
	1
),(
	6,
	'신발',
	1
),(
	7,
	'가방',
	1
),(
	8,
	'잡화',
	 1
),(
	9,
	'주얼리',
	1
),(
	10,
	'라이프웨어',
	1
),(
	11,
	'빅사이즈',
	1
),(
	12,
	'아우터',
	2
),(
	13,
	'상의',
 	2
),(
	14,
	'원피스',
	2
),(
	15,
	'팬츠',
	2
),(
	16,
	'스커트',
	2
),(
	17,
	'슈즈',
	2
),(
	18,
	'가방',
	2
),(
	19,
	'악세서리',
	2
),(
	20,
	'스웜웨어',
	2
),(
	21,
	'언더웨어',
	2
),(
	22,
	'스킨케어',
	3
),(
	23,
	'메이크업',
	3
),(
	24,
	'바디/헤어',
	3
),(
	25,
	'네일',
	3
),(
	26,
	'이너뷰티',
	3
),(
	27,
	'애슬레저',
	3
),(
	28,
	'홈트레이닝',
	3
),(
	29,
	'푸드',
	3
),(
	30,
	'기타',
	3
);


-- second_categories Table Create SQL
CREATE TABLE second_categories
(
    `second_category_no`  INT            NOT NULL    AUTO_INCREMENT COMMENT 'id',
    `name`                VARCHAR(45)    NOT NULL    COMMENT '카테고리명',
    `first_category_id`   INT            NOT NULL    COMMENT '1차 카테고리 아이디',
    `is_deleted`          TINYINT        NOT NULL    DEFAULT FALSE COMMENT '삭제여부',
    PRIMARY KEY (second_category_no)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci COMMENT '2차 카테고리';

ALTER TABLE second_categories
    ADD CONSTRAINT FK_first_category_no FOREIGN KEY (first_category_id)
        REFERENCES first_categories (first_category_no);

INSERT INTO second_categories
(
    second_category_no,
    name,
    first_category_id
) VALUES (
	1,
	'코트',
	1
),(
	2,
	'점퍼',
	1
),(
	3,
	'재킷',
	1
),(
	4,
	'가디건',
	1
),(
	5,
	'니트',
	2
),(
	6,
	'티셔츠',
	2
),(
	7,
	'블라우스/셔츠',
	2
),(
	8,
	'후드/맨투맨',
	2
),(
	9,
	'베스트',
	2
),(
	10,
	'미니스커트',
	3
),(
	11,
	'롱스커트',
	3
),(
	12,
	'청바지',
	4
),(
	13,
	'슬랙스',
 	4
),(
	14,
	'반바지',
	4
),(
	15,
	'레깅스',
	4
),(
	16,
	'스니커즈',
	6
),(
	17,
	'부츠',
	6
),(
	18,
	'힐',
	6
),(
	19,
	'플랫/로퍼',
	6
),(
	20,
	'샌들',
	6
),(
	21,
	'크로스백',
	7
),(
	22,
	'클러치',
	7
),(
	23,
	'숄더백',
	7
),(
	24,
	'토트백',
	7
),(
	25,
	'백팩',
	7
),(
	26,
	'휴대폰케이스',
	8
),(
	27,
	'지갑/파우치',
	8
),(
	28,
	'스카프/머플러',
	8
),(
	29,
	'모자',
	8
),(
	30,
	'양말',
	8
),(
	31,
	'시계',
	8
),(
	32,
	'아이웨어',
	8
),(
	33,
	'기타',
	8
),(
	34,
	'귀걸이',
	9
),(
	35,
	'목걸이/팔찌',
	9
),(
	36,
	'반지',
	9
),(
	37,
	'언더웨어',
	10
),(
	38,
	'홈웨어',
	10
),(
	39,
	'스윔웨어',
	10
),(
	40,
	'아우터',
	11
),(
	41,
	'상의',
	11
),(
	42,
	'스커트',
	11
),(
	43,
	'바지',
	11
),(
	44,
	'드레스',
	11
),(
	45,
	'자켓',
	12
),(
	46,
	'코드',
	12
),(
	47,
	'집업',
	12
),(
	48,
	'가디건',
	12
),(
	49,
	'점퍼',
	12
),(
	50,
	'기타',
	12
),(
	51,
	'티/반팔티',
	13
),(
	52,
	'니트',
	13
),(
	53,
	'맨투맨',
	13
),(
	54,
	'후디',
	13
),(
	55,
	'셔츠/블라우스',
	13
),(
	56,
	'민소매/나시',
	13
),(
	57,
	'기타',
	13
),(
	58,
	'미니',
	14
),(
	59,
	'미디',
	14
),(
	60,
	'롱',
	14
),(
	61,
	'점프수트',
	14
),(
	62,
	'기타',
	14
),(
	63,
	'스키니',
	15
),(
	64,
	'스트레이트',
	15
),(
	65,
	'와이드',
	15
),(
	66,
	'숏',
	15
),(
	67,
	'기타',
	15
),(
	68,
	'미니',
	16
),(
	69,
	'미디',
	16
),(
	70,
	'롱',
	16
),(
	71,
	'기타',
	16
),(
	72,
	'스니커즈',
	17
),(
	73,
	'러닝화',
	17
),(
	74,
	'플랫',
	17
),(
	75,
	'로퍼',
	17
),(
	76,
	'펌프스',
	17
),(
	77,
	'부츠',
	17
),(
	78,
	'샌들/슬리퍼',
	17
),(
	79,
	'기타',
	17
),(
	80,
	'숄더백',
	18
),(
	81,
	'토트백',
	18
),(
	82,
	'미니백',
	18
),(
	83,
	'캔버스백',
	18
),(
	84,
	'백팩',
	18
),(
	85,
	'지갑/카드케이스',
	18
),(
	86,
	'클러치/파우치',
	18
),(
	87,
	'기타',
	18
),(
	88,
	'귀걸이',
	19
),(
	89,
	'반지',
	19
),(
	90,
	'팔찌/발찌',
	19
),(
	91,
	'시계',
	19
),(
	92,
	'스카프/머플러',
	19
),(
	93,
	'모자',
	19
),(
	94,
	'양말',
	19
),(
	95,
	'폰 악세서리',
	19
),(
	96,
	'헤어 악세서리',
	19
),(
	97,
	'선글라스/아이웨어',
	19
),(
	98,
	'시즌아이템',
	19
),(
	99,
	'기타',
	19
),(
	100,
	'비키니',
	20
),(
	101,
	'원피스',
	20
),(
	102,
	'레쉬가드',
	20
),(
	103,
	'기타',
	20
),(
	104,
	'브라',
	21
),(
	105,
	'팬티',
	21
),(
	106,
	'세트',
	21
),(
	107,
	'슬립',
	21
),(
	108,
	'홈웨어',
	21
),(
	109,
	'베이스',
	23
),(
	110,
	'색조',
	23
),(
	111,
	'아우터',
	27
),(
	112,
	'상의',
	27
),(
	113,
	'하의',
	27
),(
	114,
	'기타',
	27
);


-- color_filters Table Create SQL
CREATE TABLE color_filters
(
    `color_filter_no`  INT             NOT NULL    AUTO_INCREMENT COMMENT 'id',
    `name_kr`          VARCHAR(10)     NOT NULL    UNIQUE COMMENT '필터 한글명',
    `name_en`          VARCHAR(20)     NOT NULL    UNIQUE COMMENT '필터 영문명',
    `image_url`        VARCHAR(200)    NOT NULL    UNIQUE COMMENT '이미지 url',
    `is_deleted`       TINYINT         NOT NULL    DEFAULT FALSE COMMENT '삭제여부',
    PRIMARY KEY (color_filter_no)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci COMMENT '색상 필터';

INSERT INTO color_filters
(
	color_filter_no,
	name_kr, name_en,
	image_url
) VALUES (
	1,
	'빨강',
	'Red',
	'http://sadmin.brandi.co.kr/include/img/product/color/red.png'
),(
	2,
	'주황',
	'Orange',
	'http://sadmin.brandi.co.kr/include/img/product/color/orange.png'
),(
	3,
	'노랑',
	'Yellow',
	'http://sadmin.brandi.co.kr/include/img/product/color/yellow.png'
),(
	4,
	'베이지',
	'Beige',
	'http://sadmin.brandi.co.kr/include/img/product/color/beige.png'
),(
	5,
	'갈색',
	'Brown',
	'http://sadmin.brandi.co.kr/include/img/product/color/brown.png'
),(
	6,
	'초록',
	'Green',
	'http://sadmin.brandi.co.kr/include/img/product/color/green.png'
),(
	7,
	'민트',
	'Mint',
	'http://sadmin.brandi.co.kr/include/img/product/color/mint.png'
),(
	8,
	'하늘',
	'Skyblue',
	'http://sadmin.brandi.co.kr/include/img/product/color/skyblue.png'
),(
	9,
	'파랑',
	'Blue',
	'http://sadmin.brandi.co.kr/include/img/product/color/blue.png'
),(
	10,
	'남색',
	'Navy',
	'http://sadmin.brandi.co.kr/include/img/product/color/navy.png'
),(
	11,
	'보라',
	'Violet',
	'http://sadmin.brandi.co.kr/include/img/product/color/violet.png'
),(
	12,
	'분홍',
	'Pink',
	'http://sadmin.brandi.co.kr/include/img/product/color/pink.png'
),(
	13,
	'흰색',
	'White',
	'http://sadmin.brandi.co.kr/include/img/product/color/white.png'
),(
	14,
	'회색',
	'Gray',
	'http://sadmin.brandi.co.kr/include/img/product/color/gray.png'
),(
	15,
	'검정',
	'Black',
	'http://sadmin.brandi.co.kr/include/img/product/color/black.png'
),(
	16,
	'골드',
	'Gold',
	'http://sadmin.brandi.co.kr/include/img/product/color/gold.png'
),(
	17,
	'로즈골드',
	'Rosegold',
	'http://sadmin.brandi.co.kr/include/img/product/color/rosegold.png'
),(
	18,
	'실버',
	'Sliver',
	'http://sadmin.brandi.co.kr/include/img/product/color/silver.png'
),(
	19,
	'선택안함',
	'선택안함',
	'선택안함'
);


-- style_filters Table Create SQL
CREATE TABLE style_filters
(
    `style_filter_no`  INT            NOT NULL    AUTO_INCREMENT COMMENT 'id',
    `name`             VARCHAR(45)    NOT NULL    UNIQUE COMMENT '필터명',
    `is_deleted`       TINYINT        NOT NULL    DEFAULT FALSE COMMENT '삭제여부',
    PRIMARY KEY (style_filter_no)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci COMMENT '스타일필터';

INSERT INTO style_filters
(
	style_filter_no,
	name
) VALUES (
	1,
	'선택안함'
),(
	2,
	'심플베이직'
),(
	3,
	'러블리'
),(
	4,
	'페미닌'
),(
	5,
	'캐주얼'
),(
	6,
	'섹시글램'
);


-- products Table Create SQL
CREATE TABLE products
(
    `product_no`  INT         NOT NULL    AUTO_INCREMENT COMMENT 'id',
    `uploader`    INT         NOT NULL    COMMENT '등록자',
    `created_at`  DATETIME    NOT NULL    DEFAULT CURRENT_TIMESTAMP COMMENT '최초 등록일시',
    `is_deleted`  TINYINT     NOT NULL    DEFAULT FALSE COMMENT '삭제여부',
    PRIMARY KEY (product_no)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci COMMENT '상품 번호';

ALTER TABLE products
    ADD CONSTRAINT FK_uploader FOREIGN KEY (uploader)
        REFERENCES accounts (account_no);

INSERT INTO products (
    product_no,
    uploader,
    created_at
) VALUES (
    1, -- product_no
    1, -- uploader
    '2020-03-31 09:00:00' -- created_at
),
(
    2, -- product_no
    3, -- uploader
    '2020-04-01 09:00:00' -- created_at
),
(
    3, -- product_no
    4, -- uploader
    '2020-04-02 09:00:00' -- created_at
),
(
    4, -- product_no
    4, -- uploader
    '2020-04-03 09:00:00' -- created_at
),
(
    5, -- product_no
    4, -- uploader
    '2020-04-04 09:00:00' -- created_at
),
(
    6, -- product_no
    5, -- uploader
    '2020-04-05 09:00:00' -- created_at
);

-- product_infos Table Create SQL
CREATE TABLE product_infos
(
    `product_info_no`      INT              NOT NULL    AUTO_INCREMENT COMMENT 'id',
    `seller_id`            INT              NOT NULL    COMMENT '셀러 계정 외래키',
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
    `start_time`           DATETIME         NOT NULL    DEFAULT CURRENT_TIMESTAMP COMMENT '시작일시',
    `close_time`           DATETIME         NOT NULL    DEFAULT '2037-12-31 23:59:59' COMMENT '종료일시',
    `modifier`             INT              NOT NULL    COMMENT '수정자',
    `is_deleted`           TINYINT          NOT NULL    DEFAULT FALSE COMMENT '삭제여부',
    `product_id`           INT              NOT NULL    COMMENT '상품 아이디',
    PRIMARY KEY (product_info_no)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci COMMENT '상품 정보';

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
    ADD CONSTRAINT FK_product_info_modifier FOREIGN KEY (modifier)
        REFERENCES accounts (account_no);

ALTER TABLE product_infos
    ADD CONSTRAINT FK_seller_id FOREIGN KEY (seller_id)
        REFERENCES seller_accounts (seller_account_no);
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
    start_time,
    modifier,
    product_id
) VALUES
(
    1, -- product_info_no
    2, -- seller_id
    1, -- is_available
    1, -- is_on_display
    1, -- product_sort_id
    3, -- first_category_id
    10, -- second_category_id
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
    '2020-03-31 09:00:00', -- start_time
    1, -- modifier, account_no
    1 -- product_id
),
(
    2, -- product_info_no
    3, -- seller_id
    1, -- is_available
    2, -- is_on_display
    2, -- product_sort_id
    6, -- first_category_id
    17, -- second_category_id
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
    '2020-04-01 09:00:00', -- start_time
    3, -- modifier, account_no
    2 -- product_id
),
(
    3, -- product_info_no
    4, -- seller_id
    1, -- is_available
    1, -- is_on_display
    1, -- product_sort_id
    13, -- first_category_id
    51, -- second_category_id
    '상품3', -- name
    '브랜디 상품 입니다.', -- short_description
    1, -- color_filter_id
    1, -- style_filter_id
    '<h1>브랜디 상품 입니다. 브랜디 상품 입니다.</h1>', -- long_description
    'https://www.youtube.com/watch?v=twGpF2v_w-s', -- youtube_url
    -1, -- stock, 관리안함이면 -1
    15000, -- price
    0.4, -- discount_rate
    '2020-05-12 23:59:59', -- discount_start_time
    '2020-06-12 23:59:59', -- discount_end_time
    1, -- min_unit
    10, -- max_unit
    '2020-04-02 09:00:00', -- start_time
    4, -- modifier, account_no
    3 -- product_id
),
(
    4, -- product_info_no
    4, -- seller_id
    1, -- is_available
    1, -- is_on_display
    1, -- product_sort_id
    15, -- first_category_id
    63, -- second_category_id
    '상품4', -- name
    '브랜디 상품 입니다.', -- short_description
    1, -- color_filter_id
    1, -- style_filter_id
    '<h1>브랜디 상품 입니다. 브랜디 상품 입니다.</h1>', -- long_description
    'https://www.youtube.com/watch?v=twGpF2v_w-s', -- youtube_url
    -1, -- stock, 관리안함이면 -1
    12080, -- price
    0.3, -- discount_rate
    '2020-05-12 23:59:59', -- discount_start_time
    '2020-06-12 23:59:59', -- discount_end_time
    1, -- min_unit
    10, -- max_unit
    '2020-04-03 09:00:00', -- start_time
    4, -- modifier, account_no
    4 -- product_id
),
(
    5, -- product_info_no
    4, -- seller_id
    1, -- is_available
    1, -- is_on_display
    1, -- product_sort_id
    19, -- first_category_id
    94, -- second_category_id
    '상품5', -- name
    '브랜디 상품 입니다.', -- short_description
    1, -- color_filter_id
    1, -- style_filter_id
    '<h1>브랜디 상품 입니다. 브랜디 상품 입니다.</h1>', -- long_description
    'https://www.youtube.com/watch?v=twGpF2v_w-s', -- youtube_url
    -1, -- stock, 관리안함이면 -1
    129000, -- price
    0.45, -- discount_rate
    '2020-05-12 23:59:59', -- discount_start_time
    '2020-06-12 23:59:59', -- discount_end_time
    1, -- min_unit
    10, -- max_unit
    '2020-04-04 09:00:00', -- start_time
    4, -- modifier, account_no
    5 -- product_id
),
(
    6, -- product_info_no
    5, -- seller_id
    1, -- is_available
    1, -- is_on_display
    1, -- product_sort_id
    20, -- first_category_id
    102, -- second_category_id
    '상품6', -- name
    '브랜디 상품 입니다.', -- short_description
    1, -- color_filter_id
    1, -- style_filter_id
    '<h1>브랜디 상품 입니다. 브랜디 상품 입니다.</h1>', -- long_description
    'https://www.youtube.com/watch?v=twGpF2v_w-s', -- youtube_url
    -1, -- stock, 관리안함이면 -1
    18000, -- price
    0.15, -- discount_rate
    '2020-05-12 23:59:59', -- discount_start_time
    '2020-06-12 23:59:59', -- discount_end_time
    1, -- min_unit
    10, -- max_unit
    '2020-04-05 09:00:00', -- start_time
    5, -- modifier, account_no
    6 -- product_id
);

-- event_types Table Create SQL
CREATE TABLE event_types
(
    `event_type_no`  INT            NOT NULL    AUTO_INCREMENT COMMENT 'id',
    `name`           VARCHAR(45)    NOT NULL    UNIQUE COMMENT '타입명',
    `is_deleted`     TINYINT        NOT NULL    DEFAULT FALSE COMMENT '삭제여부',
    PRIMARY KEY (event_type_no)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci COMMENT '기획전 타입(이벤트, 쿠폰, 상품(이미지,텍스트), 유튜브)';

INSERT INTO event_types (
	event_type_no,
	name
) VALUES (
	1,
	'이벤트'
),(
	2,
	'쿠폰'
),(
	3,
	'상품(이미지)'
),(
	4,
	'상품(텍스트)'
),(
	5,
	'유튜브'
);


-- event_sorts Table Create SQL
CREATE TABLE event_sorts
(
    `event_sort_no`  INT            NOT NULL    AUTO_INCREMENT COMMENT 'id',
    `name`           VARCHAR(45)    NOT NULL    COMMENT '종류명',
    `event_type_id`  INT            NOT NULL    COMMENT '기획전 타입 아이디',
    `is_deleted`     TINYINT        NOT NULL    DEFAULT FALSE COMMENT '삭제여부',
    PRIMARY KEY (event_sort_no)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci COMMENT '기획전 종류';

ALTER TABLE event_sorts
    ADD CONSTRAINT FK_event_type_id FOREIGN KEY (event_type_id)
        REFERENCES event_types (event_type_no);

INSERT INTO event_sorts
(
	event_sort_no,
	name,
	event_type_id
) VALUES(
	1,
	'댓글창 있음',
	1
),(
	2,
	'댓글창 없음',
	1
),(
	3,
	'브랜디배송상품(정률)',
	2
),(
	4,
	'브랜디배송상품(정액)',
	2
),(
	5,
	'셀러쿠폰(정률)-브레스',
	2
),(
	6,
	'셀러쿠폰(정액)-브레스',
	2
),(
	7,
	'전체상품(정률)',
	2
),(
	8,
	'전체상품(정액)',
	2
),(
	9,
	'상품',
	3
),(
	10,
	'버튼',
	3
),(
	11,
	'상품',
	4
),(
	12,
	'버튼',
	4
),(
	13,
	'상품',
	5
),(
	14,
	'버튼',
	5
);


-- events Table Create SQL
CREATE TABLE events
(
    `event_no`    INT         NOT NULL    AUTO_INCREMENT COMMENT 'id',
    `uploader`    INT         NOT NULL    COMMENT '등록자',
    `created_at`  DATETIME    NOT NULL    DEFAULT CURRENT_TIMESTAMP COMMENT '최초 등록일시',
    `is_deleted`  TINYINT     NOT NULL    DEFAULT FALSE COMMENT '삭제여부',
    PRIMARY KEY (event_no)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci COMMENT '기획전';

ALTER TABLE events
    ADD CONSTRAINT FK_event_uploader FOREIGN KEY (uploader)
        REFERENCES accounts (account_no);

INSERT INTO events (
    event_no,
    uploader
) VALUES (
    1, -- event_no
    1 -- uploader
),
(
    2, -- event_no
    2 -- uploader
),
(
    3, -- event_no
    3 -- uploader
),
(
    4, -- event_no
    4 -- uploader
),
(
    5, -- event_no
    5 -- uploader
),
(
    6, -- event_no
    6 -- uploader
),
(
    7, -- event_no
    3 -- uploader
),
(
    8, -- event_no
    4 -- uploader
);


-- event_infos Table Create SQL
CREATE TABLE event_infos
(
    `event_info_no`      INT             NOT NULL    AUTO_INCREMENT COMMENT 'id',
    `name`               VARCHAR(45)     NOT NULL    COMMENT '기획전명',
    `is_on_main`         TINYINT         NOT NULL    COMMENT '메인노출여부',
    `is_on_event`        TINYINT         NOT NULL    COMMENT '기획전 진열여부',
    `short_description`  VARCHAR(45)     NULL        COMMENT '기획전 간략설명',
    `event_start_time`   DATETIME        NOT NULL    COMMENT '기획전 기간_시작',
    `event_end_time`     DATETIME        NOT NULL    COMMENT '기획전 기간_종료',
    `banner_image_url`   VARCHAR(200)    NULL        COMMENT '기획전 배너 이미지_url',
    `detail_image_url`   VARCHAR(200)    NULL        COMMENT '기획전 상세 이미지_url',
    `long_description`   BLOB            NULL        COMMENT '기획전 상세설명',
    `youtube_url`        VARCHAR(100)    NULL        COMMENT '유튜브 url',
    `event_type_id`      INT             NOT NULL    COMMENT '기획전 타입 아이디',
    `event_sort_id`      INT             NOT NULL    COMMENT '기획전 종류 아이디',
    `start_time`         DATETIME        NOT NULL    DEFAULT CURRENT_TIMESTAMP COMMENT '시작일시',
    `close_time`         DATETIME        NOT NULL    DEFAULT '2037-12-31 23:59:59' COMMENT '종료일시',
    `modifier`           INT             NOT NULL    COMMENT '수정자',
    `is_deleted`         TINYINT         NOT NULL    DEFAULT FALSE COMMENT '삭제여부',
    `event_id`           INT             NOT NULL    COMMENT '이벤트 아이디',
    PRIMARY KEY (event_info_no)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci COMMENT '기획전 정보(한번 저장하면 타입 수정 불가)';

ALTER TABLE event_infos
    ADD CONSTRAINT FK_event_infos_event_type_id FOREIGN KEY (event_type_id)
        REFERENCES event_types (event_type_no);

ALTER TABLE event_infos
    ADD CONSTRAINT FK_event_sort_id FOREIGN KEY (event_sort_id)
        REFERENCES event_sorts (event_sort_no);

ALTER TABLE event_infos
    ADD CONSTRAINT FK_event_id FOREIGN KEY (event_id)
        REFERENCES events (event_no);

ALTER TABLE event_infos
    ADD CONSTRAINT FK_event_info_modifier FOREIGN KEY (modifier)
        REFERENCES accounts (account_no);

INSERT INTO event_infos
(
	event_info_no,
	name,
	is_on_main,
	is_on_event,
	short_description,
	event_start_time,
	event_end_time,
	banner_image_url,
	detail_image_url,
	long_description,
	youtube_url,
	event_type_id,
	event_sort_id,
	start_time,
	modifier,
	event_id
) VALUES (
	1, -- event_info_no
	'이벤트1 이벤트', -- name
	1, -- is_on_main
	1, -- is_on_event
	'브랜디 기획전 이벤트타입 입니다.', -- short_description
	'2020-03-21 23:59:59', -- event_stat_time
	'2020-04-21 23:59:59', -- event_end_time
	'https://image.brandi.me/home/banner/bannerImage_1_1585288803.jpg', -- banner_image_url
	'https://image.brandi.me/event/2020/03/27/1585274063_bannerdetail.jpg', -- detail_image_url
	NULL, -- long_description
	NULL, -- youtube_url
	1, -- event_type_id, 이벤트타입
	1, -- event_sort_id
	(SELECT created_at FROM events WHERE event_no=1), -- start_time
	1, -- modifier, account_no
	1 -- event_id
),(
	2, -- event_info_no
	'이벤트2 쿠폰', -- name
	1, -- is_on_main
	1, -- is_on_event
	'브랜디 쿠폰 이벤트2 입니다.', -- short_description
	'2020-03-27 23:59:59', -- event_start_time
	'2020-04-19 23:59:59', -- event_end_time
	NULL, -- banner_image_url
	NULL, -- detail_image_url
	'<p>브랜디 이벤트2 입니다. 장문의 상세 설명입니다.</p>', -- long_description
	NULL, -- youtube_url
	2, -- event_type_id
	3, -- event_sort_id
	(SELECT created_at FROM events WHERE event_no=2), -- start_time
	2, -- modifier, account_no
	2 -- event_id
),(
	3, -- event_info_no
	'이벤트3 쿠폰', -- name
	1, -- is_on_main
	1, -- is_on_event
	'브랜디 이벤트3 입니다.', -- short_description
	'2020-03-27 23:59:59', -- event_stat_time
	'2020-04-19 23:59:59', -- event_end_time
	null, -- banner_image_url
	null, -- detail_image_url
	'<p>브랜디 이벤트3 입니다. 장문의 상세 설명입니다.</p>', -- long_description
	null, -- youtube_url
	2, -- event_type_id
	3, -- event_sort_id
	(SELECT created_at FROM events WHERE event_no=3), -- start_time
	2, -- modifier, account_no
	3 -- event_id
),(
	4, -- event_info_no
	'이벤트4 쿠폰', -- name
	1, -- is_on_main
	1, -- is_on_event
	'브랜디 이벤트4 입니다.', -- short_description
	'2020-03-27 23:59:59', -- event_stat_time
	'2020-04-19 23:59:59', -- event_end_time
	null, -- banner_image_url
	null, -- detail_image_url
	'<p>브랜디 이벤트4 입니다. 장문의 상세 설명입니다.</p>', -- long_description
	null, -- youtube_url
	2, -- event_type_id
	3, -- event_sort_id
	(SELECT created_at FROM events WHERE event_no=4), -- start_time
	2, -- modifier, account_no
	4 -- event_id
),(
	5, -- event_info_no
	'이벤트4 상품이미지', -- name
	1, -- is_on_main
	1, -- is_on_event
	NULL, -- short_description
	'2020-03-27 23:59:59', -- event_stat_time
	'2020-04-19 23:59:59', -- event_end_time
	'https://image.brandi.me/home/banner/bannerImage_126162_1585534016.jpg', -- banner_image_url
	'https://image.brandi.me/event/2020/03/27/1585300626_bannerdetail.jpg', -- detail_image_url
	NULL, -- long_description
	NULL, -- youtube_url
	3, -- event_type_id
	9, -- event_sort_id
	(SELECT created_at FROM events WHERE event_no=7), -- start_time
	2, -- modifier, account_no
	5 -- event_id
),(
	6, -- event_info_no
	'이벤트4 상품이미지', -- name
	1, -- is_on_main
	1, -- is_on_event
	NULL, -- short_description
	'2020-03-27 23:59:59', -- event_stat_time
	'2020-04-19 23:59:59', -- event_end_time
	'https://image.brandi.me/home/banner/bannerImage_126162_1585534016.jpg', -- banner_image_url
	'https://image.brandi.me/event/2020/03/27/1585300626_bannerdetail.jpg', -- detail_image_url
	NULL, -- long_description
	NULL, -- youtube_url
	3, -- event_type_id
	10, -- event_sort_id
	(SELECT created_at FROM events WHERE event_no=8), -- start_time
	2, -- modifier, account_no
	6 -- event_id
),(
	7, -- event_info_no
	'이벤트4 상품텍스트', -- name
	1, -- is_on_main
	1, -- is_on_event
	'브랜디 이벤트4 입니다.', -- short_description
	'2020-03-27 23:59:59', -- event_stat_time
	'2020-04-19 23:59:59', -- event_end_time
	'https://image.brandi.me/home/banner/bannerImage_126162_1585534016.jpg', -- banner_image_url
	NULL, -- detail_image_url
	null, -- long_description
	null, -- youtube_url
	4, -- event_type_id
	11, -- event_sort_id
	(SELECT created_at FROM events WHERE event_no=9), -- start_time
	2, -- modifier, account_no
	7 -- event_id
),(
	8, -- event_info_no
	'이벤트4 유튜브', -- name
	1, -- is_on_main
	1, -- is_on_event
	'브랜디 이벤트4 입니다.', -- short_description
	'2020-03-27 23:59:59', -- event_stat_time
	'2020-04-19 23:59:59', -- event_end_time
	'https://image.brandi.me/home/banner/bannerImage_126162_1585534016.jpg', -- banner_image_url
	'https://image.brandi.me/event/2020/03/27/1585300626_bannerdetail.jpg', -- detail_image_url
	NULL, -- long_description
	'https://youtu.be/jVTc9c3j8R4', -- youtube_url
	5, -- event_type_id
	13, -- event_sort_id
	(SELECT created_at FROM events WHERE event_no=10), -- start_time
	2, -- modifier, account_no
	8 -- event_id
);


-- image_sizes Table Create SQL
CREATE TABLE image_sizes
(
    `image_size_no`  INT           NOT NULL    AUTO_INCREMENT COMMENT 'id',
    `name`           VARCHAR(10)   NOT NULL    UNIQUE COMMENT '사이즈 명',
    `is_deleted`     TINYINT       NOT NULL    DEFAULT FALSE COMMENT '삭제여부',
    `height`         INT           NULL        COMMENT '높이',
    `width`          INT           NULL        COMMENT '세로',
    PRIMARY KEY (image_size_no)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci COMMENT '이미지 사이즈';

INSERT INTO image_sizes
(
	image_size_no,
	name,
	width
) VALUES (
	1,
	'L',
	640
),(
	2,
	'M',
	320
),(
	3,
	'S',
	150
);


-- event_button_link_types Table Create SQL
CREATE TABLE event_button_link_types
(
    `event_button_link_type_no`  INT            NOT NULL    AUTO_INCREMENT COMMENT 'id',
    `name`                       VARCHAR(45)    NOT NULL    UNIQUE COMMENT '링크타입명',
    `is_deleted`                 TINYINT        NOT NULL    DEFAULT FALSE COMMENT '삭제여부',
    PRIMARY KEY (event_button_link_type_no)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci COMMENT '이벤트 버튼 링크 타입';

INSERT INTO event_button_link_types
(
	event_button_link_type_no,
	name
) VALUES (
	1,
	'GNB 홈 - tab 홈'
),(
	2,
	'GNB 홈 - tab 베스트'
),(
	3,
	'GNB 홈 - tab 쇼핑몰*마켓'
),(
	4,
	'웹링크(웹뷰)'
),(
	5,
	'웹링크(외부)'
),(
	6,
	'쿠폰다운로드'
);


-- manager_infos Table Create SQL
CREATE TABLE manager_infos
(
    `manager_info_no`  INT             NOT NULL    AUTO_INCREMENT COMMENT 'id',
    `name`             VARCHAR(45)     NULL        COMMENT '담당자명',
    `contact_number`   VARCHAR(14)     NOT NULL    COMMENT '담당자 번호',
    `email`            VARCHAR(500)    NULL        COMMENT '담당자 이메일',
    `seller_info_id`   INT        	   NOT NULL    COMMENT '셀러 아이디',
    `is_deleted`       TINYINT         NOT NULL    DEFAULT FALSE COMMENT '삭제여부',
    `ranking`             INT             NULL        DEFAULT 1 COMMENT '담당자 순서',
    PRIMARY KEY (manager_info_no)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci COMMENT '셀러 담당자 정보';

ALTER TABLE manager_infos
    ADD CONSTRAINT FK_seller_info_id FOREIGN KEY (seller_info_id)
        REFERENCES seller_infos (seller_info_no);

INSERT INTO manager_infos
(
	manager_info_no,
	name,
	contact_number,
	email,
	seller_info_id
) VALUES (
	1,
	'김승준',
	'123-4567-8901',
	'hihi@gmail.com',
	1
),
(
	2,
	'윤희철',
	'456-342-9445',
	'you@gmail.com',
	2
),
(
	3,
	'이소헌',
	'456-342-9445',
	'me@gmail.com',
	3
),
(
	4,
	'이종민',
	'123-456-678',
	'unique@naver.com',
	4
),
(
	5,
	'최예지',
	'564-2132-5435',
	'event@yj.com',
	5
),
(
	6,
	'랜디',
	'564-2132-5435',
	'randi@yj.com',
	6
);

-- product_images Table Create SQL
CREATE TABLE product_images
(
    `product_image_no`  INT             NOT NULL    AUTO_INCREMENT COMMENT 'id',
    `image_url`         VARCHAR(200)    NOT NULL    COMMENT '이미지 url',
    `product_info_id`   INT             NOT NULL    COMMENT '상품 정보 외래키',
    `image_size_id`     INT             NOT NULL    COMMENT '이미지 사이즈 아이디',
    `image_order`       INT             NOT NULL    COMMENT '이미지 순서',
    `is_deleted`        TINYINT         NOT NULL    DEFAULT FALSE COMMENT '삭제여부',
    PRIMARY KEY (product_image_no)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci COMMENT '상품 이미지';

ALTER TABLE product_images
    ADD CONSTRAINT FK_product_images__no_id FOREIGN KEY (product_info_id)
        REFERENCES product_infos (product_info_no);

ALTER TABLE product_images
    ADD CONSTRAINT FK_image_size_id FOREIGN KEY (image_size_id)
        REFERENCES image_sizes (image_size_no);

INSERT INTO product_images
(
	product_image_no,
	image_url,
	product_info_id,
	image_size_id,
	image_order
) VALUES (
	1, -- product_image_no
	'https://image.brandi.me/cproduct/2020/03/20/14748562_1584631415_image1_M.jpg', -- image_url
	1, -- product_info_id
	1, -- image_size_id
	1 -- image_order
),(
	2, -- product_image_no
	'https://image.brandi.me/cproduct/2020/02/10/13664328_1581264198_image1_M.jpg', -- image_url
	1,  -- product_info_id
	2,  -- image_size_id
	1 -- image_order
),(
	3, -- product_image_no
	'https://image.brandi.me/cproductdetail/2020/02/10/051ab4b12c1dc3c3cdbed61944ae2799.jpeg',  -- image_url
	1,  -- product_info_id
	3,  -- image_size_id
	1 -- image_order
),(
	4,  -- product_image_no
	'https://image.brandi.me/cproductdetail/2020/03/16/63a59a5211cb6f5b6e69313411684950.JPG',  -- image_url
	2,  -- product_info_id
	1,  -- image_size_id
	1 -- image_order
),(
	5,  -- product_image_no
	'https://image.brandi.me/cproductdetail/2020/03/16/63a59a5211cb6f5b6e69313411684950.JPG',  -- image_url
	2,  -- product_info_id
	2,  -- image_size_id
	1 -- image_order
),(
	6,  -- product_image_no
	'https://image.brandi.me/cproductdetail/2020/03/16/63a59a5211cb6f5b6e69313411684950.JPG',  -- image_url
	2,  -- product_info_id
	3,  -- image_size_id
	1 -- image_order
),(
	7, -- product_image_no
	'https://image.brandi.me/cproduct/2020/02/10/13664328_1581264198_image1_M.jpg', -- image_url
	3,  -- product_info_id
	1,  -- image_size_id
	1 -- image_order
),(
	8, -- product_image_no
	'https://image.brandi.me/cproductdetail/2020/02/10/051ab4b12c1dc3c3cdbed61944ae2799.jpeg',  -- image_url
	3,  -- product_info_id
	2,  -- image_size_id
	1 -- image_order
),(
	9,  -- product_image_no
	'https://image.brandi.me/cproductdetail/2020/03/16/63a59a5211cb6f5b6e69313411684950.JPG',  -- image_url
	3,  -- product_info_id
	3,  -- image_size_id
	1 -- image_order
),(
	10,  -- product_image_no
	'https://image.brandi.me/cproductdetail/2020/03/16/63a59a5211cb6f5b6e69313411684950.JPG',  -- image_url
	4,  -- product_info_id
	1,  -- image_size_id
	1 -- image_order
),(
	11,  -- product_image_no
	'https://image.brandi.me/cproductdetail/2020/03/16/63a59a5211cb6f5b6e69313411684950.JPG',  -- image_url
	4,  -- product_info_id
	2,  -- image_size_id
	1 -- image_order
),(
	12,  -- product_image_no
	'https://image.brandi.me/cproductdetail/2020/03/16/63a59a5211cb6f5b6e69313411684950.JPG',  -- image_url
	4,  -- product_info_id
	3,  -- image_size_id
	1 -- image_order
);


-- authorization_types Table Create SQL
CREATE TABLE product_tags
(
    `product_tag_no`  INT            NOT NULL    AUTO_INCREMENT COMMENT 'id',
    `name`            VARCHAR(20)    NOT NULL    COMMENT '태그명',
    `product_info_id` INT            NOT NULL    COMMENT '상품 정보 외래키',
    `is_deleted`      TINYINT        NOT NULL    DEFAULT FALSE COMMENT '삭제여부',
    PRIMARY KEY (product_tag_no)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci COMMENT '상품 태그 관리';

ALTER TABLE product_tags
    ADD CONSTRAINT FK_product_info_id FOREIGN KEY (product_info_id)
        REFERENCES product_infos (product_info_no);

INSERT INTO product_tags
(
	product_tag_no,
	name,
	product_info_id
) VALUES (
	1,
	'봄',
	1
),(
	2,
	'4월',
	1
),(
	3,
	'맨투맨',
	2
),(
	4,
	'이벤트가격',
	2
),(
	5,
	'롱원피스',
	3
),(
	6,
	'새학기',
	3
);


-- product_change_histories Table Create SQL
CREATE TABLE product_change_histories
(
    `product_change_history_no`  INT              NOT NULL    AUTO_INCREMENT COMMENT 'id',
    `product_id`                 INT              NOT NULL    COMMENT '변경된 상품 아이디',
    `modifier`                   INT              NOT NULL    COMMENT '수정자',
    `changed_time`               DATETIME         NOT NULL    COMMENT '수정 날짜',
    `is_available`               TINYINT          NOT NULL    COMMENT '판매여부',
    `is_on_display`              TINYINT          NOT NULL    COMMENT '진열여부',
    `price`                      INT              NOT NULL    COMMENT '판매가격',
    `discount_rate`              DECIMAL(2, 2)    NOT NULL    COMMENT '할인율',
    `is_deleted`                 TINYINT          DEFAULT FALSE NOT NULL    COMMENT '삭제여부',
    PRIMARY KEY (product_change_history_no)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci COMMENT '상품의 경우 전체 수량이 많아 이력 테이블 따로 관리';

ALTER TABLE product_change_histories
    ADD CONSTRAINT FK_product_change_histories_product_id FOREIGN KEY (product_id)
        REFERENCES products (product_no);

ALTER TABLE product_change_histories
    ADD CONSTRAINT FK_product_change_histories_modifier FOREIGN KEY (modifier)
        REFERENCES accounts (account_no);

INSERT INTO product_change_histories
(
    product_change_history_no,
    product_id,
    modifier,
    changed_time,
    is_available,
    is_on_display,
    price,
    discount_rate,
    is_deleted
) VALUES (
    1, -- product_change_history_no
    1, -- product_id
    1, -- modifier
    '2020-03-31 09:00:00', -- changed_time
    1, -- is_available
    1, -- is_on_display
    12000, -- price
    0.3, -- discount_rate
    0 -- is_deleted
),(
    2, -- product_change_history_no
    2, -- product_id
    3, -- modifier
    '2020-04-01 09:00:00', -- changed_time
    1, -- is_available
    1, -- is_on_display
    15000, -- price
    0.5, -- discount_rate
    0 -- is_deleted
),(
    3, -- product_change_history_no
    3, -- product_id
    4, -- modifier
    '2020-04-02 09:00:00', -- changed_time
    1, -- is_available
    1, -- is_on_display
    15000, -- price
    0.4, -- discount_rate
    0 -- is_deleted
),(
    4, -- product_change_history_no
    4, -- product_id
    4, -- modifier
    '2020-04-03 09:00:00', -- changed_time
    1, -- is_available
    1, -- is_on_display
    12080, -- price
    0.3, -- discount_rate
    0 -- is_deleted
),(
    5, -- product_change_history_no
    5, -- product_id
    4, -- modifier
    '2020-04-04 09:00:00', -- changed_time
    1, -- is_available
    1, -- is_on_display
    129000, -- price
    0.45, -- discount_rate
    0 -- is_deleted
),(
    6, -- product_change_history_no
    6, -- product_id
    5, -- modifier
    '2020-04-05 09:00:00', -- changed_time
    1, -- is_available
    1, -- is_on_display
    18000, -- price
    0.15, -- discount_rate
    0 -- is_deleted
);

-- event_detail_infos Table Create SQL
CREATE TABLE event_detail_infos
(
    `event_detail_info_no`     INT            NOT NULL    AUTO_INCREMENT COMMENT 'id',
    `button_name`              VARCHAR(45)    NULL        COMMENT '이벤트 버튼이름',
    `button_link_type_id`      INT            NULL        COMMENT '이벤트 버튼 링크타입 아이디',
    `button_link_description`  VARCHAR(45)    NULL        COMMENT '이벤트 버튼 링크내용',
    `event_info_id`            INT            NOT NULL    COMMENT '기획전 정보 아이디',
    `is_deleted`               TINYINT        NOT NULL    DEFAULT FALSE COMMENT '삭제여부',
    PRIMARY KEY (event_detail_info_no)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci COMMENT '이벤트 상세정보';

ALTER TABLE event_detail_infos
    ADD CONSTRAINT FK_button_link_type_id FOREIGN KEY (button_link_type_id)
        REFERENCES event_button_link_types (event_button_link_type_no);

ALTER TABLE event_detail_infos
    ADD CONSTRAINT FK_event_info_id FOREIGN KEY (event_info_id)
        REFERENCES event_infos (event_info_no);

INSERT INTO event_detail_infos
(
	event_detail_info_no,
	button_name,
	button_link_type_id,
	event_info_id
) VALUES (
	1, -- event_detail_info_no
	'1번 이벤트 버튼',	-- button_name
	1, -- button_link_type_id
	1 -- event_info_id
),(
	2, -- event_detail_info_no
	'2번 이벤트 버튼', -- button_name
	2, -- buttion_link_type_id
	2 -- event_info_id
),(
	3, -- event_detail_info_no
	'3번 이벤트 버튼', -- button_name
	3, -- button_link_type_id
	3 -- event_info_id
),(
	4, -- event_detail_info_no
	'4번 이벤트 버튼',
	4, -- buttion_link_type_id
	4 -- event_info_id
);



-- event_detail_product_infos Table Create SQL
CREATE TABLE event_detail_product_infos
(
	`event_detail_product_info_no`  INT        NOT NULL    AUTO_INCREMENT COMMENT 'id',
    `product_order`                 INT        NOT NULL    COMMENT '진열순위',
    `product_id`                    INT        NOT NULL    COMMENT '상품 아이디',
    `event_info_id`                 INT        NOT NULL    COMMENT '기획전 정보 아이디',
    `is_deleted`                    TINYINT    NOT NULL    DEFAULT FALSE COMMENT '삭제여부',
	PRIMARY KEY (event_detail_product_info_no)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci COMMENT '이벤트 상세정보(매핑 상품)';

ALTER TABLE event_detail_product_infos
	ADD CONSTRAINT FK_event_detail_product_infos_product_id FOREIGN KEY (product_id)
		REFERENCES product_infos (product_info_no);

ALTER TABLE event_detail_product_infos
    ADD CONSTRAINT FK_event_detail_product_infos_event_info_id FOREIGN KEY (event_info_id)
        REFERENCES event_infos (event_info_no);

INSERT INTO event_detail_product_infos
(
	event_detail_product_info_no,
	product_order,
	product_id,
	event_info_id
) VALUES (
	1, -- no
	1, -- product_order
	1, -- product_id
	5 -- event_info_id
),(
	2, -- no
	2, -- product_order
	2, -- product_id
	5 -- event_info_id
),(
	3, -- no
	3, -- product_order
	3, -- product_id
	5 -- event_info_id
),(
	4, -- no
	1, -- product_order
	1, -- product_id
	6 -- event_info_id
),(
	5, -- no
	2, -- product_order
	2, -- product_id
	6 -- event_info_id
),(
	6, -- no
	1, -- product_order
	3, -- product_id
	7 -- event_info_id
),(
	7, -- no
	2, -- product_order
	1, -- product_id
	7 -- event_info_id
),(
	8, -- no
	3, -- product_order
	2, -- product_id
	7 -- event_info_id
),(
	9, -- no
	1, -- product_order
	2, -- product_id
	8 -- event_info_id
),(
	10, -- no
	2, -- product_order
	3, -- product_id
	8 -- event_info_id
),(
	11, -- no
	3, -- product_order
	4, -- product_id
	8 -- event_info_id
);

-- seller_status_change_histories Table Create SQL
CREATE TABLE seller_status_change_histories
(
    `seller_status_change_history_no`  INT         NOT NULL    AUTO_INCREMENT COMMENT 'id',
    `seller_account_id`                INT         NOT NULL    COMMENT '셀러 계정 외래키',
    `changed_time`                     DATETIME    NOT NULL    DEFAULT CURRENT_TIMESTAMP COMMENT '셀러상태 변경 적용일시',
    `seller_status_id`                 INT         NOT NULL    COMMENT '셀러상태 외래키',
    `modifier`                         INT         NOT NULL    COMMENT '변경 실행자',
    PRIMARY KEY (seller_status_change_history_no)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci COMMENT '셀러상태 변경 기록';

ALTER TABLE seller_status_change_histories
    ADD CONSTRAINT FK_status_change_history_seller_account_id FOREIGN KEY (seller_account_id)
        REFERENCES seller_accounts (seller_account_no);

ALTER TABLE seller_status_change_histories
    ADD CONSTRAINT FK_status_change_history_seller_status_id FOREIGN KEY (seller_status_id)
        REFERENCES seller_statuses (status_no);

INSERT INTO seller_status_change_histories
(
	seller_status_change_history_no,
	seller_account_id,
	changed_time,
	seller_status_id,
	modifier
) VALUES (
	1, -- no
	2, -- seller_account_id
	'2020-03-31 23:59:59', -- changed_time
	1, -- seller_status_id
	2  -- modifier
),(
	2, -- no
	2, -- seller_account_id
	'2020-04-01 02:59:59', -- changed_time
	2, -- seller_status_id
	1  -- modifier
),(
	3, -- no
	2, -- seller_account_id
	'2020-04-01 05:59:59', -- changed_time
	3, -- seller_status_id
	1  -- modifier
),(
	4, -- no
	2, -- seller_account_id
	'2020-04-01 07:59:59', -- changed_time
	4, -- seller_status_id
	1  -- modifier
)
