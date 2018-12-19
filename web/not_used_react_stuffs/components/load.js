function test(input) {
   $.ajax({
      type: "POST",
      url: "/test.py",
      data: { param: input },
      success: callbackFunc
   });
}
function callbackFunc(response) {
   console.log(response);
}