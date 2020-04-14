// 이메일 정규식
export const check_email = /([\w-\.]+)@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.)|(([\w-]+\.)+))([a-zA-Z]{2,4}|[0-9]{1,3})(\]?)$/;
// 대문자 정규식
export const upper_case = /[A-Z]/;
// 소문자 정규식
export const lower_case = /^[a-z]+$/;
// 숫자 정규식
export const number_case = /\d/;
// id 시작글자
export const id_start = /^[a-z]+[a-z0-9]/;
// 한글 영문 숫자 정규식
export const korean_english_number = /^[ㄱ-ㅎ|가-힣|a-z|A-Z|0-9|\*]+$/;
// 10자리 숫자만
export const ten_number_case = /^[0-9]{10,10}$/;
// 한글 영문 숫자
export const korean_number_hypen_case = /^[ㄱ-ㅎ|가-힣|0-9|-]+$/;
// 영어 소문자, 숫자, 밑줄, 마침표
export const lower_number_underline_dot_case = /^[a-z|0-9|_|.]+$/;
// 숫자, 하이픈
export const number_hypen_case = /^[0-9|-]+$/;
// 2글자 이상
export const two_length_case = /^.{2}/;
// 4글자 이상
export const four_length_case = /^.{4}/;
// 숫자만
export const only_number_case = /^[0-9]*$/;
// 3자리
export const numberFormat = (x) => {
  x = x.replace(/^[0]|[^0-9,]/g, ''); // 입력값이 숫자 및 0으로 시작하는 것이 아니면 공백
  x = x.replace(/,/g, ''); // ,값 공백처리
  return x.replace(/\B(?=(\d{3})+(?!\d))/g, ','); // 정규식을 이용해서 3자리 마다 , 추가
};
export const removeComma = (str) => {
  return parseInt(str.replace(/,/g, ''));
};

// id 정규식
export const check_id = /[a-zA-Z0-9-_]{5,20}/;

// 4글자 이상
export const len_four = /[a-zA-Z0-9-_]{4,}/;

// 핸드폰
export const cellphone_num = /^\d{3}[-]\d{3,4}[-]\d{4}$/;

// 전화번호
export const check_num = /(^02.{0}|^01.{1}|[0-9]{4})-([0-9]+)-([0-9]{4})/;

// URL 주소
export const check_url = /(http|https):\/\/(\w+:{0,1}\w*@)?(\S+)(:[0-9]+)?(\/|\/([\w#!:.?+=&%@!\-\/]))?/;

export const business_number_case = /^[0-9]{3}-{1}[0-9]{2}-{1}[0-9]{5}$/;
