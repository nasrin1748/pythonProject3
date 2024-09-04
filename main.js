function square(number) {
        return number * number;
}

function run(){
              let htmlCode = document.getElementById("html-code").value;
              let cssCode = document.getElementById("css-code").value;
              let jsCode = document.getElementById("js-code").value;
              let output = document.getElementById("output");

              output.contentDocument.body.innerHTML = htmlCode+ "<style>" +cssCode+ "</style>";
              output.contentWindow.eval(jsCode);
        }
function imp(){
var iframe = document.getElementById( 'ifrm' );
	var content = document.getElementById("iframeContent").innerHTML;
	var frameDoc = iframe.document;
	if (iframe.contentWindow)
		frameDoc = iframe.contentWindow.document;

	frameDoc.open();
	frameDoc.writeln(content);
	frameDoc.close();
	}

function input() {
      const userInput = prompt("Please enter your name:");
      return userInput;

  }
