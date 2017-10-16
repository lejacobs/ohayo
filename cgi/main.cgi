#! /usr/bin/env python

print "Content-Type: text/html"
print
print """\

<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <meta name="author" content="">
    <link rel="icon" href="favicon.ico">

    <title>Bedroom Music Player</title>

    <!-- Bootstrap core CSS -->
    <link href="css/bootstrap.min.css" rel="stylesheet">

    <!-- Custom styles for this template -->
    <link href="starter-template.css" rel="stylesheet">

    <!-- Just for debugging purposes. Don't actually copy these 2 lines! -->
    <!--[if lt IE 9]><script src="js/ie8-responsive-file-warning.js"></script><![endif]-->
    <script src="js/ie-emulation-modes-warning.js"></script>

    <!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
    <!--[if lt IE 9]>
      <script src="https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script>
      <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
    <![endif]-->
  </head>

  <body>

    <nav class="navbar navbar-inverse navbar-fixed-top" role="navigation">
      <div class="container">
        <div class="navbar-header">
          <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false" aria-controls="navbar">
            <span class="sr-only">Toggle navigation</span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
          <a class="navbar-brand" href="#">Music Player</a>
        </div>
        <div id="navbar" class="collapse navbar-collapse">
          <ul class="nav navbar-nav">
            <li class="active"><a href="#">Home</a></li>
            <li><a href="#about">About</a></li>
            <li><a href="#contact">Contact</a></li>
          </ul>
        </div><!--/.nav-collapse -->
      </div>
    </nav>

    <div class="container">

      <div class="starter-template">
        <h1>Ohayo Radio V1.23</h1>
      </div>

    </div><!-- /.container -->

    <p>
      <button type="button" class="btn btn-lg btn-primary" onclick="location.href='http://ohayo/cgi-bin/kdfc.cgi'">KDFC</button>
      <button type="button" class="btn btn-lg btn-primary" onclick="location.href='http://ohayo/cgi-bin/kqed.cgi'">KQED</button>
      <button type="button" class="btn btn-lg btn-primary" onclick="location.href='http://ohayo/cgi-bin/kusc.cgi'">KUSC</button>
      <button type="button" class="btn btn-lg btn-warning" onclick="location.href='http://ohayo/cgi-bin/stop.cgi'">Stop</button>
    </p>

    <div class="container">

      <div class="starter-template">
        <h2>Volume</h1>
      </div>
    </div><!-- /.container -->

    <p>
      <button type="button" class="btn btn-lg btn-primary" onclick="location.href='http://ohayo/cgi-bin/ten.cgi'">10</button>
      <button type="button" class="btn btn-lg btn-primary" onclick="location.href='http://ohayo/cgi-bin/tenless.cgi'">-10</button>
      <button type="button" class="btn btn-lg btn-primary" onclick="location.href='http://ohayo/cgi-bin/tenmore.cgi'">+10</button>
      <button type="button" class="btn btn-lg btn-primary" onclick="location.href='http://ohayo/cgi-bin/sixty.cgi'">60</button>
    </p>

    <!-- Bootstrap core JavaScript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>
    <script src="js/bootstrap.min.js"></script>
    <!-- IE10 viewport hack for Surface/desktop Windows 8 bug -->
    <script src="js/ie10-viewport-bug-workaround.js"></script>
  </body>
</html>

"""

