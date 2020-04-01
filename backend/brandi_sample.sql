CREATE DATABASE brandi2 CHARACTER SET utf8mb4;-- COLLATE utf8mb4_general_ci;

use brandi2

-- authorization_types Table Create SQL
CREATE TABLE seller_infos
(
	seller_info_no INT NOT NULL PRIMARY KEY AUTO_INCREMENT COMMENT 'id',
	name_kr VARCHAR(45) NOT NULL, 
	name_en VARCHAR(45) NOT NULL, 
	site_url VARCHAR(1000) NOT NULL,
	center_number VARCHAR(14) NOT NULL
) ENGINE=INNODB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci COMMENT '권한 타입(마스터 or 셀러)';

ALTER TABLE seller_infos COMMENT '셀러 수정페이지 전체 / 셀러 정보 수정할때마다 새로운 row로 생성(변경이력 관리 용)';
-- authorization_types Table Create SQL
CREATE TABLE manager_infos
(
    manager_info_no  INT             NOT NULL    AUTO_INCREMENT COMMENT 'id',
    contact_number   VARCHAR(14)     NOT NULL    COMMENT '담당자 번호',
    seller_id        INT             NOT NULL    COMMENT '셀러 아이디',
    is_deleted       TINYINT         NOT NULL    COMMENT '삭제여부',
    PRIMARY KEY (manager_info_no)
) ENGINE=INNODB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci COMMENT '권한 타입(마스터 or 셀러)';
ALTER TABLE manager_infos COMMENT '셀러 담당자 정보';
ALTER TABLE manager_infos
    ADD CONSTRAINT FK_manager_infos_seller_id_seller_infos_seller_info_no FOREIGN KEY (seller_id)
        REFERENCES seller_infos (seller_info_no) ON DELETE RESTRICT ON UPDATE RESTRICT;
