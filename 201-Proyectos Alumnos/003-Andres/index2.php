<!doctype>
<html>
	<head>
  	<meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
    	#ruleta{animation:frena 10s;width:500px;height:500px;position:relative;
      animation-fill-mode: forwards;}
      @keyframes frena{
      	0%{transform:rotate(0deg);}
        100%{transform:rotate(359deg);}
      }
      #bolita{position:absolute;top:150px;left:150px;background:white;width:20px;
      height:20px;border-radius:20px;animation:mueve_bola 10s;animation-fill-mode: forwards;}
      @keyframes mueve_bola{
      	0%{left:250px;top:250px;}
        100%{left:250px;top:400px;}
      }
    </style>
  </head>
  <body>
  	<div id="ruleta">
  		<img  src="ruleta.jpg">
      <div id="bolita"></div>
    </div>
  </body>
</html>