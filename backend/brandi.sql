CREATE DATABASE brandi2 default CHARACTER SET UTF8;

use brandi2

-- Create SQL for authorization_type table
CREATE TABLE authorization_types(
	auth_type_no INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY COMMENT 'id',
	name		 VARCHAR(45)  NOT NULL COMMENT '타입명',
	is_deleted	 TINYINT      NOT NULL COMMENT '삭제여부' DEFAULT 0
) ENGINE=INNODB CHARSET=utf8;

ALTER TABLE authorization_types COMMENT '권한타입(마스터 or 셀러)';

-- Create SQL for accounts table
CREATE TABLE accounts
(
	account_no	 INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY COMMENT 'id',
	login_id	 VARCHAR(45)  NOT NULL COMMENT '로그인 아이디',
	password	 VARCHAR(80)  NOT NULL COMMENT '비밀번호',
	is_deleted   TINYINT	  NOT NULL COMMENT '삭제여부' DEFAULT 0,
	auth_type_id INT UNSIGNED         NOT NULL COMMENT '권한 타입'
) ENGINE=INNODB CHARSET=utf8;

ALTER TABLE accounts COMMENT '계정 정보';

ALTER TABLE accounts
    ADD CONSTRAINT FK_accounts_auth_type_id_authorization_types_auth_type_no FOREIGN KEY (auth_type_id)
        REFERENCES authorization_types (auth_type_no) ON DELETE RESTRICT ON UPDATE RESTRICT;

-- Create SQL for seller_accounts table
CREATE TABLE seller_accounts
(
	seller_account_no INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY COMMENT 'id',
	created_at DATETIME NOT NULL COMMENT '최초 등록일시',
	is_deleted TINYINT  NOT NULL COMMENT '삭제여부',
	account_id INT UNSIGNED		NOT NULL COMMENT '계정 정보 아이디'
) ENGINE=INNODB CHARSET=utf8;

ALTER TABLE seller_accounts COMMENT '셀러 계정';

ALTER TABLE seller_accounts
	ADD CONSTRAINT FK_seller_accounts_account_id_accounts_account_no FOREIGN KEY (account_id)
		REFERENCES accounts (account_no) ON DELETE RESTRICT ON UPDATE RESTRICT;
