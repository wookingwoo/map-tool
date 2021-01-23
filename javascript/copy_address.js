function copyToClipboard(text) {

  const span_result_MSG = document.getElementById('copy_result_msg');

  var copy_string = document.createElement("textarea");

  document.body.appendChild(copy_string);
  copy_string.value = text;
  copy_string.select();


  try {
    var copying = document.execCommand('copy');
    var resultMSG = copying ? '복사 완료' : '복사 실패';
    span_result_MSG.innerHTML = resultMSG;
    document.body.removeChild(copy_string);
  } catch (e) {
    span_result_MSG.innerHTML = '복사 실패';
  }


}
