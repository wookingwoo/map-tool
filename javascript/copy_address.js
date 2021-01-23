
  
  
  // function copy_address(){
  //   const successMSG = document.getElementById('success_msg');
  //   const copy_string = document.querySelector('#copy_string');
  //   const selection = window.getSelection();
  //   const range = document.createRange();
  //   range.selectNode(copy_string);
  //   selection.removeAllRanges();
  //   selection.addRange(range);
    
  //   try{
  //     var successful = document.execCommand('copy');
  //     var resultMSG = successful ? '복사 완료' : '복사 실패'; 
  //     successMSG.innerHTML=resultMSG;
  //     selection.removeAllRanges();
  //   }catch(e){
  //     successMSG.innerHTML=resultMSG;
  //   }
  // }
  





  function copyToClipboard(text) {
    var dummy = document.createElement("textarea");
    // to avoid breaking orgain page when copying more words
    // cant copy when adding below this code
    // dummy.style.display = 'none'
    document.body.appendChild(dummy);
    //Be careful if you use texarea. setAttribute('value', value), which works with "input" does not work with "textarea". – Eduard
    dummy.value = text;
    dummy.select();
    document.execCommand("copy");
    document.body.removeChild(dummy);
}
