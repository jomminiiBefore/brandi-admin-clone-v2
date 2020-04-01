// 이메일 정규식
export const check_email = /([\w-\.]+)@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.)|(([\w-]+\.)+))([a-zA-Z]{2,4}|[0-9]{1,3})(\]?)$/;
// 대문자 정규식
export const upper_case = /[A-Z]/;
// 소문자 정규식
export const lower_case = /[a-z]/;
// 숫자 정규식
export const number_case = /\d/;
// 3자리
export const numberFormat = x => {
  x = x.replace(/^[0]|[^0-9,]/g, ''); // 입력값이 숫자 및 0으로 시작하는 것이 아니면 공백
  x = x.replace(/,/g, ''); // ,값 공백처리
  return x.replace(/\B(?=(\d{3})+(?!\d))/g, ','); // 정규식을 이용해서 3자리 마다 , 추가
};
export const removeComma = str => {
  return parseInt(str.replace(/,/g, ''));
};
