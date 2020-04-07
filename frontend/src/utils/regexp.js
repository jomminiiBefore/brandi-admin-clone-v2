// 이메일 정규식
export const check_email = /([\w-\.]+)@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.)|(([\w-]+\.)+))([a-zA-Z]{2,4}|[0-9]{1,3})(\]?)$/;
// 대문자 정규식
export const upper_case = /[A-Z]/;
// 소문자 정규식
export const lower_case = /^[a-z]+$/;
// 숫자 정규식
export const number_case = /\d/;
// 3자리
export const numberFormat = x => {
  x = x.replace(/^[0]|[^0-9,]/g, ""); // 입력값이 숫자 및 0으로 시작하는 것이 아니면 공백
  x = x.replace(/,/g, ""); // ,값 공백처리
  return x.replace(/\B(?=(\d{3})+(?!\d))/g, ","); // 정규식을 이용해서 3자리 마다 , 추가
};
export const removeComma = str => {
  return parseInt(str.replace(/,/g, ""));
};

// id 시작글자
export const id_start = /^[a-z]+[a-z0-9]/;

// 한글 영문 숫자 허용 정규식
export const korean_english_number = /^[ㄱ-ㅎ|가-힣|a-z|A-Z|0-9|\*]+$/;

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
