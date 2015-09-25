from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("""
    <h1>Hello world!</h1>
    <p>Haha this is only for testing purpose!</p>
    <p>You can click <a href= "/hello/nice">here</a> to see more!</p>
    """)

def nice(request):
    return HttpResponse("""
<head>
<title> First html </title>
<style>
body {background-color: lightgrey}
h1 {text-align: center; color: blue; font-size: 300%}
p#p01  {color: green;
	border: 1px solid black;
	padding: 10px;
	margin: 30px
}
p {
	color: yellow;
	padding: 10px
}
</style>
</head>

<body>
<h1> The first heading </h1>
<p id="p01">This is a paragraph to show that I have understood some of the html5 features</p>

<p id="p02"> This is another paragraph just for fun</p>
<p>You can click <a href= "/hello">here</a> to return back!</p>


</body>

""")

def home(request):
    return render(request, "home.html", {})